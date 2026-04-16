"""One-time script to populate comprehensive product options from research."""
import json, os

DATA_FILE = "project_data.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Preserve current selections
selections = data.get("selections", {})

# ─────────────────────────────────────────────
# DECKING (25 options)
# ─────────────────────────────────────────────
data["product_options"]["decking"] = [
    # --- Trex ---
    {"id": "trex-enhance-basics", "name": "Trex Enhance Basics", "brand": "Trex", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 3.15, "retail": 4.00, "offered": 4.25, "notes": "Entry-level; single-sided cap; 25-yr warranty"},
    {"id": "trex-enhance-naturals", "name": "Trex Enhance Naturals", "brand": "Trex", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 3.65, "retail": 4.65, "offered": 4.90, "notes": "Multi-tonal grain; 25-yr warranty; most popular Trex SKU"},
    {"id": "trex-select", "name": "Trex Select", "brand": "Trex", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 4.25, "retail": 5.50, "offered": 5.90, "notes": "Mid-tier; 35-yr warranty; grooved for hidden fasteners"},
    {"id": "trex-transcend", "name": "Trex Transcend", "brand": "Trex", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 5.75, "retail": 7.50, "offered": 8.00, "notes": "50-yr warranty; widest color palette; premium wood look"},
    {"id": "trex-transcend-lineage", "name": "Trex Transcend Lineage", "brand": "Trex", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 6.75, "retail": 9.00, "offered": 9.50, "notes": "CoolDeck tech (25F cooler); 50-yr warranty; top Trex"},
    # --- TimberTech / AZEK ---
    {"id": "timbertech-edge", "name": "TimberTech Edge", "brand": "TimberTech", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 3.90, "retail": 5.00, "offered": 5.25, "notes": "Entry TimberTech composite; 30-yr warranty"},
    {"id": "timbertech-legacy", "name": "TimberTech Legacy", "brand": "TimberTech", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 4.75, "retail": 6.15, "offered": 6.50, "notes": "Mid-grade composite; 30-yr warranty; multi-width boards"},
    {"id": "azek-harvest", "name": "AZEK Harvest Collection", "brand": "AZEK", "type": "Advanced PVC", "unit": "per LF",
     "wholesale": 5.00, "retail": 6.50, "offered": 7.00, "notes": "100% PVC, zero organic content; 30-yr full warranty"},
    {"id": "azek-landmark", "name": "AZEK Landmark Collection", "brand": "AZEK", "type": "Advanced PVC", "unit": "per LF",
     "wholesale": 5.90, "retail": 7.75, "offered": 8.25, "notes": "Mid-tier PVC; richer grain; contractor favorite"},
    {"id": "azek-vintage", "name": "AZEK Vintage Collection", "brand": "AZEK", "type": "Advanced PVC", "unit": "per LF",
     "wholesale": 6.75, "retail": 8.75, "offered": 9.25, "notes": "Top AZEK; most realistic wood aesthetic; 30-yr warranty"},
    # --- Fiberon ---
    {"id": "fiberon-goodlife", "name": "Fiberon Good Life", "brand": "Fiberon", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 2.45, "retail": 3.40, "offered": 3.65, "notes": "Budget entry composite; 25-yr warranty"},
    {"id": "fiberon-symmetry", "name": "Fiberon Symmetry", "brand": "Fiberon", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 5.15, "retail": 6.50, "offered": 6.90, "notes": "Mid-premium smooth face; 25-yr fade/stain warranty"},
    {"id": "fiberon-paramount", "name": "Fiberon Paramount", "brand": "Fiberon", "type": "3-Sided PVC Cap", "unit": "per LF",
     "wholesale": 5.50, "retail": 7.00, "offered": 7.50, "notes": "PVC-capped 3 sides; lifetime residential warranty"},
    {"id": "fiberon-promenade", "name": "Fiberon Promenade", "brand": "Fiberon", "type": "4-Sided PVC Cap", "unit": "per LF",
     "wholesale": 8.50, "retail": 10.25, "offered": 11.25, "notes": "Full PVC; 4-sided cap; lifetime warranty; AZEK alternative"},
    # --- Deckorators ---
    {"id": "deckorators-frontier", "name": "Deckorators Frontier", "brand": "Deckorators", "type": "Mineral-Based Composite", "unit": "per LF",
     "wholesale": 4.15, "retail": 5.15, "offered": 5.50, "notes": "Zero wood fiber = zero moisture absorption; 30-yr warranty"},
    {"id": "deckorators-vault", "name": "Deckorators Vault", "brand": "Deckorators", "type": "Mineral-Based Composite", "unit": "per LF",
     "wholesale": 4.75, "retail": 6.00, "offered": 6.50, "notes": "Mid-tier MBC; richer colors; 30-yr warranty; Lowe's"},
    {"id": "deckorators-voyage", "name": "Deckorators Voyage", "brand": "Deckorators", "type": "Mineral-Based Composite", "unit": "per LF",
     "wholesale": 4.90, "retail": 6.40, "offered": 6.75, "notes": "Premium MBC; most realistic grain; 30-yr warranty"},
    # --- Wolf ---
    {"id": "wolf-perspective", "name": "Wolf Perspective", "brand": "Wolf", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 5.75, "retail": 7.25, "offered": 7.75, "notes": "Mid-premium; 25-yr warranty; dealer/lumberyard channel"},
    {"id": "wolf-serenity", "name": "Wolf Serenity", "brand": "Wolf", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 7.65, "retail": 9.25, "offered": 10.00, "notes": "Premium line; deep embossing; 25-yr warranty"},
    # --- MoistureShield ---
    {"id": "moistureshield-elevate", "name": "MoistureShield Elevate", "brand": "MoistureShield", "type": "Capped Composite", "unit": "per LF",
     "wholesale": 4.85, "retail": 6.00, "offered": 6.50, "notes": "Can be submerged; great for lakefront; 25-yr warranty"},
    {"id": "moistureshield-vision", "name": "MoistureShield Vision CoolDeck", "brand": "MoistureShield", "type": "Premium Composite", "unit": "per LF",
     "wholesale": 7.60, "retail": 9.50, "offered": 10.25, "notes": "CoolDeck tech (25F cooler surface); 25-yr warranty"},
    # --- Zuri ---
    {"id": "zuri-premium", "name": "Zuri Premium", "brand": "Zuri (Royal)", "type": "Full Cellular PVC", "unit": "per LF",
     "wholesale": 9.75, "retail": 12.50, "offered": 13.50, "notes": "Most realistic PVC on market; hardwood-exact texture; dealer-only"},
    # --- Natural Wood ---
    {"id": "western-red-cedar", "name": "Western Red Cedar (Clear)", "brand": "Natural Wood", "type": "Wood", "unit": "per LF",
     "wholesale": 5.25, "retail": 7.50, "offered": 8.50, "notes": "Naturally rot-resistant; requires annual staining; 15-30yr life"},
    {"id": "ipe-hardwood", "name": "Ipe (Brazilian Walnut)", "brand": "Natural Wood", "type": "Tropical Hardwood", "unit": "per LF",
     "wholesale": 7.50, "retail": 10.50, "offered": 11.50, "notes": "Hardest deck wood; 75-yr lifespan; Class A fire rated"},
    {"id": "pt-pine", "name": "Pressure-Treated Pine", "brand": "Natural Wood", "type": "PT Lumber", "unit": "per LF",
     "wholesale": 1.50, "retail": 2.15, "offered": 2.75, "notes": "Most affordable; requires annual maintenance; 15-20yr life"},
]

