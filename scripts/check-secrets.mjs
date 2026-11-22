#!/usr/bin/env node
// Block commits that would publish private data. Runs as a git pre-commit hook (.githooks/pre-commit).
//   node scripts/check-secrets.mjs            # check staged changes (what's about to be committed)
//   node scripts/check-secrets.mjs --all      # check every tracked file
// Rule: API keys, tokens, passwords, private keys and personal email addresses never go into git.
// Keys belong in .env (ignored); .env.example holds the names with empty values.
import { execFileSync } from "node:child_process";
import fs from "node:fs";

const git = (...a) => execFileSync("git", a, { encoding: "utf8", maxBuffer: 64 * 1024 * 1024 });
const all = process.argv.includes("--all");
const problems = [];

// 1. Files that must never be committed
const BLOCKED_FILES = [
  [/(^|\/)\.env(\.[\w-]+)?$/, "environment file with keys (only .env.example may be committed)"],
  [/(^|\/)\.mcp\.json$/, "MCP config (may hold tokens); commit .mcp.json.example instead"],
  [/(^|\/)\.claude\/settings\.local\.json$/, "personal Claude Code settings"],
  [/(^|\/)app\/\.data\//, "local app data (settings, job history)"],
  [/\.(pem|key|p12|pfx|keystore|jks)$|(^|\/)id_(rsa|ed25519|ecdsa)(\.pub)?$/, "private key or certificate"],
  [/(^|\/)(credentials|secrets?)\.(json|ya?ml|txt)$/i, "credentials file"],
];
const files = (all ? git("ls-files") : git("diff", "--cached", "--name-only", "--diff-filter=ACMR")).split("\n").filter(Boolean);
for (const f of files) {
  if (/(^|\/)\.env\.example$/.test(f)) continue;
  for (const [re, why] of BLOCKED_FILES) if (re.test(f)) problems.push(`${f}: ${why}`);
}

// 2. Secrets and personal data inside the added lines
const PATTERNS = [
  [/\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{20,}/, "API key (sk-…)"],
  [/\bsk_[A-Za-z0-9]{24,}/, "API key (sk_…)"],
  [/\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{40,}/, "GitHub token"],
  [/\bAKIA[0-9A-Z]{16}\b/, "AWS access key"],
  [/\bAIza[0-9A-Za-z_-]{35}\b/, "Google API key"],
  [/\bxox[abposr]-[A-Za-z0-9-]{10,}/, "Slack token"],
  [/\bapify_api_[A-Za-z0-9]{20,}/, "Apify token"],
  [/\br8_[A-Za-z0-9]{30,}/, "Replicate token"],
  [/-----BEGIN [A-Z ]*PRIVATE KEY-----/, "private key"],
  [/\b(?:[A-Z0-9_]*(?:API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|PRIVATE_KEY))\s*[=:]\s*["']?(?!\$\{)[A-Za-z0-9_./+=-]{12,}/, "a key, token or password assigned a real value"],
  [/\b(?:password|passwd|pwd)\s*[=:]\s*["'][^"'\s]{6,}["']/i, "password"],
  [/[A-Za-z0-9._%+-]+@(?:gmail|googlemail|yahoo|hotmail|outlook|live|icloud|me|aol|proton(?:mail)?|gmx|yandex|mail)\.(?:com|me|net|ru|de)\b/i, "personal email address"],
];
const skipContent = (f) => /\.(png|jpe?g|webp|gif|mp4|mov|webm|mp3|wav|m4a|ogg|woff2?|ttf|otf|ico|pdf|zip)$/i.test(f) || /package-lock\.json$/.test(f) || f === "scripts/check-secrets.mjs";
for (const f of files) {
  if (skipContent(f)) continue;
  let text;
  if (all) {
    try {
      text = fs.readFileSync(f, "utf8");
    } catch {
      continue;
    }
  } else {
    text = git("diff", "--cached", "-U0", "--", f)
      .split("\n")
      .filter((l) => l.startsWith("+") && !l.startsWith("+++"))
      .map((l) => l.slice(1))
      .join("\n");
  }
  text.split("\n").forEach((line, i) => {
    for (const [re, why] of PATTERNS) if (re.test(line)) problems.push(`${f}${all ? `:${i + 1}` : ""}: ${why} → ${line.trim().slice(0, 90)}`);
  });
}

// 3. The commit itself must not carry a personal email
const email = (() => {
  try {
    return git("config", "user.email").trim();
  } catch {
    return "";
  }
})();
if (!all && email && !/@users\.noreply\.github\.com$|^noreply@/i.test(email))
  problems.push(`commit email is ${email}; use your GitHub noreply address: git config user.email "<id>+<user>@users.noreply.github.com"`);

if (problems.length) {
  console.error("\x1b[31m✖ Commit blocked: private data would be published\x1b[0m\n  " + problems.join("\n  "));
  console.error("\nMove keys to .env (ignored by git), remove personal emails, then commit again.");
  console.error("If a match is a false alarm, adjust scripts/check-secrets.mjs rather than skipping the check.");
  process.exit(1);
}
if (all) console.log(`✔ ${files.length} tracked files checked: no keys, passwords or personal emails`);
