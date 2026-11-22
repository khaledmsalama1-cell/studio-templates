# studio-templates

The template registry for [Studio](https://github.com/khaledmsalama1-cell/studio): 110 templates — 97 ready-to-use studio templates and 13 external starters — plus 100 brand starters.

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

### Reels (9:16 video) — 30

| Template | What it's for | Category | Scenes |
|---|---|---|---|
| [Big announcement](templates/reel/reel-announcement.json) | Share news with a reveal. | announcement | 4 |
| [Before and after](templates/reel/reel-before-after.json) | Show the change your product makes. | transformation | 5 |
| [Behind the scenes](templates/reel/reel-bts.json) | Show how it's made; builds trust and personality. | behind-the-scenes | 5 |
| [Customer case study](templates/reel/reel-case-study.json) | A real result with numbers. | social-proof | 5 |
| [Challenge or trend](templates/reel/reel-challenge.json) | Invite your audience into a challenge. | engagement | 3 |
| [Us vs them](templates/reel/reel-comparison.json) | Compare the usual option with yours, honestly. | promo | 4 |
| [Sale countdown](templates/reel/reel-countdown-sale.json) | Urgency for a sale or limited offer. | promo | 4 |
| [A day in the life](templates/reel/reel-day-in-life.json) | Morning to night at the brand, in quick cuts. | behind-the-scenes | 5 |
| [Event promo](templates/reel/reel-event.json) | Promote an event, launch party or live session. | event | 3 |
| [Answering an FAQ](templates/reel/reel-faq.json) | Turn a common question into content. | education | 4 |
| [Founder story](templates/reel/reel-founder-story.json) | Why the brand exists, told in 30 seconds. | story | 5 |
| [Giveaway](templates/reel/reel-giveaway.json) | Run a giveaway with simple steps. | promo | 4 |
| [We're hiring](templates/reel/reel-hiring.json) | Recruit with personality. | team | 4 |
| [Hot take](templates/reel/reel-hot-take.json) | A strong opinion that sparks comments. | opinion | 4 |
| [How to in 4 steps](templates/reel/reel-how-to.json) | A step-by-step tutorial with numbered scenes. | education | 6 |
| [Ingredient spotlight](templates/reel/reel-ingredient.json) | Zoom in on one ingredient, material or feature. | product | 4 |
| [3 things listicle](templates/reel/reel-listicle-3.json) | Three quick points with a strong hook. The most reliable short-form format. | education | 5 |
| [5 quick tips](templates/reel/reel-listicle-5.json) | Five fast tips for a high-retention 30-second reel. | education | 7 |
| [Milestone thank-you](templates/reel/reel-milestone.json) | Celebrate a milestone with your audience. | community | 4 |
| [Mistakes to avoid](templates/reel/reel-mistakes.json) | Warn people off three common mistakes. | education | 5 |
| [Myth vs fact](templates/reel/reel-myth-fact.json) | Name a common belief, bust it, give the right move. | education | 5 |
| [Problem → solution](templates/reel/reel-pas.json) | Problem, agitate, solve: the classic ad structure. | promo | 5 |
| [Product demo](templates/reel/reel-product-demo.json) | Show the product doing its job in three beats. | product | 5 |
| [Product launch](templates/reel/reel-product-launch.json) | Announce something new with build-up and a clear CTA. | launch | 5 |
| [Answer in one line](templates/reel/reel-question.json) | A question hook answered fast. | engagement | 3 |
| [Quote of the day](templates/reel/reel-quote.json) | A short, shareable quote with voice. | inspiration | 2 |
| [Seasonal moment](templates/reel/reel-seasonal.json) | Tie the brand to a holiday or season. | seasonal | 4 |
| [Surprising stat](templates/reel/reel-stat-shock.json) | Lead with a number that stops the scroll. | education | 4 |
| [Customer testimonial](templates/reel/reel-testimonial.json) | Lead with a real customer's words. | social-proof | 4 |
| [POV tutorial](templates/reel/reel-tutorial-pov.json) | First-person POV tutorial. | education | 5 |

### Product promos (9:16 video) — 8

| Template | What it's for | Category | Scenes |
|---|---|---|---|
| [3 reasons to try](templates/promo/promo-3-reasons.json) | Three reasons, fast. | promo | 5 |
| [Bundle promo](templates/promo/promo-bundle.json) | Sell a bundle with value math. | promo | 4 |
| [Classic product promo](templates/promo/promo-classic.json) | Hook, product, benefits, proof, CTA. | promo | 5 |
| [Gift idea](templates/promo/promo-gift.json) | Position the product as a gift. | seasonal | 4 |
| [New variant](templates/promo/promo-new-flavor.json) | Launch a new flavour, colour or version. | launch | 4 |
| [Limited offer](templates/promo/promo-offer.json) | A direct-response promo for an offer. | promo | 4 |
| [Back in stock](templates/promo/promo-restock.json) | Announce a restock. | launch | 4 |
| [UGC-style ad](templates/promo/promo-ugc-style.json) | Feels like a customer filming it themselves. | promo | 4 |

### Landscape video (16:9) — 8

| Template | What it's for | Category | Scenes |
|---|---|---|---|
| [Case study](templates/landscape/landscape-case-study.json) | A results story for B2B or LinkedIn. | social-proof | 5 |
| [Explainer](templates/landscape/landscape-explainer.json) | A 16:9 explainer for YouTube or LinkedIn. | education | 4 |
| [Interview highlight](templates/landscape/landscape-interview.json) | Pull quotes from an interview or podcast. | story | 4 |
| [Product overview](templates/landscape/landscape-product-overview.json) | A clean overview of what the product does. | product | 5 |
| [Top 5 countdown](templates/landscape/landscape-top-5.json) | A countdown list for YouTube. | education | 7 |
| [Tutorial](templates/landscape/landscape-tutorial.json) | A longer step-by-step tutorial. | education | 6 |
| [Company update](templates/landscape/landscape-update.json) | A short update for your audience or team. | announcement | 3 |
| [Webinar promo](templates/landscape/landscape-webinar.json) | Promote a webinar or live session. | event | 3 |

### Carousels (4:5 slides) — 20

| Template | What it's for | Category | Scenes |
|---|---|---|---|
| [Before / after](templates/carousel/carousel-before-after.json) | A transformation in slides. | transformation | 5 |
| [Case study](templates/carousel/carousel-case-study.json) | A customer story with numbers. | social-proof | 6 |
| [Checklist](templates/carousel/carousel-checklist.json) | A practical checklist people save. | education | 5 |
| [This vs that](templates/carousel/carousel-comparison.json) | Compare two options side by side. | education | 5 |
| [Do's and don'ts](templates/carousel/carousel-do-dont.json) | Contrast good and bad practice. | education | 4 |
| [FAQ](templates/carousel/carousel-faq.json) | Answer the five questions you get most. | education | 6 |
| [Framework](templates/carousel/carousel-framework.json) | Teach a simple framework or acronym. | education | 6 |
| [Glossary](templates/carousel/carousel-glossary.json) | Define the terms your audience mixes up. | education | 6 |
| [Beginner's guide](templates/carousel/carousel-guide-beginners.json) | Everything a beginner needs, in order. | education | 6 |
| [How-to guide](templates/carousel/carousel-how-to.json) | A step-by-step guide. | education | 6 |
| [Launch carousel](templates/carousel/carousel-launch.json) | Introduce a new product in slides. | launch | 5 |
| [5-point listicle](templates/carousel/carousel-listicle.json) | Cover, five ideas, CTA. | education | 7 |
| [Mistakes to avoid](templates/carousel/carousel-mistakes.json) | Five mistakes and the fix for each. | education | 7 |
| [Myth busting](templates/carousel/carousel-myths.json) | Three myths, three facts. | education | 5 |
| [Product features](templates/carousel/carousel-product-features.json) | Walk through features, one per slide. | product | 5 |
| [Quote collection](templates/carousel/carousel-quotes.json) | A swipeable set of quotes. | inspiration | 5 |
| [Weekly recap](templates/carousel/carousel-recap.json) | Round up the week. | community | 5 |
| [Stats that matter](templates/carousel/carousel-stats.json) | Three numbers with context. | education | 5 |
| [Timeline / our story](templates/carousel/carousel-timeline.json) | The brand's story as a timeline. | story | 5 |
| [Seasonal tips](templates/carousel/carousel-tips-season.json) | Timely tips for a season or holiday. | seasonal | 5 |

### Feed posts (4:5) — 11

| Template | What it's for | Category | Scenes |
|---|---|---|---|
| [Announcement](templates/post/post-announcement.json) | One bold line for news. | announcement | 1 |
| [Event](templates/post/post-event.json) | Save the date. | event | 1 |
| [We're hiring](templates/post/post-hiring.json) | A recruiting post. | team | 1 |
| [Milestone](templates/post/post-milestone.json) | Celebrate a number. | community | 1 |
| [Product spotlight](templates/post/post-product.json) | One product, one line. | product | 1 |
| [Question](templates/post/post-question.json) | Ask your audience something. | engagement | 1 |
| [Quote](templates/post/post-quote.json) | A quote in brand style. | inspiration | 1 |
| [Sale](templates/post/post-sale.json) | Promote an offer. | promo | 1 |
| [Big number](templates/post/post-stat.json) | A single stat that stops the scroll. | education | 1 |
| [Testimonial](templates/post/post-testimonial.json) | A customer review. | social-proof | 1 |
| [Tip of the day](templates/post/post-tip.json) | One useful tip. | education | 1 |

### Square posts (1:1) — 10

| Template | What it's for | Category | Scenes |
|---|---|---|---|
| [Announcement card](templates/square/square-announcement.json) | News in a square. | announcement | 1 |
| [Holiday greeting](templates/square/square-holiday.json) | A seasonal greeting. | seasonal | 1 |
| [Product card](templates/square/square-product.json) | Product photo with one line. | product | 1 |
| [This or that](templates/square/square-question.json) | Ask a this-or-that question. | engagement | 1 |
| [Quote card](templates/square/square-quote.json) | A classic square quote card. | inspiration | 1 |
| [Review card](templates/square/square-review.json) | Five-star review card. | social-proof | 1 |
| [Sale card](templates/square/square-sale.json) | Offer in a square. | promo | 1 |
| [Stat card](templates/square/square-stat.json) | A square stat. | education | 1 |
| [Thank you card](templates/square/square-thank-you.json) | Say thanks. | community | 1 |
| [Tip card](templates/square/square-tip.json) | A square tip. | education | 1 |

### Stories (9:16 frames) — 10

| Template | What it's for | Category | Scenes |
|---|---|---|---|
| [Behind the scenes](templates/story/story-bts.json) | Quick BTS frames. | behind-the-scenes | 3 |
| [Countdown](templates/story/story-countdown.json) | Build up to a launch or sale. | promo | 3 |
| [Event reminder](templates/story/story-event.json) | Remind people about an event. | event | 3 |
| [Link in bio](templates/story/story-link.json) | Send people to the link. | promo | 3 |
| [Poll setup](templates/story/story-poll.json) | Frames that set up a poll sticker. | engagement | 2 |
| [Product drop](templates/story/story-product-drop.json) | Announce a drop in frames. | launch | 3 |
| [Q&A](templates/story/story-qa.json) | Collect and answer questions. | community | 2 |
| [Review highlight](templates/story/story-review.json) | Share a customer review. | social-proof | 3 |
| [Sale stories](templates/story/story-sale.json) | Push a sale across frames. | promo | 3 |
| [3 quick tips](templates/story/story-tips.json) | Three tips in three frames. | education | 5 |

### External starters — 13

| Starter | Engine | What it is |
|---|---|---|
| [HyperFrames registry blocks](https://github.com/heygen-com/hyperframes/tree/main/registry) | hyperframes | Ready-made blocks and components installable into any HyperFrames project with npx hyperframes add. |
| [HyperFrames Swiss grid](https://hyperframes.heygen.com) | hyperframes | Official HyperFrames example: Swiss typographic grid. Create with: npx hyperframes init --example swiss-grid |
| [HyperFrames Warm grain](https://hyperframes.heygen.com) | hyperframes | Official HyperFrames example: warm, film-grain look. Create with: npx hyperframes init --example warm-grain |
| [Remotion Audiogram](https://github.com/remotion-dev/template-audiogram) | remotion | Turn podcast audio into a waveform video with captions. |
| [Remotion Code Hike](https://github.com/remotion-dev/template-code-hike) | remotion | Animated code walkthroughs. |
| [Remotion Hello World](https://github.com/remotion-dev/template-helloworld) | remotion | The official minimal Remotion starter. |
| [Remotion Music visualization](https://github.com/remotion-dev/template-music-visualization) | remotion | Audio-reactive visuals for music. |
| [Remotion Overlay](https://github.com/remotion-dev/template-overlay) | remotion | Transparent overlays for editors like Premiere and Resolve. |
| [Remotion Prompt to video](https://github.com/remotion-dev/template-prompt-to-video) | remotion | Official template that turns a text prompt into a narrated video with AI-generated images and voice. |
| [Remotion Skia](https://github.com/remotion-dev/template-skia) | remotion | 2D graphics with React Native Skia. |
| [Remotion Still images](https://github.com/remotion-dev/template-still) | remotion | Generate images (social cards, thumbnails) with Remotion. |
| [Remotion Three.js](https://github.com/remotion-dev/template-three) | remotion | 3D scenes with React Three Fiber. |
| [Remotion TikTok captions](https://github.com/remotion-dev/template-tiktok) | remotion | Official template with animated, word-by-word TikTok-style captions from a video. |

## Brand starters — 100

Fictional brands with complete kits (positioning, audience, voice, palette, fonts, logo, products, content pillars). In the Studio: **Brands → Add a brand → Start from a brand template**. Any resemblance to a real business is unintended.

### Sustainable goods

| Brand | Tagline | Fonts |
|---|---|---|
| [Bare Necessities](brands/bare-necessities.json) | Plastic-free bathroom basics. | Fraunces / Mulish |
| [Loop Goods](brands/loop-goods.json) | Reusable everything. | Fraunces / Mulish |
| [Refill Roots](brands/refill-roots.json) | Refill shop for the whole home. | Fraunces / Mulish |
| [Second Life Co.](brands/second-life-co.json) | Pre-loved furniture, restored. | Fraunces / Mulish |
| [Sun Cycle](brands/sun-cycle.json) | Solar gadgets for everyday life. | Fraunces / Mulish |

### Coffee & cafés

| Brand | Tagline | Fonts |
|---|---|---|
| [Bean & Bloom](brands/bean-and-bloom.json) | A café with a flower shop inside. | Fraunces / DM Sans |
| [Copper Kettle Roasters](brands/copper-kettle.json) | Roasted on Tuesday, in your cup by Friday. | Fraunces / DM Sans |
| [Crema Corner](brands/crema-corner.json) | The neighbourhood café that knows your order. | Fraunces / DM Sans |
| [Dawn Patrol Coffee](brands/dawn-patrol-coffee.json) | Coffee for people who are up before the sun. | Fraunces / DM Sans |
| [North Pour](brands/north-pour.json) | Light roasts for slow mornings. | Fraunces / DM Sans |

### Skincare & beauty

| Brand | Tagline | Fonts |
|---|---|---|
| [Bloom Ritual](brands/bloom-ritual.json) | Botanical body care for slow evenings. | Cormorant Garamond / Lato |
| [Dew Theory](brands/dew-theory.json) | Hydration, explained. | Cormorant Garamond / Lato |
| [Lumen Skin](brands/lumen-skin.json) | Gentle actives for sensitive skin. | Cormorant Garamond / Lato |
| [Oat & Ash](brands/oat-and-ash.json) | Three-step skincare. Nothing extra. | Cormorant Garamond / Lato |
| [Velvet Clay](brands/velvet-clay.json) | Clay masks with a softer touch. | Cormorant Garamond / Lato |

### Yoga & wellness

| Brand | Tagline | Fonts |
|---|---|---|
| [Breathe Collective](brands/breathe-collective.json) | Breathwork and yoga retreats. | Lora / Nunito Sans |
| [Lotus & Light](brands/lotus-and-light.json) | Yoga for every body. | Lora / Nunito Sans |
| [Mat & Mind](brands/mat-and-mind.json) | Movement and mindfulness, 30 minutes a day. | Lora / Nunito Sans |
| [Still Water Yoga](brands/still-water-yoga.json) | A quiet room in a busy city. | Lora / Nunito Sans |
| [Sun Salute Studio](brands/sunsalute-studio.json) | Morning flows to start the day right. | Lora / Nunito Sans |

### Real estate

| Brand | Tagline | Fonts |
|---|---|---|
| [Brick & Beam](brands/brick-and-beam.json) | Character homes in old neighbourhoods. | Marcellus / Manrope |
| [Coastline Living](brands/coastline-living.json) | Homes by the water. | Marcellus / Manrope |
| [Keystone Homes](brands/keystone-homes.json) | Your first home, step by step. | Marcellus / Manrope |
| [Open Door Realty](brands/open-door-realty.json) | Homes with room to grow. | Marcellus / Manrope |
| [Urban Nest](brands/urban-nest.json) | City apartments, honestly described. | Marcellus / Manrope |

### Clinics & dental

| Brand | Tagline | Fonts |
|---|---|---|
| [Bright Dental Care](brands/bright-dental.json) | Family dentistry, Saturdays too. | Outfit / Outfit |
| [Calm Cove Clinic](brands/calm-cove-clinic.json) | Skin and laser clinic, explained simply. | Outfit / Outfit |
| [Clearview Optics](brands/clearview-optics.json) | Eye tests and frames you'll love. | Outfit / Outfit |
| [Gentle Hands Physio](brands/gentle-hands-clinic.json) | Physiotherapy that gets you moving. | Outfit / Outfit |
| [Smile Studio Dental](brands/smile-studio.json) | Check-ups without the dread. | Outfit / Outfit |

### Kids & education

| Brand | Tagline | Fonts |
|---|---|---|
| [Bright Sparks Tutoring](brands/bright-sparks.json) | Tutoring that builds confidence. | Baloo 2 / Nunito |
| [Little Makers](brands/little-makers.json) | Craft and science classes for ages 5–10. | Baloo 2 / Nunito |
| [Play Lab](brands/play-lab.json) | Holiday camps where kids build things. | Baloo 2 / Nunito |
| [Story Sprouts](brands/story-sprouts.json) | Reading adventures for early readers. | Baloo 2 / Nunito |
| [Tiny Coders](brands/tiny-coders.json) | Kids learn to code by making games. | Baloo 2 / Nunito |

### Software & SaaS

| Brand | Tagline | Fonts |
|---|---|---|
| [Brightdesk](brands/brightdesk.json) | Customer support that feels personal. | Inter Tight / Inter |
| [Formwell](brands/formwell.json) | Forms people actually finish. | Inter Tight / Inter |
| [Ledgerly](brands/ledgerly.json) | Invoices and expenses without the spreadsheet. | Inter Tight / Inter |
| [Signalbox](brands/signalbox.json) | Know when something breaks before customers do. | Inter Tight / Inter |
| [Taskflow](brands/taskflow.json) | Plan the week in ten minutes. | Inter Tight / Inter |

### Bakeries

| Brand | Tagline | Fonts |
|---|---|---|
| [Butter Lane Bakery](brands/butter-lane.json) | Croissants with 81 layers. We counted. | Young Serif / Karla |
| [Knead & Co.](brands/knead-and-co.json) | Real bread for real sandwiches. | Young Serif / Karla |
| [The Little Oven](brands/little-oven.json) | A tiny bakery with big birthday cakes. | Young Serif / Karla |
| [Rise & Crumb](brands/rise-and-crumb.json) | Sourdough that takes two days. Worth it. | Young Serif / Karla |
| [Sugar & Salt Patisserie](brands/sugar-and-salt.json) | French pastry, made every morning. | Young Serif / Karla |

### Bookshops

| Brand | Tagline | Fonts |
|---|---|---|
| [Chapter & Verse](brands/chapter-and-verse.json) | Poetry and fiction, picked by people. | Libre Caslon Text / Work Sans |
| [Dog-Eared Books](brands/dog-eared-books.json) | Well-loved books, ready for you. | Libre Caslon Text / Work Sans |
| [Ink & Index](brands/ink-and-index.json) | Non-fiction for curious minds. | Libre Caslon Text / Work Sans |
| [Paper Lantern Books](brands/paper-lantern-books.json) | Translated fiction from around the world. | Libre Caslon Text / Work Sans |
| [The Reading Nook](brands/the-reading-nook.json) | Kids' books and story time. | Libre Caslon Text / Work Sans |

### Streetwear & sneakers

| Brand | Tagline | Fonts |
|---|---|---|
| [Concrete Kids](brands/concrete-kids.json) | Streetwear from the skatepark up. | Bebas Neue / Barlow |
| [Lowkey Supply](brands/lowkey-supply.json) | Quiet logos, loud quality. | Bebas Neue / Barlow |
| [Neon Alley](brands/neon-alley.json) | Night-time graphics, daytime fits. | Bebas Neue / Barlow |
| [Rooftop Crew](brands/rooftop-crew.json) | Made in the city, worn on the roof. | Bebas Neue / Barlow |
| [Sole District](brands/sole-district.json) | Rare sneakers, verified. | Bebas Neue / Barlow |

### Jewellery

| Brand | Tagline | Fonts |
|---|---|---|
| [Ember & Gold](brands/ember-and-gold.json) | Bold pieces for bold days. | Cormorant Garamond / Work Sans |
| [Gilded Thread](brands/gilded-thread.json) | Fine gold for everyday wear. | Cormorant Garamond / Work Sans |
| [Moonstone Atelier](brands/moonstone-atelier.json) | Stones with stories. | Cormorant Garamond / Work Sans |
| [Salt & Silver](brands/salt-and-silver.json) | Ocean-inspired silver, made by hand. | Cormorant Garamond / Work Sans |
| [Tiny Heirloom](brands/tiny-heirloom.json) | Personalised pieces to pass down. | Cormorant Garamond / Work Sans |

### Restaurants

| Brand | Tagline | Fonts |
|---|---|---|
| [Ember Table](brands/ember-table.json) | Everything on the menu meets the fire. | DM Serif Display / DM Sans |
| [Green Bowl Kitchen](brands/green-bowl.json) | Bowls that keep you going till dinner. | DM Serif Display / DM Sans |
| [Nonna Rosa](brands/nonna-rosa.json) | Pasta rolled by hand, every afternoon. | DM Serif Display / DM Sans |
| [Saffron Street](brands/saffron-street.json) | Street food from Mumbai, cooked like home. | DM Serif Display / DM Sans |
| [Tide & Thyme](brands/tide-and-thyme.json) | Seafood from the morning catch. | DM Serif Display / DM Sans |

### Pet care

| Brand | Tagline | Fonts |
|---|---|---|
| [Fetch & Feast](brands/fetch-and-feast.json) | Fresh dog food, delivered. | Fredoka / Nunito |
| [Happy Paws](brands/happy-paws.json) | Treats dogs go wild for, ingredients you'll recognise. | Fredoka / Nunito |
| [Tailwind Pet Supply](brands/tailwind-pets.json) | Gear for adventurous dogs. | Fredoka / Nunito |
| [The Good Groomer](brands/the-good-groomer.json) | Calm grooming for nervous dogs. | Fredoka / Nunito |
| [Whisker & Co.](brands/whisker-and-co.json) | Everything for indoor cats. | Fredoka / Nunito |

### Photography & studios

| Brand | Tagline | Fonts |
|---|---|---|
| [Film & Flower](brands/film-and-flower.json) | Film photography for couples. | Italiana / Jost |
| [Frame & Field](brands/frame-and-field.json) | Outdoor family portraits. | Italiana / Jost |
| [Golden Hour Studio](brands/golden-hour-studio.json) | Wedding photos that feel like you. | Italiana / Jost |
| [Headshot House](brands/headshot-house.json) | Headshots in 20 minutes. | Italiana / Jost |
| [Still Life Co.](brands/still-life-co.json) | Product photography for small brands. | Italiana / Jost |

### Fashion boutiques

| Brand | Tagline | Fonts |
|---|---|---|
| [Fold Boutique](brands/fold-boutique.json) | Curated pieces from independent designers. | Playfair Display / Inter |
| [Maison Verde](brands/maison-verde.json) | Linen, made slowly. | Playfair Display / Inter |
| [Petal & Hem](brands/petal-and-hem.json) | Dresses for every celebration. | Playfair Display / Inter |
| [Sunday Tailor](brands/sunday-tailor.json) | Made-to-measure without the fuss. | Playfair Display / Inter |
| [Thread & Row](brands/thread-and-row.json) | Wardrobe staples that last ten years. | Playfair Display / Inter |

### Gyms & fitness

| Brand | Tagline | Fonts |
|---|---|---|
| [Forge Strength Club](brands/forge-strength.json) | Lift heavy, leave strong. | Archivo Black / Archivo |
| [Iron Tide Gym](brands/iron-tide.json) | Strength training for real life. | Archivo Black / Archivo |
| [Kettlebell District](brands/kettlebell-district.json) | Kettlebells only. Results always. | Archivo Black / Archivo |
| [Pulse Lab](brands/pulse-lab.json) | 45-minute classes that count. | Archivo Black / Archivo |
| [Stride Run Club](brands/stride-run-club.json) | Run together, get faster. | Archivo Black / Archivo |

### Money & fintech

| Brand | Tagline | Fonts |
|---|---|---|
| [Future Fund](brands/future-fund.json) | Investing for beginners, in plain English. | Sora / Nunito Sans |
| [Harborline](brands/harborline.json) | A bank that explains itself. | Sora / Nunito Sans |
| [Penny Jar](brands/penny-jar.json) | Round up, save up. | Sora / Nunito Sans |
| [Splitly](brands/splitly.json) | Split bills without the awkward chat. | Sora / Nunito Sans |
| [Stackwise](brands/stackwise.json) | Budgeting for people who hate budgeting. | Sora / Nunito Sans |

### Plant shops

| Brand | Tagline | Fonts |
|---|---|---|
| [Greenhouse Nine](brands/greenhouse-nine.json) | Rare plants from our own greenhouse. | Gloock / Figtree |
| [Leaf & Light](brands/leaf-and-light.json) | Plants matched to your window. | Gloock / Figtree |
| [Pothos Place](brands/pothos-place.json) | Hard-to-kill plants for new plant parents. | Gloock / Figtree |
| [Terra & Twig](brands/terra-and-twig.json) | Plants, pots and good soil. | Gloock / Figtree |
| [The Fern Room](brands/the-fern-room.json) | A shop full of ferns, and help. | Gloock / Figtree |

### Travel & tours

| Brand | Tagline | Fonts |
|---|---|---|
| [Island Hopper](brands/island-hopper.json) | Island trips, sorted. | Syne / Manrope |
| [Local Lens Tours](brands/local-lens-tours.json) | City tours led by locals. | Syne / Manrope |
| [Passport Club](brands/passport-club.json) | Weekend city breaks, planned for you. | Syne / Manrope |
| [Slow Roads](brands/slow-roads.json) | Road trips with the good stops marked. | Syne / Manrope |
| [Wander Wild Tours](brands/wander-wild.json) | Small-group trips off the beaten path. | Syne / Manrope |
