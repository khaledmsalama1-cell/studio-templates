#!/usr/bin/env python3
"""Seed 100 fictional brand starters (any resemblance to a real business is unintended) into brands/<id>.json for the Studio.

Every brand is invented. Palettes are built from a hue per brand and nudged until text is readable:
ink on background and secondary on primary reach 4.5:1, accent on background reaches 3:1.
"""
import colorsys, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- colour
def hx(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360, l, s)
    return "#%02X%02X%02X" % (round(r * 255), round(g * 255), round(b * 255))

def lum(c):
    v = [int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    v = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in v]
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]

def ratio(a, b):
    x, y = sorted([lum(a), lum(b)], reverse=True)
    return (x + 0.05) / (y + 0.05)

def palette(h, accent_h, style):
    """style: dark (deep primary), bright (saturated primary), light (soft primary, dark text on it)"""
    bg = hx(h, 0.30, 0.97)
    ink = hx(h, 0.35, 0.10)
    muted = hx(h, 0.10, 0.42)
    if style == "dark":
        primary, secondary = hx(h, 0.45, 0.16), hx(h, 0.35, 0.94)
    elif style == "bright":
        primary, secondary = hx(h, 0.70, 0.36), hx(h, 0.25, 0.97)
    else:
        primary, secondary = hx(h, 0.45, 0.86), hx(h, 0.45, 0.14)
    # Nudge until readable
    l = 0.36
    while style == "bright" and ratio(primary, secondary) < 4.5 and l > 0.12:
        l -= 0.02
        primary = hx(h, 0.70, l)
    al = 0.50
    accent = hx(accent_h, 0.75, al)
    while ratio(accent, bg) < 3.0 and al > 0.2:
        al -= 0.02
        accent = hx(accent_h, 0.75, al)
    ml = 0.42
    while ratio(muted, bg) < 4.5 and ml > 0.1:
        ml -= 0.02
        muted = hx(h, 0.10, ml)
    return {"primary": primary, "secondary": secondary, "accent": accent, "background": bg, "ink": ink, "muted": muted}

# ---------------------------------------------------------------- logo
def logo_svg(name, c, shape):
    initials = "".join(w[0] for w in re.findall(r"[A-Za-z]+", name)[:2]).upper()
    shapes = {
        "circle": f'<circle cx="100" cy="100" r="92" fill="{c["primary"]}"/>',
        "square": f'<rect x="8" y="8" width="184" height="184" rx="44" fill="{c["primary"]}"/>',
        "arch": f'<path d="M8 192V100a92 92 0 0 1 184 0v92z" fill="{c["primary"]}"/>',
        "diamond": f'<rect x="38" y="38" width="124" height="124" rx="20" transform="rotate(45 100 100)" fill="{c["primary"]}"/>',
        "hex": f'<path d="M100 8l80 46v92l-80 46-80-46V54z" fill="{c["primary"]}"/>',
    }
    dot = f'<circle cx="156" cy="44" r="16" fill="{c["accent"]}"/>' if shape in ("square", "circle") else ""
    size = 84 if len(initials) == 1 else 70
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">{shapes[shape]}{dot}'
            f'<text x="100" y="{100 + size * 0.35:.0f}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" '
            f'font-weight="700" font-size="{size}" fill="{c["secondary"]}">{initials}</text></svg>')

