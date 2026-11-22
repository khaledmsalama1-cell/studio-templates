# studio-templates

The template registry for [Studio](https://github.com/khaledmsalama1-cell/studio): {{COUNT}} templates — {{STUDIO}} ready-to-use studio templates and {{EXTERNAL}} external starters — plus 100 brand starters.

The Studio scans this repo (**Apps → Sources → Refresh**) and shows the templates in **Create → Templates**, each drawn live in your brand's colours, fonts and logo. Picking one creates a project with the template's scenes, filled in from the brand.

## How a template works

A studio template is a list of scenes using the Studio's scene types — `hook`, `point`, `list`, `stat`, `quote`, `media`, `cta` — for one format (`reel`, `promo`, `landscape`, `carousel`, `post`, `square`, `story`). Video templates include a `say` line per scene for the voiceover; scenes are cut on those words.

Placeholders are filled from the brand when the project is created:

| Placeholder | Filled with |
|---|---|
| `{{brand}}` | Brand name |
| `{{product}}` | First product in brand.json |
| `{{cta}}` | First call to action |
| `{{topic}}` | The topic you type, or the brand's first content pillar |
| `{{audience}}` | First persona's name |
| `{{handle}}` | Instagram or TikTok handle |

Wrap a word in `*asterisks*` to colour it with the brand accent. `media` scenes leave `src` empty so you pick a photo or clip in the project.

External starters (official Remotion templates, HyperFrames examples) are listed with links.

## Privacy

This registry is public. Entries never contain API keys, tokens, passwords or personal emails: integrations name the environment variables they need (for example `FAL_KEY`), and the Studio stores the values in its own git-ignored `.env`. A pre-commit hook ([`scripts/check-secrets.mjs`](scripts/check-secrets.mjs)) blocks commits that would add such data; enable it after cloning with `git config core.hooksPath .githooks`.

## Add a template

1. Create `templates/<format>/<id>.json` (copy an existing one; see [`schema.json`](schema.json)).
2. Run `node scripts/build-index.mjs`. It fails on unknown scene types, missing text or voiceover lines, and unknown placeholders.
3. Commit the template, `index.json` and `README.md`.

## Catalogue