# ─────────────────────────────────────────────
# RAILING (15 options)
# ─────────────────────────────────────────────
data["product_options"]["railing"] = [
    # --- Composite ---
    {"id": "trex-select-rail", "name": "Trex Select Railing", "brand": "Trex", "type": "Composite", "unit": "per LF",
     "wholesale": 33.00, "retail": 45.00, "offered": 50.00, "notes": "Entry composite railing; white/black only; 25-yr warranty"},
    {"id": "trex-transcend-rail", "name": "Trex Transcend Railing", "brand": "Trex", "type": "Composite", "unit": "per LF",
     "wholesale": 50.00, "retail": 68.00, "offered": 75.00, "notes": "Premium composite; matches Transcend deck colors; 25-yr warranty"},
    {"id": "timbertech-radiance-express", "name": "TimberTech RadianceRail Express", "brand": "TimberTech", "type": "Composite", "unit": "per LF",
     "wholesale": 55.00, "retail": 78.00, "offered": 85.00, "notes": "Minimalist look; kit-based; 30-yr warranty"},
    {"id": "timbertech-radiance-full", "name": "TimberTech RadianceRail", "brand": "TimberTech", "type": "Composite + Aluminum", "unit": "per LF",
     "wholesale": 78.00, "retail": 110.00, "offered": 122.00, "notes": "Multiple profiles; cable infill option; 30-yr warranty"},
    {"id": "deckorators-estate", "name": "Deckorators Estate", "brand": "Deckorators", "type": "Composite", "unit": "per LF",
     "wholesale": 38.00, "retail": 51.00, "offered": 58.00, "notes": "Mid-range composite; matches Deckorators decking; 20-yr warranty"},
    # --- Aluminum ---
    {"id": "trex-signature-rail", "name": "Trex Signature Aluminum", "brand": "Trex", "type": "Aluminum", "unit": "per LF",
     "wholesale": 65.00, "retail": 88.00, "offered": 98.00, "notes": "Sleek modern profile; matches Trex deck colors; 25-yr warranty"},
    {"id": "deckorators-alx", "name": "Deckorators ALX", "brand": "Deckorators", "type": "Aluminum", "unit": "per LF",
     "wholesale": 47.00, "retail": 63.00, "offered": 70.00, "notes": "Powder-coated aluminum; mid-price; Lowe's; 20-yr warranty"},
    {"id": "fortress-al13", "name": "Fortress Al13 PLUS", "brand": "Fortress", "type": "Aluminum (Pre-Welded)", "unit": "per LF",
     "wholesale": 55.00, "retail": 78.00, "offered": 85.00, "notes": "Pre-welded panels; bracket-mount; minimal site fabrication"},
    {"id": "westbury-tuscany", "name": "Westbury Tuscany C10", "brand": "Westbury", "type": "Aluminum", "unit": "per LF",
     "wholesale": 60.00, "retail": 83.00, "offered": 92.00, "notes": "Industry workhorse; 12 standard colors; square or round balusters"},
    {"id": "railblazers", "name": "RailBlazers Aluminum", "brand": "RailBlazers", "type": "Aluminum", "unit": "per LF",
     "wholesale": 49.00, "retail": 67.00, "offered": 74.00, "notes": "DIY-friendly; Lowe's; galvanized + powder-coated; good value"},
    # --- Cable ---
    {"id": "feeney-cablerail", "name": "Feeney CableRail (infill only)", "brand": "Feeney", "type": "Stainless Cable", "unit": "per LF",
     "wholesale": 26.00, "retail": 42.00, "offered": 50.00, "notes": "Cable infill only; requires separate frame; price drops on long runs"},
    {"id": "feeney-designrail", "name": "Feeney DesignRail (complete)", "brand": "Feeney", "type": "Aluminum + Cable", "unit": "per LF",
     "wholesale": 105.00, "retail": 135.00, "offered": 148.00, "notes": "Complete frame + cable system; elite cable railing; 10-yr warranty"},
    {"id": "atlantis-raileasy", "name": "Atlantis RailEasy", "brand": "Atlantis Rail", "type": "Stainless Cable", "unit": "per LF",
     "wholesale": 25.00, "retail": 36.00, "offered": 42.00, "notes": "Most economical cable infill; modular; works with any post system"},
    # --- Glass ---
    {"id": "framed-glass", "name": "Framed Glass Panel", "brand": "Various", "type": "Tempered Glass + Aluminum", "unit": "per LF",
     "wholesale": 118.00, "retail": 170.00, "offered": 188.00, "notes": "Aluminum-framed tempered glass; maximizes views; coastal/elevated"},
    {"id": "frameless-glass", "name": "Frameless Glass Panel", "brand": "Custom Fabricated", "type": "Structural Tempered Glass", "unit": "per LF",
     "wholesale": 185.00, "retail": 240.00, "offered": 270.00, "notes": "Post-mounted standoff glass; custom-fabricated; most premium option"},
]