# ---------------------------------------------------------------- industries
# name, display font, body font, energy, persona, pains, desires, pillars, ctas, tone, do, dont, use, avoid, imagery, music, voice
IND = {
    "coffee": dict(label="Coffee & cafés", fonts=("Fraunces", "DM Sans"), energy="calm", persona="The morning ritualist",
        pains=["Bitter, stale coffee", "Rushed mornings"], desires=["A café-quality cup at home", "A small daily pleasure"],
        pillars=[("Brew better", "Quick tips that make coffee taste better"), ("From the roaster", "Sourcing and roasting, behind the scenes"), ("Regulars", "Customers and their rituals")],
        ctas=["Order fresh beans", "Visit the café", "Save this for tomorrow's brew"], tone=["warm", "unhurried", "knowledgeable"],
        do=["Use sensory words", "Explain one idea at a time"], dont=["Coffee snobbery", "Hype"], use=["fresh", "roast", "brew"], avoid=["artisanal", "elevate"],
        imagery="Morning light, hands and steam, warm browns", music="Lo-fi acoustic, 80–90 BPM", voice="Friendly barista, calm, 30s"),
    "bakery": dict(label="Bakeries", fonts=("Young Serif", "Karla"), energy="calm", persona="The weekend treat-seeker",
        pains=["Supermarket bread that tastes of nothing", "No time to bake"], desires=["Real bread and pastries", "Something to share"],
        pillars=[("Fresh today", "What came out of the oven"), ("How it's made", "Dough, timing and craft"), ("Celebrations", "Cakes and orders for big days")],
        ctas=["Pre-order for the weekend", "Visit us", "Order a cake"], tone=["cosy", "generous", "proud of the craft"],
        do=["Talk about texture and smell", "Name the baker"], dont=["Diet talk", "Over-the-top claims"], use=["fresh", "slow-proved", "butter"], avoid=["guilt-free", "artisan-crafted"],
        imagery="Flour, crusts, golden light, close-ups", music="Light jazz piano", voice="Warm, smiling, unhurried"),
    "restaurant": dict(label="Restaurants", fonts=("DM Serif Display", "DM Sans"), energy="medium", persona="The local food lover",
        pains=["Same old places", "Disappointing meals out"], desires=["A place worth coming back to", "Something new to try"],
        pillars=[("On the menu", "Dishes and what's in season"), ("In the kitchen", "Chefs and process"), ("Tables", "Guests, events and moments")],
        ctas=["Book a table", "See the menu", "Order for delivery"], tone=["welcoming", "lively", "confident"],
        do=["Show the food close up", "Mention what's seasonal"], dont=["Long ingredient lists", "Exclamation marks"], use=["seasonal", "fresh", "table"], avoid=["foodie", "mouth-watering"],
        imagery="Overhead plates, flame, busy pass, candlelight", music="Upbeat soul or bossa nova", voice="Host at the door: warm, quick, sure"),
    "skincare": dict(label="Skincare & beauty", fonts=("Cormorant Garamond", "Lato"), energy="calm", persona="The thoughtful skincare buyer",
        pains=["Products that irritate", "Confusing routines"], desires=["Calm, healthy skin", "A routine that's simple"],
        pillars=[("Routine", "How to use it, step by step"), ("Ingredients", "What's inside and why"), ("Real skin", "Customer results, unfiltered")],
        ctas=["Find your routine", "Shop the set", "Take the skin quiz"], tone=["gentle", "clear", "reassuring"],
        do=["Explain ingredients simply", "Show real skin"], dont=["Medical claims", "Before/after exaggeration"], use=["gentle", "barrier", "routine"], avoid=["flawless", "miracle"],
        imagery="Soft daylight, textures, clean surfaces, real skin", music="Soft ambient, slow", voice="Calm, close, reassuring"),
    "fitness": dict(label="Gyms & fitness", fonts=("Archivo Black", "Archivo"), energy="high", persona="The busy person getting back in shape",
        pains=["No time", "Intimidating gyms"], desires=["Visible progress", "A routine that sticks"],
        pillars=[("Train", "Workouts and form tips"), ("Fuel", "Simple nutrition habits"), ("Members", "Progress stories")],
        ctas=["Book a free class", "Join today", "Save this workout"], tone=["energetic", "direct", "encouraging"],
        do=["Short, punchy lines", "Celebrate effort"], dont=["Body shaming", "Unrealistic promises"], use=["strong", "progress", "show up"], avoid=["beach body", "no pain no gain"],
        imagery="High contrast, motion, sweat, real members", music="Driving electronic, 120–128 BPM", voice="Coach: upbeat, firm, motivating"),
    "yoga": dict(label="Yoga & wellness", fonts=("Lora", "Nunito Sans"), energy="calm", persona="The stressed professional seeking calm",
        pains=["Stress and stiffness", "Feeling like a beginner"], desires=["Calm and flexibility", "A welcoming space"],
        pillars=[("Practice", "Short flows and poses"), ("Breathe", "Breathing and mindfulness"), ("Community", "Teachers and students")],
        ctas=["Book your first class", "Try a free flow", "Join the retreat"], tone=["calm", "kind", "grounded"],
        do=["Invite, don't push", "Use breath language"], dont=["Extreme poses as the norm", "Spiritual jargon"], use=["breathe", "practice", "gentle"], avoid=["detox", "perfect pose"],
        imagery="Natural light, plants, soft linen tones", music="Ambient pads, birdsong", voice="Soft, slow, warm teacher"),
    "fashion": dict(label="Fashion boutiques", fonts=("Playfair Display", "Inter"), energy="medium", persona="The style-conscious shopper",
        pains=["Fast fashion that falls apart", "Not knowing what suits them"], desires=["Pieces that last", "Easy outfits"],
        pillars=[("New in", "Fresh arrivals"), ("How to wear it", "Styling ideas"), ("Made well", "Fabric and making")],
        ctas=["Shop new in", "Book a styling session", "Shop the look"], tone=["confident", "editorial", "friendly"],
        do=["Show outfits, not just items", "Talk fabric and fit"], dont=["Trend-chasing language", "Body talk"], use=["fit", "fabric", "wear"], avoid=["must-have", "obsessed"],
        imagery="Editorial portraits, texture details, city backdrops", music="Chic downtempo house", voice="Editor: polished, warm"),
    "streetwear": dict(label="Streetwear & sneakers", fonts=("Bebas Neue", "Barlow"), energy="high", persona="The drop hunter",
        pains=["Missing drops", "Looking like everyone else"], desires=["Limited pieces", "Being first"],
        pillars=[("Drops", "Releases and restocks"), ("Fits", "How people wear it"), ("Culture", "Music, art and the scene")],
        ctas=["Shop the drop", "Get notified", "Link in bio"], tone=["bold", "playful", "street-smart"],
        do=["Keep it short", "Talk like the community"], dont=["Corporate language", "Try-hard slang"], use=["drop", "fit", "limited"], avoid=["fashionista", "trendy"],
        imagery="Flash photography, concrete, close-up sneakers", music="Hip-hop beats, 90 BPM", voice="Hype but chill, young"),
    "jewelry": dict(label="Jewellery", fonts=("Cormorant", "Work Sans"), energy="calm", persona="The meaningful-gift buyer",
        pains=["Generic gifts", "Jewellery that tarnishes"], desires=["Something personal", "Pieces worn every day"],
        pillars=[("Pieces", "New and signature pieces"), ("Made by hand", "The bench and the craft"), ("Stories", "Gifts and the people behind them")],
        ctas=["Shop the collection", "Book a custom piece", "Find the perfect gift"], tone=["refined", "intimate", "warm"],
        do=["Close-up detail shots", "Tell gift stories"], dont=["Discount shouting", "Over-sparkle"], use=["handmade", "everyday", "gift"], avoid=["bling", "luxury lifestyle"],
        imagery="Macro detail, skin tones, soft shadows", music="Gentle piano", voice="Soft, intimate, assured"),
    "pets": dict(label="Pet care", fonts=("Fredoka", "Nunito"), energy="medium", persona="The devoted pet parent",
        pains=["Unhealthy treats", "Bored pets"], desires=["Happy, healthy pets", "Products they can trust"],
        pillars=[("Happy pets", "Customer pets and stories"), ("Care tips", "Health and training tips"), ("What's inside", "Ingredients and safety")],
        ctas=["Shop treats", "Book grooming", "Tag your pet"], tone=["playful", "caring", "trustworthy"],
        do=["Show real pets", "Use their names"], dont=["Guilt-tripping owners", "Medical claims"], use=["happy", "healthy", "tail wags"], avoid=["fur baby overload", "best ever"],
        imagery="Pets at eye level, natural light, mess allowed", music="Upbeat ukulele", voice="Cheerful, warm, a little silly"),
    "plants": dict(label="Plant shops", fonts=("Gloock", "Figtree"), energy="calm", persona="The new plant parent",
        pains=["Plants that die", "Not knowing what fits their light"], desires=["A greener home", "Plants that thrive"],
        pillars=[("Plant care", "Light, water and repotting"), ("Plant of the week", "One plant up close"), ("Green homes", "Customer spaces")],
        ctas=["Find your plant", "Shop plants", "Book a plant clinic"], tone=["gentle", "encouraging", "curious"],
        do=["Give one care tip at a time", "Celebrate small wins"], dont=["Shaming dead plants", "Latin overload"], use=["light", "thrive", "repot"], avoid=["impossible to kill", "jungle vibes"],
        imagery="Window light, leaves, soil, ceramics", music="Soft acoustic guitar", voice="Gentle, encouraging gardener"),
    "books": dict(label="Bookshops", fonts=("Libre Caslon Text", "Work Sans"), energy="calm", persona="The curious reader",
        pains=["Not knowing what to read next", "Algorithm picks"], desires=["A great next book", "Recommendations from people"],
        pillars=[("Staff picks", "Books we love and why"), ("Events", "Readings and clubs"), ("Reading life", "Habits, shelves and quotes")],
        ctas=["Find your next read", "Join the book club", "Visit the shop"], tone=["thoughtful", "witty", "warm"],
        do=["Quote lines from books", "Recommend with reasons"], dont=["Spoilers", "Snobbery"], use=["read", "story", "shelf"], avoid=["bookworm", "must-read"],
        imagery="Shelves, paper texture, reading corners", music="Quiet cello or piano", voice="Bookseller: thoughtful, dry humour"),
    "saas": dict(label="Software & SaaS", fonts=("Inter Tight", "Inter"), energy="medium", persona="The overloaded team lead",
        pains=["Scattered tools", "Manual busywork"], desires=["Time back", "A team that's in sync"],
        pillars=[("Product tips", "Features and shortcuts"), ("Ways of working", "Ideas for better work"), ("Customers", "How teams use it")],
        ctas=["Start free", "Book a demo", "See how it works"], tone=["clear", "helpful", "confident"],
        do=["Show the product", "Lead with the outcome"], dont=["Buzzwords", "Vague claims"], use=["save time", "workflow", "team"], avoid=["synergy", "revolutionary"],
        imagery="Clean UI close-ups, real teams, desks", music="Minimal electronic", voice="Clear, friendly product expert"),
    "fintech": dict(label="Money & fintech", fonts=("Sora", "Nunito Sans"), energy="medium", persona="The first-time saver",
        pains=["Money stress", "Confusing banking"], desires=["Feeling in control", "Saving without thinking"],
        pillars=[("Money basics", "Plain-English money tips"), ("In the app", "Features that help"), ("Goals", "Customer saving stories")],
        ctas=["Open an account", "Download the app", "Start saving"], tone=["plain-spoken", "reassuring", "smart"],
        do=["Use simple numbers", "Explain jargon"], dont=["Get-rich promises", "Fear tactics"], use=["save", "control", "simple"], avoid=["guaranteed returns", "to the moon"],
        imagery="Phones in hand, everyday moments, clean graphics", music="Light electronic, optimistic", voice="Calm, trustworthy, friendly"),
    "realestate": dict(label="Real estate", fonts=("Marcellus", "Manrope"), energy="calm", persona="The first-time buyer",
        pains=["A confusing process", "Missing good listings"], desires=["The right home", "A guide they trust"],
        pillars=[("Listings", "Homes worth seeing"), ("Buying guide", "Step-by-step advice"), ("Neighbourhoods", "Local life and spots")],
        ctas=["Book a viewing", "Get a valuation", "See listings"], tone=["trustworthy", "calm", "local"],
        do=["Show light and space", "Give real numbers"], dont=["Pressure tactics", "Clichés"], use=["home", "neighbourhood", "light"], avoid=["dream home", "won't last"],
        imagery="Wide interiors, daylight, streets", music="Warm acoustic", voice="Calm local expert"),
    "dental": dict(label="Clinics & dental", fonts=("Outfit", "Outfit"), energy="calm", persona="The nervous patient",
        pains=["Dental anxiety", "Unclear costs"], desires=["A calm visit", "A smile they like"],
        pillars=[("Care tips", "Everyday oral care"), ("Meet the team", "People behind the chair"), ("Treatments", "What happens, explained")],
        ctas=["Book a check-up", "Book online", "Ask us a question"], tone=["calm", "clear", "kind"],
        do=["Explain what happens", "Show the team"], dont=["Scary close-ups", "Medical promises"], use=["gentle", "check-up", "smile"], avoid=["pain-free guaranteed", "perfect teeth"],
        imagery="Bright clean rooms, friendly faces", music="Soft piano", voice="Kind, steady, clear"),
    "travel": dict(label="Travel & tours", fonts=("Syne", "Manrope"), energy="medium", persona="The experience collector",
        pains=["Tourist traps", "Planning stress"], desires=["Unforgettable trips", "Someone who knows the place"],
        pillars=[("Destinations", "Places worth the trip"), ("Travel tips", "Packing, timing and local tips"), ("Travellers", "Guest stories")],
        ctas=["Plan your trip", "Book the tour", "Get the itinerary"], tone=["adventurous", "warm", "knowing"],
        do=["Show real places", "Give insider tips"], dont=["Wanderlust clichés", "Exaggeration"], use=["local", "journey", "explore"], avoid=["paradise", "bucket list"],
        imagery="Wide landscapes, golden hour, people in place", music="World-influenced acoustic", voice="Local guide: warm, curious"),
    "photo": dict(label="Photography & studios", fonts=("Italiana", "Jost"), energy="calm", persona="The couple planning a wedding",
        pains=["Stiff photos", "Not knowing how to pose"], desires=["Natural, timeless photos", "Feeling relaxed"],
        pillars=[("Portfolio", "Recent sessions"), ("Tips", "How to prepare for a shoot"), ("Love notes", "Client stories")],
        ctas=["Check your date", "Book a session", "See the portfolio"], tone=["romantic", "relaxed", "honest"],
        do=["Let photos lead", "Share the story behind a shot"], dont=["Over-editing", "Pushy packages"], use=["moment", "natural", "light"], avoid=["magical", "once in a lifetime"],
        imagery="Film tones, candid moments, soft light", music="Cinematic strings", voice="Warm, gentle storyteller"),
    "kids": dict(label="Kids & education", fonts=("Baloo 2", "Nunito"), energy="high", persona="The involved parent",
        pains=["Screen time battles", "Bored kids"], desires=["Kids who love learning", "Activities that build skills"],
        pillars=[("Learn at home", "Simple activities"), ("In class", "What kids are making"), ("Parents", "Tips and stories")],
        ctas=["Book a trial class", "Join the waitlist", "Download the activity"], tone=["cheerful", "encouraging", "clear"],
        do=["Speak to parents", "Show kids creating"], dont=["Fear about falling behind", "Too much text"], use=["learn", "play", "create"], avoid=["genius", "ahead of the class"],
        imagery="Bright colour, hands making things, real classrooms", music="Playful xylophone", voice="Cheerful teacher"),
    "eco": dict(label="Sustainable goods", fonts=("Recoleta", "Mulish"), energy="calm", persona="The low-waste shopper",
        pains=["Greenwashing", "Plastic everywhere"], desires=["Swaps that actually work", "Fewer, better things"],
        pillars=[("Swaps", "Easy low-waste swaps"), ("Made responsibly", "Materials and makers"), ("Impact", "What changes, in numbers")],
        ctas=["Shop the swaps", "Start a refill", "Learn more"], tone=["honest", "optimistic", "practical"],
        do=["Back claims with numbers", "Celebrate small changes"], dont=["Guilt", "Vague eco claims"], use=["refill", "swap", "reuse"], avoid=["eco-friendly (unbacked)", "planet-saving"],
        imagery="Natural materials, refills, sunlight", music="Light folk", voice="Honest, upbeat, practical"),
}
if "Recoleta" in IND["eco"]["fonts"]:  # Recoleta isn't on Google Fonts; use a close free match
    IND["eco"]["fonts"] = ("Fraunces", "Mulish")
