#!/usr/bin/env python3
"""Seed data for studio-templates. Writes templates/<format>/<id>.json.

Placeholders filled by the Studio from brand.json when a project is created:
  {{brand}} {{product}} {{cta}} {{topic}} {{audience}} {{handle}}
On-screen text stays short; video scenes carry a `say` voiceover line.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = []

# scene helpers -------------------------------------------------------------
def hook(text, say=None, sub=None, bg=None): return _s("hook", text=text, say=say, sub=sub, bg=bg)
def point(kicker, text, say=None, sub=None, bg=None): return _s("point", kicker=kicker, text=text, say=say, sub=sub, bg=bg)
def lst(text, items, say=None): return _s("list", text=text, items=items, say=say)
def stat(value, text, say=None, sub=None): return _s("stat", value=value, text=text, say=say, sub=sub)
def quote(text, author, say=None): return _s("quote", text=text, author=author, say=say)
def media(text, say=None, sub=None): return _s("media", src="", text=text, say=say, sub=sub)
def cta(text="{{cta}}", say=None, button=None, sub=None): return _s("cta", text=text, say=say, button=button, sub=sub)

def _s(type, **kw):
    return {"type": type, **{k: v for k, v in kw.items() if v is not None}}

def add(id, name, format, category, description, scenes, tags=()):
    T.append({"id": id, "name": name, "format": format, "category": category, "description": description, "tags": list(tags), "scenes": scenes})

# =================================================================== REELS (9:16 video)
add("reel-listicle-3", "3 things listicle", "reel", "education", "Three quick points with a strong hook. The most reliable short-form format.", [
    hook("3 things about *{{topic}}*", "Three things nobody tells you about {{topic}}."),
    point("01", "The first thing", "First: the thing most people get wrong."),
    point("02", "The second thing", "Second: the simple fix that changes it."),
    point("03", "The best one", "And third, the one that makes the biggest difference."),
    cta(say="Follow for more."),
], ["listicle", "tips"])
add("reel-listicle-5", "5 quick tips", "reel", "education", "Five fast tips for a high-retention 30-second reel.", [
    hook("5 *{{topic}}* tips in 30s", "Five {{topic}} tips in thirty seconds. Go."),
    point("1", "Tip one", "One."), point("2", "Tip two", "Two."), point("3", "Tip three", "Three."),
    point("4", "Tip four", "Four."), point("5", "Save this one", "And five, the one you'll want to save."),
    cta("Save this", "Save this for later."),
], ["listicle", "tips"])
add("reel-myth-fact", "Myth vs fact", "reel", "education", "Name a common belief, bust it, give the right move.", [
    hook("*Myth:* the common belief", "Here's a myth about {{topic}} that just won't die."),
    point("Why people believe it", "It sounds right", "It sounds right, so everyone repeats it."),
    point("The fact", "What's actually true", "But here's what's actually true."),
    point("Do this instead", "The better move", "So do this instead."),
    cta(say="Follow {{brand}} for more."),
], ["myth", "education"])
add("reel-before-after", "Before and after", "reel", "transformation", "Show the change your product makes.", [
    hook("From *this* to *this*", "Watch what happens when you switch to {{product}}."),
    media("Before", "Before: the usual problem."),
    point("The change", "One simple switch", "We changed one thing."),
    media("After", "After: the difference is obvious."),
    cta(say="Try it yourself. Link in bio."),
], ["transformation", "product"])
add("reel-how-to", "How to in 4 steps", "reel", "education", "A step-by-step tutorial with numbered scenes.", [
    hook("How to *{{topic}}*", "Here's how to {{topic}}, step by step."),
    point("Step 1", "Start here", "Step one."), point("Step 2", "Then this", "Step two."),
    point("Step 3", "Then this", "Step three."), point("Step 4", "Finish strong", "And step four."),
    cta("Save the steps", "Save this so you have the steps."),
], ["tutorial", "how-to"])
add("reel-pas", "Problem → solution", "reel", "promo", "Problem, agitate, solve: the classic ad structure.", [
    hook("Tired of *the problem*?", "Tired of dealing with the same problem every day?"),
    point("It gets worse", "It costs you more than you think", "It costs you time, money, and patience."),
    media("{{product}}", "Meet {{product}}."),
    lst("Why it works", ["Benefit one", "Benefit two", "Benefit three"], "It fixes it in three ways."),
    cta(button="Shop now", say="Get yours today."),
], ["ad", "pas"])
add("reel-product-launch", "Product launch", "reel", "launch", "Announce something new with build-up and a clear CTA.", [
    hook("It's *finally* here", "It's finally here."),
    media("Introducing {{product}}", "Introducing {{product}}."),
    lst("What's new", ["The headline feature", "The detail people love", "The price"], "Here's what's new."),
    stat("Today", "available now", "Available today."),
    cta(button="Get it first", say="Be one of the first. Link in bio."),
], ["launch", "announcement"])
add("reel-product-demo", "Product demo", "reel", "product", "Show the product doing its job in three beats.", [
    hook("Watch {{product}} in action", "Here's {{product}} in action."),
    media("Step one", "First, this."), media("Step two", "Then this."), media("The result", "And here's the result."),
    cta(say="Want one? Link in bio."),
], ["demo", "product"])
add("reel-testimonial", "Customer testimonial", "reel", "social-proof", "Lead with a real customer's words.", [
    hook("What our customers say", "Don't take our word for it."),
    quote("Add a real customer quote here", "Customer name", "Here's what one customer told us."),
    stat("4.9★", "average rating", "And they're not the only one."),
    cta(say="See why. Link in bio."),
], ["review", "proof"])
add("reel-bts", "Behind the scenes", "reel", "behind-the-scenes", "Show how it's made; builds trust and personality.", [
    hook("How we make *{{product}}*", "Ever wondered how we make {{product}}?"),
    media("Where it starts", "It starts here."), media("The part nobody sees", "This is the part nobody sees."),
    media("Ready for you", "And then it's ready for you."),
    cta(say="Follow {{brand}} for more behind the scenes."),
], ["bts", "process"])
add("reel-founder-story", "Founder story", "reel", "story", "Why the brand exists, told in 30 seconds.", [
    hook("Why we started *{{brand}}*", "This is why we started {{brand}}."),
    point("The moment", "It started with a problem", "It started with a problem we couldn't ignore."),
    point("The turn", "So we built the fix", "So we built the thing we wished existed."),
    point("Today", "Now it's for you", "And now it's here for people like you."),
    cta(say="Thanks for being part of it."),
], ["story", "founder"])
add("reel-day-in-life", "A day in the life", "reel", "behind-the-scenes", "Morning to night at the brand, in quick cuts.", [
    hook("A day at *{{brand}}*", "Come spend a day with us at {{brand}}."),
    media("Morning", "Morning."), media("Midday", "Midday."), media("Evening", "Evening."),
    cta(say="See you tomorrow."),
], ["vlog", "bts"])
add("reel-faq", "Answering an FAQ", "reel", "education", "Turn a common question into content.", [
    hook("You asked: *the question*?", "One of the questions we get the most."),
    point("Short answer", "The short answer", "The short answer is yes, and here's why."),
    lst("The details", ["Detail one", "Detail two", "Detail three"], "Here are the details."),
    cta("Ask us anything", "Got a question? Drop it in the comments."),
], ["faq", "community"])
add("reel-stat-shock", "Surprising stat", "reel", "education", "Lead with a number that stops the scroll.", [
    stat("73%", "of people get this wrong", "Seventy-three percent of people get this wrong."),
    point("Why it matters", "Here's why that matters", "Here's why that matters for you."),
    point("The fix", "Do this instead", "The fix is simpler than you think."),
    cta(say="Follow for more."),
], ["stat", "hook"])
add("reel-comparison", "Us vs them", "reel", "promo", "Compare the usual option with yours, honestly.", [
    hook("The usual way vs *our way*", "Here's the usual way, and here's ours."),
    lst("The usual way", ["Slower", "Costs more", "Same old result"], "The usual way."),
    lst("With {{product}}", ["Faster", "Fair price", "Better result"], "With {{product}}."),
    cta(say="You choose. Link in bio."),
], ["comparison", "ad"])
add("reel-mistakes", "Mistakes to avoid", "reel", "education", "Warn people off three common mistakes.", [
    hook("Stop making these *3 mistakes*", "Stop making these three mistakes with {{topic}}."),
    point("Mistake 1", "The first mistake", "Mistake one."), point("Mistake 2", "The second mistake", "Mistake two."),
    point("Mistake 3", "The worst one", "And the worst one."),
    cta(say="Follow so you don't miss the fixes."),
], ["mistakes", "tips"])
add("reel-hot-take", "Hot take", "reel", "opinion", "A strong opinion that sparks comments.", [
    hook("Unpopular opinion:", "Unpopular opinion."),
    point("The take", "Your bold statement", "Here it is."),
    point("Why", "Here's my reasoning", "And here's why I think that."),
    cta("Agree or disagree?", "Agree or disagree? Tell me in the comments."),
], ["opinion", "engagement"])
add("reel-countdown-sale", "Sale countdown", "reel", "promo", "Urgency for a sale or limited offer.", [
    hook("Our biggest sale *ends soon*", "Our biggest sale ends soon."),
    stat("30%", "off everything", "Thirty percent off everything."),
    stat("48h", "left", "Only forty-eight hours left."),
    cta(button="Shop the sale", say="Don't miss it. Link in bio."),
], ["sale", "urgency"])
add("reel-event", "Event promo", "reel", "event", "Promote an event, launch party or live session.", [
    hook("You're invited", "You're invited."),
    lst("Details", ["Date and time", "Place or link", "What to expect"], "Here are the details."),
    cta(button="Save your spot", say="Save your spot. Link in bio."),
], ["event", "invite"])
add("reel-announcement", "Big announcement", "reel", "announcement", "Share news with a reveal.", [
    hook("We have *news*", "We have some news."),
    point("The news", "What's happening", "Here's what's happening."),
    point("What it means", "What it means for you", "And here's what it means for you."),
    cta(say="More soon. Follow so you don't miss it."),
], ["news"])
add("reel-hiring", "We're hiring", "reel", "team", "Recruit with personality.", [
    hook("We're *hiring*", "We're hiring at {{brand}}."),
    point("The role", "Role title", "We're looking for someone to join as our next role."),
    lst("You'll love it if", ["You care about craft", "You like small teams", "You want to grow"], "You'll love it here if this sounds like you."),
    cta("Apply now", "Apply through the link in bio."),
], ["hiring", "team"])
add("reel-milestone", "Milestone thank-you", "reel", "community", "Celebrate a milestone with your audience.", [
    stat("10K", "of you. Thank you.", "Ten thousand of you. Thank you."),
    point("Where we started", "It started small", "We started with almost nothing."),
    point("What's next", "Here's what's next", "And here's what's coming next."),
    cta("Thank you", "Thank you for being here."),
], ["milestone", "community"])
add("reel-seasonal", "Seasonal moment", "reel", "seasonal", "Tie the brand to a holiday or season.", [
    hook("Your *season* starts here", "The season is here, and we're ready."),
    media("Seasonal pick", "Our pick for the season."),
    lst("Why now", ["Reason one", "Reason two", "Limited time"], "Here's why now."),
    cta(button="Shop the edit", say="Find it in the link in bio."),
], ["holiday", "seasonal"])
add("reel-tutorial-pov", "POV tutorial", "reel", "education", "First-person POV tutorial.", [
    hook("POV: you finally *get it right*", "POV: you finally get it right."),
    media("Step 1", "Step one."), media("Step 2", "Step two."), media("Done", "Done."),
    cta(say="Save it and try it tonight."),
], ["pov", "tutorial"])
add("reel-case-study", "Customer case study", "reel", "social-proof", "A real result with numbers.", [
    hook("How one customer *did it*", "Here's how one customer got real results."),
    point("The problem", "Where they started", "Here's where they started."),
    point("What changed", "What they did", "Here's what they changed."),
    stat("2×", "the result", "And here's the result."),
    cta(say="Want the same? Link in bio."),
], ["case-study", "proof"])
add("reel-ingredient", "Ingredient spotlight", "reel", "product", "Zoom in on one ingredient, material or feature.", [
    hook("The secret is *one ingredient*", "The secret is one ingredient."),
    media("Meet it", "Meet it."),
    lst("Why it matters", ["Benefit one", "Benefit two", "Where it comes from"], "Here's why it matters."),
    cta(say="Taste the difference."),
], ["product", "feature"])
add("reel-challenge", "Challenge or trend", "reel", "engagement", "Invite your audience into a challenge.", [
    hook("Try this *7-day challenge*", "Try this seven-day challenge."),
    lst("The rules", ["Rule one", "Rule two", "Rule three"], "Here are the rules."),
    cta("Tag us", "Tag us so we can see how it goes."),
], ["challenge", "ugc"])
add("reel-quote", "Quote of the day", "reel", "inspiration", "A short, shareable quote with voice.", [
    quote("A line worth sharing", "Author", "Here's something worth thinking about today."),
    cta(say="Share this with someone who needs it."),
], ["quote", "inspiration"])
add("reel-question", "Answer in one line", "reel", "engagement", "A question hook answered fast.", [
    hook("Why does *this happen*?", "Ever wondered why this happens?"),
    point("The answer", "Short answer", "Short answer: here's why."),
    cta(say="Follow for more quick answers."),
], ["question", "quick"])
add("reel-giveaway", "Giveaway", "reel", "promo", "Run a giveaway with simple steps.", [
    hook("*Giveaway* time", "It's giveaway time."),
    media("The prize", "Here's what you can win."),
    lst("How to enter", ["Follow {{handle}}", "Like this post", "Tag a friend"], "Here's how to enter."),
    cta("Good luck", "Winner announced Friday. Good luck."),
], ["giveaway", "growth"])

# =================================================================== PROMOS (9:16 product videos)
add("promo-classic", "Classic product promo", "promo", "promo", "Hook, product, benefits, proof, CTA.", [
    hook("Meet *{{product}}*", "Meet {{product}}."),
    media("{{product}}", "Made for people who care about quality."),
    lst("Why people love it", ["Benefit one", "Benefit two", "Benefit three"], "Here's why people love it."),
    stat("4.9★", "from real customers", "And customers agree."),
    cta(button="Shop now", say="Get yours today."),
], ["ad", "product"])
add("promo-ugc-style", "UGC-style ad", "promo", "promo", "Feels like a customer filming it themselves.", [
    hook("I didn't expect *this*", "Okay, I didn't expect this to actually work."),
    media("First impression", "First impression? Honestly, great."),
    point("The best part", "What surprised me", "The best part is how easy it is."),
    cta(button="Try it", say="Link in bio if you want to try it."),
], ["ugc", "ad"])
add("promo-offer", "Limited offer", "promo", "promo", "A direct-response promo for an offer.", [
    hook("This week only", "This week only."),
    stat("20%", "off {{product}}", "Twenty percent off {{product}}."),
    media("{{product}}", "Our best seller."),
    cta(button="Claim offer", say="Claim it before it's gone."),
], ["offer", "sale"])
add("promo-3-reasons", "3 reasons to try", "promo", "promo", "Three reasons, fast.", [
    hook("3 reasons to try *{{product}}*", "Three reasons to try {{product}}."),
    point("1", "Reason one", "One."), point("2", "Reason two", "Two."), point("3", "Reason three", "Three."),
    cta(button="Shop now", say="Link in bio."),
], ["ad", "reasons"])
add("promo-gift", "Gift idea", "promo", "seasonal", "Position the product as a gift.", [
    hook("The gift they'll *actually use*", "Looking for a gift they'll actually use?"),
    media("{{product}}", "Meet {{product}}."),
    lst("Perfect for", ["Who it's for", "Who else", "And you"], "Perfect for the people you love."),
    cta(button="Shop gifts", say="Order by Friday for delivery."),
], ["gift", "holiday"])
add("promo-bundle", "Bundle promo", "promo", "promo", "Sell a bundle with value math.", [
    hook("Better *together*", "Some things are better together."),
    lst("In the bundle", ["Item one", "Item two", "Item three"], "Here's what's in the bundle."),
    stat("Save 25%", "vs buying separately", "Save twenty-five percent compared to buying them separately."),
    cta(button="Get the bundle", say="Link in bio."),
], ["bundle", "value"])
add("promo-restock", "Back in stock", "promo", "launch", "Announce a restock.", [
    hook("It's *back*", "It's back in stock."),
    media("{{product}}", "The one you asked for."),
    stat("Limited", "quantities", "Quantities are limited."),
    cta(button="Shop now", say="Grab it while you can."),
], ["restock", "urgency"])
add("promo-new-flavor", "New variant", "promo", "launch", "Launch a new flavour, colour or version.", [
    hook("New *flavour* just dropped", "A new one just dropped."),
    media("Meet the new one", "Meet the new one."),
    lst("Tasting notes", ["Note one", "Note two", "Note three"], "Here's what it's like."),
    cta(button="Try it first", say="Try it first. Link in bio."),
], ["launch", "variant"])

# =================================================================== LANDSCAPE (16:9 video)
add("landscape-explainer", "Explainer", "landscape", "education", "A 16:9 explainer for YouTube or LinkedIn.", [
    hook("What is *{{topic}}*?", "What is {{topic}}, and why does it matter?"),
    point("The idea", "In one sentence", "In one sentence, here's the idea."),
    lst("Three things to know", ["First", "Second", "Third"], "Here are three things to know."),
    cta("Subscribe for more", "Subscribe for more."),
], ["youtube", "explainer"])
add("landscape-product-overview", "Product overview", "landscape", "product", "A clean overview of what the product does.", [
    hook("Meet {{product}}", "Meet {{product}}."),
    media("What it is", "Here's what it is."),
    lst("What it does", ["Feature one", "Feature two", "Feature three"], "Here's what it does."),
    quote("A customer quote", "Customer", "Here's what customers say."),
    cta(button="Learn more", say="Learn more at the link below."),
], ["product", "overview"])
add("landscape-tutorial", "Tutorial", "landscape", "education", "A longer step-by-step tutorial.", [
    hook("How to *{{topic}}*", "In this video, how to {{topic}}."),
    point("Step 1", "Get set up", "Step one: get set up."), point("Step 2", "Do the main thing", "Step two."),
    point("Step 3", "Check your work", "Step three."), point("Step 4", "Polish", "And step four."),
    cta("Subscribe", "If this helped, subscribe."),
], ["tutorial", "youtube"])
add("landscape-case-study", "Case study", "landscape", "social-proof", "A results story for B2B or LinkedIn.", [
    hook("How a customer *got results*", "Here's how one customer got real results."),
    point("Challenge", "The challenge", "The challenge."), point("Approach", "What we did", "What we did."),
    stat("+40%", "the result", "The result."),
    cta(button="Book a call", say="Want the same? Book a call."),
], ["b2b", "case-study"])
add("landscape-update", "Company update", "landscape", "announcement", "A short update for your audience or team.", [
    hook("What's new at {{brand}}", "Here's what's new at {{brand}}."),
    lst("This month", ["Update one", "Update two", "Update three"], "Three updates this month."),
    cta("Thanks for watching", "Thanks for watching."),
], ["update", "news"])
add("landscape-webinar", "Webinar promo", "landscape", "event", "Promote a webinar or live session.", [
    hook("Join our live session", "Join our live session."),
    lst("You'll learn", ["Lesson one", "Lesson two", "Lesson three"], "Here's what you'll learn."),
    cta(button="Register free", say="Register free at the link."),
], ["webinar", "event"])
add("landscape-top-5", "Top 5 countdown", "landscape", "education", "A countdown list for YouTube.", [
    hook("Top 5 *{{topic}}*", "The top five {{topic}}, counted down."),
    point("#5", "Number five", "Number five."), point("#4", "Number four", "Number four."), point("#3", "Number three", "Number three."),
    point("#2", "Number two", "Number two."), point("#1", "Number one", "And number one."),
    cta("Subscribe", "Subscribe for more."),
], ["countdown", "youtube"])
add("landscape-interview", "Interview highlight", "landscape", "story", "Pull quotes from an interview or podcast.", [
    hook("A conversation about *{{topic}}*", "A conversation about {{topic}}."),
    quote("Highlight quote one", "Guest name", "Here's one moment that stood out."),
    quote("Highlight quote two", "Guest name", "And another."),
    cta("Watch the full episode", "Watch the full episode at the link."),
], ["podcast", "interview"])

# =================================================================== CAROUSELS (4:5 slides)
def car(id, name, category, description, slides, tags=()):
    add(id, name, "carousel", category, description, slides, tags)

car("carousel-listicle", "5-point listicle", "education", "Cover, five ideas, CTA.", [
    hook("5 things about *{{topic}}*", sub="Swipe →"),
    *[point(f"0{i}", f"Idea {i}", sub="One or two lines of detail.") for i in range(1, 6)],
    cta(sub="Save this for later"),
], ["listicle"])
car("carousel-how-to", "How-to guide", "education", "A step-by-step guide.", [
    hook("How to *{{topic}}*", sub="A step-by-step guide →"),
    *[point(f"Step {i}", f"Step {i} headline", sub="What to do and why.") for i in range(1, 5)],
    cta("Save the guide", sub="Follow {{handle}} for more"),
], ["how-to", "guide"])
car("carousel-myths", "Myth busting", "education", "Three myths, three facts.", [
    hook("3 myths about *{{topic}}*", sub="Swipe to bust them →"),
    point("Myth 1", "The first myth", sub="The truth in one line."),
    point("Myth 2", "The second myth", sub="The truth in one line."),
    point("Myth 3", "The third myth", sub="The truth in one line."),
    cta("Share with a friend", sub="Who still believes these?"),
], ["myth"])
car("carousel-framework", "Framework", "education", "Teach a simple framework or acronym.", [
    hook("The *3-step framework* for {{topic}}", sub="Swipe →"),
    point("A", "First letter: the idea", sub="What it means."),
    point("B", "Second letter: the idea", sub="What it means."),
    point("C", "Third letter: the idea", sub="What it means."),
    lst("Use it when", ["Situation one", "Situation two", "Situation three"]),
    cta(sub="Save the framework"),
], ["framework"])
car("carousel-checklist", "Checklist", "education", "A practical checklist people save.", [
    hook("The *{{topic}}* checklist", sub="Save this →"),
    lst("Before", ["Check one", "Check two", "Check three"]),
    lst("During", ["Check one", "Check two", "Check three"]),
    lst("After", ["Check one", "Check two", "Check three"]),
    cta("Save the checklist"),
], ["checklist"])
car("carousel-do-dont", "Do's and don'ts", "education", "Contrast good and bad practice.", [
    hook("Do's and don'ts of *{{topic}}*", sub="Swipe →"),
    lst("Do", ["Do this", "Do this", "Do this"]),
    lst("Don't", ["Avoid this", "Avoid this", "Avoid this"]),
    cta(sub="Save for later"),
], ["tips"])
car("carousel-comparison", "This vs that", "education", "Compare two options side by side.", [
    hook("Option A vs *option B*", sub="Which is right for you? →"),
    lst("Option A", ["Pro", "Pro", "Con"]),
    lst("Option B", ["Pro", "Pro", "Con"]),
    point("Verdict", "Choose A if…, B if…", sub="One-line rule of thumb."),
    cta(sub="Follow {{handle}}"),
], ["comparison"])
car("carousel-case-study", "Case study", "social-proof", "A customer story with numbers.", [
    hook("How a customer *doubled results*", sub="The full story →"),
    point("Before", "Where they started", sub="The situation."),
    point("What changed", "What they did", sub="The change."),
    stat("2×", "the result", sub="In 30 days."),
    quote("A line from the customer", "Customer name"),
    cta(),
], ["case-study"])
car("carousel-stats", "Stats that matter", "education", "Three numbers with context.", [
    hook("3 numbers every {{audience}} should know", sub="Swipe →"),
    stat("73%", "first stat", sub="Source and context."),
    stat("2.5×", "second stat", sub="Source and context."),
    stat("48h", "third stat", sub="Source and context."),
    cta(sub="Share this"),
], ["stats"])
car("carousel-quotes", "Quote collection", "inspiration", "A swipeable set of quotes.", [
    hook("Words we live by", sub="Swipe →"),
    quote("Quote one", "Author"), quote("Quote two", "Author"), quote("Quote three", "Author"),
    cta("Which one is yours?"),
], ["quotes"])
car("carousel-timeline", "Timeline / our story", "story", "The brand's story as a timeline.", [
    hook("The story of *{{brand}}*", sub="Swipe through the years →"),
    point("Year 1", "Where it started", sub="A line about the start."),
    point("Year 2", "The first big moment", sub="What happened."),
    point("Today", "Where we are now", sub="What's next."),
    cta("Thank you for being here"),
], ["story", "timeline"])
car("carousel-faq", "FAQ", "education", "Answer the five questions you get most.", [
    hook("Your questions, *answered*", sub="Swipe →"),
    *[point(f"Q{i}", f"Question {i}?", sub="Short answer.") for i in range(1, 5)],
    cta("Ask us anything", sub="Comment your question"),
], ["faq"])
car("carousel-glossary", "Glossary", "education", "Define the terms your audience mixes up.", [
    hook("*{{topic}}* terms, explained", sub="Swipe →"),
    *[point(f"Term {i}", f"Term {i}", sub="Plain-English definition.") for i in range(1, 5)],
    cta(sub="Save for later"),
], ["glossary"])
car("carousel-product-features", "Product features", "product", "Walk through features, one per slide.", [
    hook("Everything {{product}} does", sub="Swipe →"),
    media("Feature one", sub="Why it matters."), media("Feature two", sub="Why it matters."), media("Feature three", sub="Why it matters."),
    cta(button="Shop now"),
], ["product"])
car("carousel-mistakes", "Mistakes to avoid", "education", "Five mistakes and the fix for each.", [
    hook("5 *{{topic}}* mistakes", sub="And how to fix them →"),
    *[point(f"Mistake {i}", f"Mistake {i}", sub="The fix in one line.") for i in range(1, 6)],
    cta(sub="Save this"),
], ["mistakes"])
car("carousel-before-after", "Before / after", "transformation", "A transformation in slides.", [
    hook("The *difference* is real", sub="Swipe →"),
    media("Before"), media("After"),
    lst("What changed", ["Change one", "Change two", "Change three"]),
    cta(),
], ["transformation"])
car("carousel-recap", "Weekly recap", "community", "Round up the week.", [
    hook("This week at *{{brand}}*", sub="Swipe →"),
    point("01", "Highlight one", sub="A line."), point("02", "Highlight two", sub="A line."), point("03", "Highlight three", sub="A line."),
    cta("See you next week"),
], ["recap"])
car("carousel-guide-beginners", "Beginner's guide", "education", "Everything a beginner needs, in order.", [
    hook("A beginner's guide to *{{topic}}*", sub="Start here →"),
    point("Start", "What you need", sub="The basics."), point("Learn", "The first skill", sub="Why it matters."),
    point("Practice", "Your first week", sub="What to do."), point("Next", "Where to go next", sub="Level up."),
    cta(sub="Follow {{handle}} for part 2"),
], ["guide", "beginner"])
car("carousel-launch", "Launch carousel", "launch", "Introduce a new product in slides.", [
    hook("Introducing *{{product}}*", sub="Swipe →"),
    media("{{product}}"),
    lst("What's inside", ["Feature", "Feature", "Feature"]),
    stat("Today", "available now"),
    cta(button="Shop now"),
], ["launch"])
car("carousel-tips-season", "Seasonal tips", "seasonal", "Timely tips for a season or holiday.", [
    hook("Seasonal tips from *{{brand}}*", sub="Swipe →"),
    *[point(f"Tip {i}", f"Seasonal tip {i}", sub="One line.") for i in range(1, 4)],
    cta(sub="Save for later"),
], ["seasonal"])

# =================================================================== POSTS (4:5 single)
def post(id, name, category, description, scene, tags=()):
    add(id, name, "post", category, description, [scene], tags)

post("post-announcement", "Announcement", "announcement", "One bold line for news.", hook("Big news from *{{brand}}*", sub="Details in the caption"), ["news"])
post("post-tip", "Tip of the day", "education", "One useful tip.", point("Tip", "A useful tip about {{topic}}", sub="One line of detail."), ["tip"])
post("post-stat", "Big number", "education", "A single stat that stops the scroll.", stat("73%", "of people get this wrong", sub="Here's how not to →"), ["stat"])
post("post-quote", "Quote", "inspiration", "A quote in brand style.", quote("A line worth sharing", "Author"), ["quote"])
post("post-testimonial", "Testimonial", "social-proof", "A customer review.", quote("A real customer review", "Customer name"), ["review"])
post("post-sale", "Sale", "promo", "Promote an offer.", stat("30% off", "everything this week", sub="Link in bio"), ["sale"])
post("post-product", "Product spotlight", "product", "One product, one line.", media("{{product}}", sub="{{cta}}"), ["product"])
post("post-event", "Event", "event", "Save the date.", hook("Save the date", sub="Date · Place"), ["event"])
post("post-hiring", "We're hiring", "team", "A recruiting post.", hook("We're *hiring*", sub="Role title · link in bio"), ["hiring"])
post("post-question", "Question", "engagement", "Ask your audience something.", hook("What's your *favourite*…?", sub="Tell us in the comments"), ["engagement"])
post("post-milestone", "Milestone", "community", "Celebrate a number.", stat("10K", "thank you", sub="From all of us at {{brand}}"), ["milestone"])

# =================================================================== SQUARE (1:1)
def sq(id, name, category, description, scene, tags=()):
    add(id, name, "square", category, description, [scene], tags)

sq("square-quote", "Quote card", "inspiration", "A classic square quote card.", quote("A line worth sharing", "Author"), ["quote"])
sq("square-review", "Review card", "social-proof", "Five-star review card.", quote("★★★★★ A short review", "Customer name"), ["review"])
sq("square-tip", "Tip card", "education", "A square tip.", point("Tip", "One useful tip", sub="Save for later"), ["tip"])
sq("square-stat", "Stat card", "education", "A square stat.", stat("2×", "faster than the usual way"), ["stat"])
sq("square-announcement", "Announcement card", "announcement", "News in a square.", hook("Coming *soon*", sub="{{brand}}"), ["news"])
sq("square-sale", "Sale card", "promo", "Offer in a square.", stat("20% off", "this weekend only", sub="Link in bio"), ["sale"])
sq("square-question", "This or that", "engagement", "Ask a this-or-that question.", hook("This *or* that?", sub="Comment your pick"), ["engagement"])
sq("square-product", "Product card", "product", "Product photo with one line.", media("{{product}}", sub="{{cta}}"), ["product"])
sq("square-thank-you", "Thank you card", "community", "Say thanks.", hook("Thank *you*", sub="From all of us at {{brand}}"), ["community"])
sq("square-holiday", "Holiday greeting", "seasonal", "A seasonal greeting.", hook("Happy *holidays*", sub="From {{brand}}"), ["holiday"])

# =================================================================== STORIES (9:16 frames)
def story(id, name, category, description, frames, tags=()):
    add(id, name, "story", category, description, frames, tags)

story("story-poll", "Poll setup", "engagement", "Frames that set up a poll sticker.", [hook("Quick question", sub="Tap →"), hook("This *or* that?", sub="Add a poll sticker here")], ["poll"])
story("story-countdown", "Countdown", "promo", "Build up to a launch or sale.", [hook("Something's *coming*", sub="Tap →"), stat("3", "days to go"), cta("Turn on reminders", button="Remind me")], ["countdown"])
story("story-bts", "Behind the scenes", "behind-the-scenes", "Quick BTS frames.", [hook("Today at *{{brand}}*", sub="Tap →"), media("Behind the scenes"), cta("More tomorrow")], ["bts"])
story("story-product-drop", "Product drop", "launch", "Announce a drop in frames.", [hook("New *drop*", sub="Tap →"), media("{{product}}"), cta(button="Shop now")], ["launch"])
story("story-link", "Link in bio", "promo", "Send people to the link.", [hook("New on the blog", sub="Tap →"), point("Read it", "Headline of the post"), cta("Link in bio", button="Read now")], ["traffic"])
story("story-qa", "Q&A", "community", "Collect and answer questions.", [hook("Ask us *anything*", sub="Question sticker here"), point("Q", "Answer to a question")], ["qa"])
story("story-review", "Review highlight", "social-proof", "Share a customer review.", [hook("What you said", sub="Tap →"), quote("A customer review", "Customer"), cta(button="Shop now")], ["review"])
story("story-tips", "3 quick tips", "education", "Three tips in three frames.", [hook("3 quick tips", sub="Tap →"), point("1", "Tip one"), point("2", "Tip two"), point("3", "Tip three"), cta("Save this")], ["tips"])
story("story-event", "Event reminder", "event", "Remind people about an event.", [hook("Today's the day", sub="Tap →"), lst("Details", ["Time", "Place", "What to bring"]), cta(button="Join")], ["event"])
story("story-sale", "Sale stories", "promo", "Push a sale across frames.", [hook("*Sale* starts now"), stat("30%", "off everything"), cta(button="Shop now")], ["sale"])

# =================================================================== EXTERNAL STARTERS
EXT = [
    ("remotion-hello-world", "Remotion Hello World", "remotion", "The official minimal Remotion starter.", "https://github.com/remotion-dev/template-helloworld"),
    ("remotion-tiktok", "Remotion TikTok captions", "remotion", "Official template with animated, word-by-word TikTok-style captions from a video.", "https://github.com/remotion-dev/template-tiktok"),
    ("remotion-audiogram", "Remotion Audiogram", "remotion", "Turn podcast audio into a waveform video with captions.", "https://github.com/remotion-dev/template-audiogram"),
    ("remotion-music-visualization", "Remotion Music visualization", "remotion", "Audio-reactive visuals for music.", "https://github.com/remotion-dev/template-music-visualization"),
    ("remotion-three", "Remotion Three.js", "remotion", "3D scenes with React Three Fiber.", "https://github.com/remotion-dev/template-three"),
    ("remotion-still", "Remotion Still images", "remotion", "Generate images (social cards, thumbnails) with Remotion.", "https://github.com/remotion-dev/template-still"),
    ("remotion-skia", "Remotion Skia", "remotion", "2D graphics with React Native Skia.", "https://github.com/remotion-dev/template-skia"),
    ("remotion-overlay", "Remotion Overlay", "remotion", "Transparent overlays for editors like Premiere and Resolve.", "https://github.com/remotion-dev/template-overlay"),
    ("remotion-code-hike", "Remotion Code Hike", "remotion", "Animated code walkthroughs.", "https://github.com/remotion-dev/template-code-hike"),
    ("remotion-prompt-to-video", "Remotion Prompt to video", "remotion", "Official template that turns a text prompt into a narrated video with AI-generated images and voice.", "https://github.com/remotion-dev/template-prompt-to-video"),
    ("hyperframes-warm-grain", "HyperFrames Warm grain", "hyperframes", "Official HyperFrames example: warm, film-grain look. Create with: npx hyperframes init --example warm-grain", "https://hyperframes.heygen.com"),
    ("hyperframes-swiss-grid", "HyperFrames Swiss grid", "hyperframes", "Official HyperFrames example: Swiss typographic grid. Create with: npx hyperframes init --example swiss-grid", "https://hyperframes.heygen.com"),
    ("hyperframes-registry", "HyperFrames registry blocks", "hyperframes", "Ready-made blocks and components installable into any HyperFrames project with npx hyperframes add.", "https://github.com/heygen-com/hyperframes/tree/main/registry"),
]

if __name__ == "__main__":
    out = os.path.join(ROOT, "templates")
    seen = set()
    for t in T:
        assert t["id"] not in seen, t["id"]
        seen.add(t["id"])
        d = os.path.join(out, t["format"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, f"{t['id']}.json"), "w") as f:
            json.dump({"kind": "studio", **t}, f, indent=2, ensure_ascii=False)
            f.write("\n")
    d = os.path.join(out, "external")
    os.makedirs(d, exist_ok=True)
    for id, name, engine, desc, url in EXT:
        assert id not in seen, id
        seen.add(id)
        with open(os.path.join(d, f"{id}.json"), "w") as f:
            json.dump({"kind": "external", "id": id, "name": name, "engine": engine, "category": "starter", "description": desc, "url": url, "tags": [engine, "starter"]}, f, indent=2)
            f.write("\n")
    print(f"wrote {len(T)} studio templates + {len(EXT)} external starters")