# ─────────────────────────────────────────────
# WATERPROOFING (10 options)
# ─────────────────────────────────────────────
data["product_options"]["waterproofing"] = [
    {"id": "trex-rainescape", "name": "Trex RainEscape", "brand": "Trex", "type": "Above-Joist Trough (HDPE)", "unit": "per SF",
     "wholesale": 4.25, "retail": 7.00, "offered": 5.75, "notes": "Market leader; installed before decking; feeds to downspouts; 10-yr warranty"},
    {"id": "timbertech-dryspace", "name": "TimberTech DrySpace", "brand": "TimberTech", "type": "Below-Joist Vinyl Ceiling", "unit": "per SF",
     "wholesale": 3.75, "retail": 5.00, "offered": 4.75, "notes": "Retrofit-friendly; clips under existing deck; 25-yr warranty"},
    {"id": "dek-drain", "name": "DEK Drain", "brand": "DEK Drain", "type": "Below-Joist Rubber Membrane", "unit": "per SF",
     "wholesale": 3.50, "retail": 5.50, "offered": 4.50, "notes": "Rubber membrane + cap strips; lifetime transferable warranty; retrofit OK"},
    {"id": "wahoo-dryjoistez", "name": "Wahoo DryJoist EZ", "brand": "Wahoo Decks", "type": "Above-Joist Structural", "unit": "per SF",
     "wholesale": 8.50, "retail": 12.50, "offered": 11.50, "notes": "Structural drainage; commercial-grade; high-load capacity"},
    {"id": "dexerdry", "name": "DexerDry", "brand": "DexerDry", "type": "Above-Joist Membrane Roll", "unit": "per SF",
     "wholesale": 5.00, "retail": 7.00, "offered": 6.50, "notes": "Roll-applied between joists before decking; compatible with major brands"},
    {"id": "amazing-underdeck", "name": "Amazing Underdeck", "brand": "Amazing Underdeck", "type": "Below-Joist Aluminum Ceiling", "unit": "per SF",
     "wholesale": 21.00, "retail": 30.00, "offered": 35.00, "notes": "Finished aluminum ceiling (not just drainage); installed system; premium"},
    {"id": "zip-system-deck", "name": "ZIP System Deck Tape", "brand": "Huber", "type": "Above-Joist Membrane/Tape", "unit": "per SF",
     "wholesale": 2.00, "retail": 2.75, "offered": 2.50, "notes": "Budget option; ZIP tape over joist sheathing; not a complete system"},
    {"id": "aluminum-underdeck", "name": "Aluminum T&G Underdeck", "brand": "Various", "type": "Below-Joist Aluminum Panels", "unit": "per SF",
     "wholesale": 8.00, "retail": 10.50, "offered": 10.00, "notes": "Tongue-and-groove aluminum panels from below; mill or painted finish"},
    {"id": "vinyl-underdeck", "name": "Vinyl V-Panel Underdeck", "brand": "Various", "type": "Below-Joist Vinyl Panels", "unit": "per SF",
     "wholesale": 7.00, "retail": 10.00, "offered": 9.00, "notes": "PVC V-groove panels under deck; affordable; watch slope for drainage"},
    {"id": "landscape-gutter", "name": "Membrane + Gutter (Budget)", "brand": "DIY", "type": "Flexible Membrane", "unit": "per SF",
     "wholesale": 1.00, "retail": 1.75, "offered": 1.50, "notes": "Budget retrofit; fabric stapled over joists + gutter; no finished look"},
]