if "Cormorant" == IND["jewelry"]["fonts"][0]:
    IND["jewelry"]["fonts"] = ("Cormorant Garamond", "Work Sans")

# What one business in each industry is called in a sentence
NOUN = {"coffee": "roaster", "bakery": "bakery", "restaurant": "restaurant", "skincare": "skincare brand", "fitness": "gym", "yoga": "studio",
        "fashion": "boutique", "streetwear": "label", "jewelry": "jeweller", "pets": "pet brand", "plants": "plant shop", "books": "bookshop",
        "saas": "tool", "fintech": "money app", "realestate": "agency", "dental": "clinic", "travel": "travel company", "photo": "studio",
        "kids": "learning studio", "eco": "shop"}

# ---------------------------------------------------------------- brands: id, name, industry, tagline, hue, accent hue, style, product, price, logo shape
B = [
    ("copper-kettle", "Copper Kettle Roasters", "coffee", "Roasted on Tuesday, in your cup by Friday.", 20, 32, "dark", "House Espresso Blend", "$17 / 340g", "circle"),
    ("north-pour", "North Pour", "coffee", "Light roasts for slow mornings.", 205, 35, "dark", "Nordic Light Roast", "$19 / 250g", "square"),
    ("crema-corner", "Crema Corner", "coffee", "The neighbourhood café that knows your order.", 15, 150, "bright", "Oat Flat White", "$4.80", "arch"),
    ("dawn-patrol-coffee", "Dawn Patrol Coffee", "coffee", "Coffee for people who are up before the sun.", 220, 28, "dark", "Sunrise Cold Brew", "$5.50", "hex"),
    ("bean-and-bloom", "Bean & Bloom", "coffee", "A café with a flower shop inside.", 340, 95, "light", "Rose Latte", "$5.20", "circle"),
    ("rise-and-crumb", "Rise & Crumb", "bakery", "Sourdough that takes two days. Worth it.", 30, 10, "dark", "Country Sourdough", "$8", "arch"),
    ("butter-lane", "Butter Lane Bakery", "bakery", "Croissants with 81 layers. We counted.", 42, 350, "light", "Classic Butter Croissant", "$3.75", "circle"),
    ("little-oven", "The Little Oven", "bakery", "A tiny bakery with big birthday cakes.", 330, 45, "bright", "Celebration Cake", "From $42", "square"),
    ("knead-and-co", "Knead & Co.", "bakery", "Real bread for real sandwiches.", 25, 200, "dark", "Seeded Rye Loaf", "$7", "hex"),
    ("sugar-and-salt", "Sugar & Salt Patisserie", "bakery", "French pastry, made every morning.", 350, 160, "light", "Pistachio Éclair", "$5", "diamond"),
    ("ember-table", "Ember Table", "restaurant", "Everything on the menu meets the fire.", 12, 38, "dark", "Wood-fired Tasting Menu", "$65", "square"),
    ("saffron-street", "Saffron Street", "restaurant", "Street food from Mumbai, cooked like home.", 35, 170, "bright", "Thali for Two", "$34", "circle"),
    ("tide-and-thyme", "Tide & Thyme", "restaurant", "Seafood from the morning catch.", 195, 20, "dark", "Catch of the Day", "Market price", "arch"),
    ("nonna-rosa", "Nonna Rosa", "restaurant", "Pasta rolled by hand, every afternoon.", 5, 120, "bright", "Tagliatelle al Ragù", "$19", "circle"),
    ("green-bowl", "Green Bowl Kitchen", "restaurant", "Bowls that keep you going till dinner.", 140, 40, "dark", "Harvest Bowl", "$13", "hex"),
    ("dew-theory", "Dew Theory", "skincare", "Hydration, explained.", 190, 330, "light", "Barrier Repair Serum", "$34", "circle"),
    ("lumen-skin", "Lumen Skin", "skincare", "Gentle actives for sensitive skin.", 30, 200, "light", "Calm Vitamin C", "$38", "arch"),
    ("oat-and-ash", "Oat & Ash", "skincare", "Three-step skincare. Nothing extra.", 35, 160, "dark", "The Daily Trio", "$58", "square"),
    ("velvet-clay", "Velvet Clay", "skincare", "Clay masks with a softer touch.", 15, 260, "light", "Pink Clay Mask", "$26", "hex"),
    ("bloom-ritual", "Bloom Ritual", "skincare", "Botanical body care for slow evenings.", 300, 140, "dark", "Night Body Oil", "$32", "circle"),
    ("iron-tide", "Iron Tide Gym", "fitness", "Strength training for real life.", 210, 15, "dark", "Unlimited Membership", "$59 / month", "hex"),
    ("pulse-lab", "Pulse Lab", "fitness", "45-minute classes that count.", 350, 190, "bright", "10-Class Pack", "$120", "diamond"),
    ("forge-strength", "Forge Strength Club", "fitness", "Lift heavy, leave strong.", 25, 50, "dark", "Coached Strength Program", "$89 / month", "square"),
    ("stride-run-club", "Stride Run Club", "fitness", "Run together, get faster.", 160, 20, "bright", "Couch to 5K Plan", "$49", "circle"),
    ("kettlebell-district", "Kettlebell District", "fitness", "Kettlebells only. Results always.", 0, 45, "dark", "Starter Kettlebell Course", "$79", "hex"),
    ("still-water-yoga", "Still Water Yoga", "yoga", "A quiet room in a busy city.", 185, 25, "light", "Intro Month Pass", "$45", "circle"),
    ("lotus-and-light", "Lotus & Light", "yoga", "Yoga for every body.", 300, 160, "light", "Beginner Series", "$80", "arch"),
    ("mat-and-mind", "Mat & Mind", "yoga", "Movement and mindfulness, 30 minutes a day.", 140, 330, "dark", "On-demand Membership", "$15 / month", "square"),
    ("sunsalute-studio", "Sun Salute Studio", "yoga", "Morning flows to start the day right.", 40, 200, "light", "Sunrise Flow Pass", "$60", "circle"),
    ("breathe-collective", "Breathe Collective", "yoga", "Breathwork and yoga retreats.", 200, 35, "dark", "Weekend Retreat", "$390", "hex"),
    ("thread-and-row", "Thread & Row", "fashion", "Wardrobe staples that last ten years.", 25, 210, "dark", "The Everyday Shirt", "$85", "square"),
    ("maison-verde", "Maison Verde", "fashion", "Linen, made slowly.", 100, 20, "light", "Linen Wrap Dress", "$140", "arch"),
    ("fold-boutique", "Fold Boutique", "fashion", "Curated pieces from independent designers.", 330, 50, "dark", "Designer Edit Box", "$160", "diamond"),
    ("sunday-tailor", "Sunday Tailor", "fashion", "Made-to-measure without the fuss.", 220, 40, "dark", "Custom Blazer", "From $290", "square"),
    ("petal-and-hem", "Petal & Hem", "fashion", "Dresses for every celebration.", 345, 170, "light", "Garden Party Dress", "$120", "circle"),
    ("concrete-kids", "Concrete Kids", "streetwear", "Streetwear from the skatepark up.", 0, 85, "dark", "Heavyweight Hoodie", "$75", "square"),
    ("sole-district", "Sole District", "streetwear", "Rare sneakers, verified.", 260, 50, "dark", "Authenticated Sneaker Drop", "From $160", "hex"),
    ("neon-alley", "Neon Alley", "streetwear", "Night-time graphics, daytime fits.", 280, 160, "bright", "Glow Graphic Tee", "$38", "diamond"),
    ("lowkey-supply", "Lowkey Supply", "streetwear", "Quiet logos, loud quality.", 210, 15, "dark", "Boxy Tee 3-Pack", "$65", "square"),
    ("rooftop-crew", "Rooftop Crew", "streetwear", "Made in the city, worn on the roof.", 15, 190, "bright", "Crew Cap", "$32", "circle"),
    ("gilded-thread", "Gilded Thread", "jewelry", "Fine gold for everyday wear.", 40, 350, "dark", "Solid Gold Chain", "$220", "circle"),
    ("moonstone-atelier", "Moonstone Atelier", "jewelry", "Stones with stories.", 250, 40, "light", "Moonstone Ring", "$180", "diamond"),
    ("tiny-heirloom", "Tiny Heirloom", "jewelry", "Personalised pieces to pass down.", 20, 210, "light", "Engraved Locket", "$95", "arch"),
    ("salt-and-silver", "Salt & Silver", "jewelry", "Ocean-inspired silver, made by hand.", 195, 30, "dark", "Wave Silver Cuff", "$120", "circle"),
    ("ember-and-gold", "Ember & Gold", "jewelry", "Bold pieces for bold days.", 10, 45, "dark", "Statement Hoops", "$150", "hex"),
    ("happy-paws", "Happy Paws", "pets", "Treats dogs go wild for, ingredients you'll recognise.", 30, 200, "bright", "Peanut Butter Biscuits", "$12", "circle"),
    ("whisker-and-co", "Whisker & Co.", "pets", "Everything for indoor cats.", 280, 40, "light", "Cat Tower Deluxe", "$129", "square"),
    ("the-good-groomer", "The Good Groomer", "pets", "Calm grooming for nervous dogs.", 170, 20, "dark", "Full Groom", "From $55", "arch"),
    ("fetch-and-feast", "Fetch & Feast", "pets", "Fresh dog food, delivered.", 15, 150, "bright", "Fresh Food Plan", "$3 / day", "circle"),
    ("tailwind-pets", "Tailwind Pet Supply", "pets", "Gear for adventurous dogs.", 205, 30, "dark", "Trail Harness", "$45", "hex"),
    ("leaf-and-light", "Leaf & Light", "plants", "Plants matched to your window.", 120, 30, "dark", "Low-light Starter Set", "$48", "circle"),
    ("the-fern-room", "The Fern Room", "plants", "A shop full of ferns, and help.", 150, 350, "light", "Boston Fern", "$28", "arch"),
    ("pothos-place", "Pothos Place", "plants", "Hard-to-kill plants for new plant parents.", 95, 280, "bright", "Golden Pothos", "$18", "square"),
    ("terra-and-twig", "Terra & Twig", "plants", "Plants, pots and good soil.", 25, 130, "dark", "Ceramic Pot Bundle", "$54", "hex"),
    ("greenhouse-nine", "Greenhouse Nine", "plants", "Rare plants from our own greenhouse.", 160, 40, "dark", "Variegated Monstera", "$95", "diamond"),
    ("dog-eared-books", "Dog-Eared Books", "books", "Well-loved books, ready for you.", 20, 210, "dark", "Mystery Book Box", "$35", "square"),
    ("chapter-and-verse", "Chapter & Verse", "books", "Poetry and fiction, picked by people.", 260, 30, "dark", "Staff Pick Subscription", "$22 / month", "arch"),
    ("the-reading-nook", "The Reading Nook", "books", "Kids' books and story time.", 45, 200, "light", "Story Time Pass", "$10", "circle"),
    ("ink-and-index", "Ink & Index", "books", "Non-fiction for curious minds.", 210, 10, "dark", "Big Ideas Bundle", "$58", "square"),
    ("paper-lantern-books", "Paper Lantern Books", "books", "Translated fiction from around the world.", 0, 45, "dark", "World Fiction Box", "$40", "hex"),
    ("taskflow", "Taskflow", "saas", "Plan the week in ten minutes.", 230, 160, "bright", "Team Plan", "$8 / user / month", "square"),
    ("brightdesk", "Brightdesk", "saas", "Customer support that feels personal.", 260, 40, "bright", "Support Starter", "$29 / month", "circle"),
    ("ledgerly", "Ledgerly", "saas", "Invoices and expenses without the spreadsheet.", 160, 20, "dark", "Freelancer Plan", "$12 / month", "hex"),
    ("formwell", "Formwell", "saas", "Forms people actually finish.", 15, 210, "bright", "Pro Forms", "$19 / month", "diamond"),
    ("signalbox", "Signalbox", "saas", "Know when something breaks before customers do.", 200, 10, "dark", "Monitoring Pro", "$49 / month", "square"),
    ("penny-jar", "Penny Jar", "fintech", "Round up, save up.", 140, 40, "bright", "Round-up Savings", "Free", "circle"),
    ("stackwise", "Stackwise", "fintech", "Budgeting for people who hate budgeting.", 250, 150, "bright", "Stack Plus", "$4 / month", "square"),
    ("harborline", "Harborline", "fintech", "A bank that explains itself.", 210, 30, "dark", "Everyday Account", "No monthly fee", "arch"),
    ("splitly", "Splitly", "fintech", "Split bills without the awkward chat.", 180, 330, "bright", "Group Wallet", "Free", "hex"),
    ("future-fund", "Future Fund", "fintech", "Investing for beginners, in plain English.", 160, 45, "dark", "Starter Portfolio", "From $5", "diamond"),
    ("keystone-homes", "Keystone Homes", "realestate", "Your first home, step by step.", 215, 35, "dark", "First-time Buyer Program", "Free consultation", "arch"),
    ("open-door-realty", "Open Door Realty", "realestate", "Homes with room to grow.", 25, 200, "dark", "Home Valuation", "Free", "square"),
    ("brick-and-beam", "Brick & Beam", "realestate", "Character homes in old neighbourhoods.", 10, 180, "dark", "Heritage Listings", "—", "hex"),
    ("coastline-living", "Coastline Living", "realestate", "Homes by the water.", 195, 25, "light", "Seaside Viewing Tour", "Free", "arch"),
    ("urban-nest", "Urban Nest", "realestate", "City apartments, honestly described.", 280, 45, "dark", "Apartment Finder", "Free", "square"),
    ("smile-studio", "Smile Studio Dental", "dental", "Check-ups without the dread.", 190, 30, "light", "New Patient Check-up", "$89", "circle"),
    ("bright-dental", "Bright Dental Care", "dental", "Family dentistry, Saturdays too.", 205, 150, "dark", "Family Plan", "$29 / month", "square"),
    ("gentle-hands-clinic", "Gentle Hands Physio", "dental", "Physiotherapy that gets you moving.", 160, 20, "dark", "Assessment Session", "$75", "arch"),
    ("clearview-optics", "Clearview Optics", "dental", "Eye tests and frames you'll love.", 220, 40, "bright", "Eye Test + Frames", "$149", "circle"),
    ("calm-cove-clinic", "Calm Cove Clinic", "dental", "Skin and laser clinic, explained simply.", 180, 340, "light", "Consultation", "Free", "hex"),
    ("wander-wild", "Wander Wild Tours", "travel", "Small-group trips off the beaten path.", 150, 30, "dark", "7-Day Highlands Trek", "$1,290", "diamond"),
    ("passport-club", "Passport Club", "travel", "Weekend city breaks, planned for you.", 230, 45, "bright", "City Break Bundle", "From $390", "circle"),
    ("slow-roads", "Slow Roads", "travel", "Road trips with the good stops marked.", 30, 190, "dark", "Coastal Road Trip Guide", "$29", "arch"),
    ("island-hopper", "Island Hopper", "travel", "Island trips, sorted.", 185, 20, "bright", "Three-Island Pass", "$540", "circle"),
    ("local-lens-tours", "Local Lens Tours", "travel", "City tours led by locals.", 340, 160, "dark", "Food Walking Tour", "$65", "hex"),
    ("golden-hour-studio", "Golden Hour Studio", "photo", "Wedding photos that feel like you.", 35, 350, "dark", "Full-day Wedding", "From $2,800", "circle"),
    ("frame-and-field", "Frame & Field", "photo", "Outdoor family portraits.", 110, 30, "dark", "Family Session", "$350", "arch"),
    ("still-life-co", "Still Life Co.", "photo", "Product photography for small brands.", 0, 200, "dark", "Product Shoot (10 images)", "$450", "square"),
    ("film-and-flower", "Film & Flower", "photo", "Film photography for couples.", 330, 90, "light", "Elopement Package", "$1,600", "diamond"),
    ("headshot-house", "Headshot House", "photo", "Headshots in 20 minutes.", 215, 30, "bright", "Express Headshot", "$129", "square"),
    ("little-makers", "Little Makers", "kids", "Craft and science classes for ages 5–10.", 45, 200, "bright", "Weekly Maker Class", "$25 / class", "circle"),
    ("bright-sparks", "Bright Sparks Tutoring", "kids", "Tutoring that builds confidence.", 220, 40, "bright", "Maths Tutoring", "$45 / hour", "square"),
    ("tiny-coders", "Tiny Coders", "kids", "Kids learn to code by making games.", 270, 150, "bright", "Game Design Course", "$190", "hex"),
    ("story-sprouts", "Story Sprouts", "kids", "Reading adventures for early readers.", 120, 20, "light", "Reading Club", "$15 / month", "circle"),
    ("play-lab", "Play Lab", "kids", "Holiday camps where kids build things.", 10, 190, "bright", "Summer Camp Week", "$280", "diamond"),
    ("refill-roots", "Refill Roots", "eco", "Refill shop for the whole home.", 120, 30, "dark", "Refill Starter Kit", "$39", "circle"),
    ("loop-goods", "Loop Goods", "eco", "Reusable everything.", 170, 20, "dark", "Reusable Bag Set", "$24", "hex"),
    ("bare-necessities", "Bare Necessities", "eco", "Plastic-free bathroom basics.", 35, 160, "light", "Shampoo Bar Trio", "$28", "arch"),
    ("second-life-co", "Second Life Co.", "eco", "Pre-loved furniture, restored.", 25, 210, "dark", "Restored Oak Chair", "$180", "square"),
    ("sun-cycle", "Sun Cycle", "eco", "Solar gadgets for everyday life.", 50, 200, "dark", "Solar Power Bank", "$59", "circle"),
]

def build(b):
    id, name, ind, tagline, hue, acc, style, product, price, shape = b
    t = IND[ind]
    c = palette(hue, acc, style)
    handle = "@" + id.replace("-", "")
    brand = {
        "name": name, "slug": id, "tagline": tagline, "website": "", "language": "en",
        "essence": {
            "mission": f"Give every {t['persona'].lower().replace('the ', '')} {t['desires'][0][0].lower() + t['desires'][0][1:]}.",
            "positioning": f"For {t['persona'].lower()} who wants {t['desires'][0][0].lower() + t['desires'][0][1:]}, {name} is the {NOUN[ind]} that makes it easy, unlike the usual options.",
            "values": [t["tone"][0], "care", "honesty"],
            "personality": t["tone"],
            "archetype": {"calm": "The Caregiver", "medium": "The Everyman", "high": "The Hero"}[t["energy"]],
        },
        "audience": [{"name": t["persona"].replace("The ", "").capitalize(), "description": f"People who {t['desires'][0].lower()}.", "pains": t["pains"], "desires": t["desires"], "objections": ["It costs more than the usual option"], "platforms": ["instagram", "tiktok"]}],
        "voice": {"tone": t["tone"], "do": t["do"], "dont": t["dont"], "vocabulary": {"use": t["use"], "avoid": t["avoid"]},
                  "examples": [tagline, f"{product}: {t['desires'][0].lower()}, without the fuss."]},
        "visual": {
            "colors": c,
            "fonts": {"display": {"family": t["fonts"][0], "weight": 700 if t["fonts"][0] not in ("Bebas Neue", "Anton", "Archivo Black", "Italiana", "Marcellus", "Gloock", "DM Serif Display", "Young Serif") else 400, "google": True},
                      "body": {"family": t["fonts"][1], "weight": 400, "google": True}},
            "logo": {"primary": "assets/logos/logo.svg", "mark": "assets/logos/logo.svg", "onDark": "assets/logos/logo.svg"},
            "radius": {"calm": 28, "medium": 20, "high": 12}[t["energy"]],
            "imagery": t["imagery"],
            "motion": {"energy": t["energy"], "ease": {"calm": "power2.out", "medium": "power3.out", "high": "expo.out"}[t["energy"]], "notes": ""},
        },
        "audio": {"voices": {"narrator": {"provider": "elevenlabs", "voice_id": "", "model_id": "eleven_multilingual_v2", "settings": {"stability": 0.5, "similarity_boost": 0.8, "style": 0.25, "use_speaker_boost": True}, "description": t["voice"]}}, "music": t["music"]},
        "products": [{"name": product, "description": f"Our signature {NOUN[ind]} offer.", "benefits": t["desires"], "proof": [], "price": price}],
        "content_pillars": [{"name": n, "description": d} for n, d in t["pillars"]],
        "ctas": t["ctas"],
        "platforms": {"instagram": {"handle": handle, "formats": ["reel", "carousel", "post", "story"]}, "tiktok": {"handle": handle, "formats": ["reel"]}, "youtube": {"handle": handle, "formats": ["short"]}, "linkedin": {"handle": "", "formats": []}},
        "hashtags": {"core": ["#" + id.replace("-", "")], "rotating": ["#" + w for w in t["use"][:2]]},
    }
    return {"kind": "brand", "id": id, "name": name, "industry": ind, "industryLabel": t["label"], "tagline": tagline, "logoSvg": logo_svg(name, c, shape), "brand": brand}

if __name__ == "__main__":
    out = os.path.join(ROOT, "brands")
    os.makedirs(out, exist_ok=True)
    seen = set()
    for row in B:
        e = build(row)
        assert e["id"] not in seen, e["id"]
        seen.add(e["id"])
        c = e["brand"]["visual"]["colors"]
        assert ratio(c["ink"], c["background"]) >= 4.5 and ratio(c["secondary"], c["primary"]) >= 4.5 and ratio(c["accent"], c["background"]) >= 3, (e["id"], c)
        with open(os.path.join(out, f"{e['id']}.json"), "w") as f:
            json.dump(e, f, indent=2, ensure_ascii=False)
            f.write("\n")
    print(f"wrote {len(B)} brand starters across {len(IND)} industries")