# ─────────────────────────────────────────────
# SCREENING (12 options)
# ─────────────────────────────────────────────
data["product_options"]["screening"] = [
    {"id": "screen-tight-original", "name": "Screen Tight Original", "brand": "Screen Tight", "type": "PVC Spline-Track", "unit": "per LF",
     "wholesale": 1.25, "retail": 2.15, "offered": 2.50, "notes": "Most widely used system; PVC base + cap strip; HD/Lowe's; kits ~$275"},
    {"id": "screeneze-original", "name": "ScreenEze Original", "brand": "ScreenEze", "type": "Aluminum No-Spline", "unit": "per LF",
     "wholesale": 3.00, "retail": 4.25, "offered": 5.00, "notes": "No spline needed; screen locks into extrusion; clean look"},
    {"id": "screeneze-ultimate", "name": "ScreenEze Ultimate", "brand": "ScreenEze", "type": "Aluminum No-Spline (HD)", "unit": "per LF",
     "wholesale": 4.25, "retail": 6.00, "offered": 7.00, "notes": "Heavy-duty; wider track; better for large spans & windy locations"},
    {"id": "pca-ek100", "name": "PCA EK-100 Enclosure Kit", "brand": "PCA Products", "type": "Aluminum Door/Frame", "unit": "per unit",
     "wholesale": 102.00, "retail": 165.00, "offered": 225.00, "notes": "Aluminum screen door systems; 70+ styles; 6 colors; USA-made"},
    {"id": "phantom-classic", "name": "Phantom Classic (Manual)", "brand": "Phantom Screens", "type": "Manual Retractable", "unit": "per unit",
     "wholesale": 475.00, "retail": 700.00, "offered": 950.00, "notes": "Spring-retracted; custom-built to opening; contractor-installed only"},
    {"id": "phantom-executive", "name": "Phantom Executive (Motorized)", "brand": "Phantom Screens", "type": "Motorized Retractable", "unit": "per unit",
     "wholesale": 2000.00, "retail": 3500.00, "offered": 4500.00, "notes": "Motorized; custom up to 40ft wide; requires 110V; premium"},
    {"id": "apollo-motorized", "name": "Apollo Motorized Screen", "brand": "Apollo Screen", "type": "Motorized Retractable", "unit": "per unit",
     "wholesale": 1600.00, "retail": 2750.00, "offered": 3750.00, "notes": "Up to 30ft wide; 7-yr motor/15-yr fabric warranty; price-stable 2025"},
    {"id": "lifestyle-screen", "name": "Lifestyle Garage/Porch Screen", "brand": "Lifestyle Screens", "type": "Motorized Retractable", "unit": "per unit",
     "wholesale": 1400.00, "retail": 2400.00, "offered": 3250.00, "notes": "Great for large openings up to 20ft; heavy-duty mesh"},
    {"id": "eze-breeze", "name": "Eze-Breeze 4-Track Panels", "brand": "Eze-Breeze (PGT)", "type": "Vinyl Sliding Panels", "unit": "per panel",
     "wholesale": 285.00, "retail": 400.00, "offered": 550.00, "notes": "Not screen \u2014 vinyl glazed panels; creates 3-season room; very popular SE US"},
    {"id": "screenmobile-custom", "name": "Screenmobile Custom", "brand": "Screenmobile", "type": "Custom Aluminum Frame", "unit": "per SF",
     "wholesale": 4.50, "retail": 9.50, "offered": 14.00, "notes": "Mobile franchise; comes to site; price includes frame + screen + labor"},
    {"id": "aluminum-site-built", "name": "Site-Built Aluminum Frame", "brand": "Custom", "type": "Aluminum Frame + Screen", "unit": "per SF",
     "wholesale": 5.50, "retail": 11.00, "offered": 18.00, "notes": "Contractor-built on-site; most durable; paintable; common for large porches"},
    {"id": "phifer-fiberglass", "name": "Phifer Fiberglass Screen (fabric only)", "brand": "Phifer", "type": "Screen Fabric", "unit": "per SF",
     "wholesale": 0.20, "retail": 0.45, "offered": 0.35, "notes": "Raw screen material; use with Screen Tight/ScreenEze; solar/pet = $0.60-1.20"},
]

# Fix selection if old ID no longer exists
for cat_key in ["decking", "railing", "waterproofing", "screening"]:
    current_sel = selections.get(cat_key, "")
    ids = [p["id"] for p in data["product_options"][cat_key]]
    if current_sel not in ids:
        data["selections"][cat_key] = ids[0]  # default to first

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

for cat in ["decking", "railing", "waterproofing", "screening"]:
    print(f"  {cat}: {len(data['product_options'][cat])} options")
print(f"\nSelections: {data['selections']}")
print("Done!")
