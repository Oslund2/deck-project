"""Deck Replacement Cost Calculator — FastAPI backend."""

from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json
import os
import shutil

app = FastAPI(title="Deck Cost Calculator")
app.mount("/static", StaticFiles(directory="static"), name="static")

DATA_FILE = "project_data.json"
IMAGES_DIR = "static/images"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return get_default_data()


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_default_data():
    return {
        "project": {
            "name": "Deck Replacement & Screened Underporch",
            "description": "Full tear-off and replacement of existing deck with water-tight decking system and screened-in underporch below.",
            "address": "",
            "contractor": "",
            "start_date": "",
            "completion_date": "",
        },
        "images": {
            "current": [],
            "rendered": [],
        },
        "product_options": {
            "decking": [
                {
                    "id": "trex-enhance",
                    "name": "Trex Enhance",
                    "brand": "Trex",
                    "type": "Composite",
                    "unit": "per LF",
                    "wholesale": 2.80,
                    "retail": 4.50,
                    "offered": 3.40,
                    "notes": "Budget-friendly composite, 25-year warranty",
                },
                {
                    "id": "trex-transcend",
                    "name": "Trex Transcend",
                    "brand": "Trex",
                    "type": "Composite",
                    "unit": "per LF",
                    "wholesale": 4.20,
                    "retail": 6.75,
                    "offered": 5.10,
                    "notes": "Premium composite, superior fade/stain resistance",
                },
                {
                    "id": "timbertech-azek",
                    "name": "TimberTech AZEK Vintage",
                    "brand": "TimberTech",
                    "type": "PVC",
                    "unit": "per LF",
                    "wholesale": 5.50,
                    "retail": 8.25,
                    "offered": 6.60,
                    "notes": "Top-tier PVC, lifetime fade & stain warranty",
                },
                {
                    "id": "fiberon-goodlife",
                    "name": "Fiberon Good Life",
                    "brand": "Fiberon",
                    "type": "Composite",
                    "unit": "per LF",
                    "wholesale": 2.50,
                    "retail": 4.00,
                    "offered": 3.10,
                    "notes": "Value composite option, stain resistant",
                },
            ],
            "railing": [
                {
                    "id": "trex-select-rail",
                    "name": "Trex Select Railing",
                    "brand": "Trex",
                    "type": "Composite",
                    "unit": "per LF",
                    "wholesale": 18.00,
                    "retail": 32.00,
                    "offered": 24.00,
                    "notes": "Classic composite rail system",
                },
                {
                    "id": "trex-signature-rail",
                    "name": "Trex Signature Aluminum",
                    "brand": "Trex",
                    "type": "Aluminum",
                    "unit": "per LF",
                    "wholesale": 28.00,
                    "retail": 45.00,
                    "offered": 35.00,
                    "notes": "Sleek aluminum, low profile",
                },
                {
                    "id": "cable-rail",
                    "name": "Stainless Cable Railing",
                    "brand": "Feeney",
                    "type": "Cable",
                    "unit": "per LF",
                    "wholesale": 35.00,
                    "retail": 55.00,
                    "offered": 42.00,
                    "notes": "Modern look, unobstructed views",
                },
            ],
            "waterproofing": [
                {
                    "id": "dryspace",
                    "name": "DrySpace Under-Deck System",
                    "brand": "DrySpace",
                    "type": "Ceiling Panel",
                    "unit": "per SF",
                    "wholesale": 3.50,
                    "retail": 6.00,
                    "offered": 4.50,
                    "notes": "Vinyl ceiling panels, integrated gutter",
                },
                {
                    "id": "underdeck",
                    "name": "UnderDeck Drainage",
                    "brand": "UnderDeck",
                    "type": "Trough System",
                    "unit": "per SF",
                    "wholesale": 2.75,
                    "retail": 4.50,
                    "offered": 3.50,
                    "notes": "Aluminum trough between joists",
                },
                {
                    "id": "zip-deck",
                    "name": "ZIP System Deck Tape",
                    "brand": "Huber",
                    "type": "Membrane",
                    "unit": "per SF",
                    "wholesale": 1.25,
                    "retail": 2.00,
                    "offered": 1.60,
                    "notes": "Joist-level waterproof membrane",
                },
            ],
            "screening": [
                {
                    "id": "screen-tight",
                    "name": "Screen Tight Original",
                    "brand": "Screen Tight",
                    "type": "Porch Screen System",
                    "unit": "per LF",
                    "wholesale": 3.00,
                    "retail": 5.50,
                    "offered": 4.00,
                    "notes": "Standard porch screening system",
                },
                {
                    "id": "screeneze",
                    "name": "ScreenEze Pro",
                    "brand": "ScreenEze",
                    "type": "Porch Screen System",
                    "unit": "per LF",
                    "wholesale": 4.50,
                    "retail": 7.50,
                    "offered": 5.75,
                    "notes": "No-spline system, easier maintenance",
                },
                {
                    "id": "phantom-retractable",
                    "name": "Phantom Retractable Screens",
                    "brand": "Phantom",
                    "type": "Retractable",
                    "unit": "per unit",
                    "wholesale": 350.00,
                    "retail": 600.00,
                    "offered": 475.00,
                    "notes": "Motorized retractable, premium option",
                },
            ],
        },
        "selections": {
            "decking": "trex-transcend",
            "railing": "trex-signature-rail",
            "waterproofing": "dryspace",
            "screening": "screen-tight",
        },
        "quantities": {
            "deck_sqft": 400,
            "deck_board_lf": 1200,
            "railing_lf": 85,
            "underporch_sqft": 400,
            "screening_lf": 75,
            "screen_panels": 0,
            "stairs_count": 1,
            "stair_treads_lf": 36,
        },
        "structural": {
            "items": [
                {"name": "Pressure-treated joists (2x10x12)", "qty": 28, "wholesale": 14.50, "retail": 22.00, "offered": 17.50, "unit": "each"},
                {"name": "Beam lumber (2x10 doubled)", "qty": 4, "wholesale": 18.00, "retail": 28.00, "offered": 22.00, "unit": "each"},
                {"name": "6x6 posts", "qty": 6, "wholesale": 28.00, "retail": 42.00, "offered": 34.00, "unit": "each"},
                {"name": "Post bases / brackets", "qty": 6, "wholesale": 12.00, "retail": 22.00, "offered": 16.00, "unit": "each"},
                {"name": "Joist hangers", "qty": 56, "wholesale": 1.80, "retail": 3.50, "offered": 2.40, "unit": "each"},
                {"name": "Ledger board + flashing", "qty": 1, "wholesale": 85.00, "retail": 140.00, "offered": 110.00, "unit": "lot"},
                {"name": "Concrete footings/piers", "qty": 6, "wholesale": 45.00, "retail": 75.00, "offered": 58.00, "unit": "each"},
                {"name": "Structural screws & hardware", "qty": 1, "wholesale": 180.00, "retail": 280.00, "offered": 220.00, "unit": "lot"},
                {"name": "Hidden fastener system", "qty": 1, "wholesale": 220.00, "retail": 350.00, "offered": 275.00, "unit": "lot"},
            ],
        },
        "labor": {
            "items": [
                {"name": "Demo & haul-off (existing deck)", "hours": 16, "rate": 65.00, "total": 1040.00},
                {"name": "Framing & structural", "hours": 32, "rate": 75.00, "total": 2400.00},
                {"name": "Decking installation", "hours": 24, "rate": 70.00, "total": 1680.00},
                {"name": "Railing installation", "hours": 12, "rate": 70.00, "total": 840.00},
                {"name": "Waterproofing system install", "hours": 16, "rate": 70.00, "total": 1120.00},
                {"name": "Underporch screening", "hours": 12, "rate": 65.00, "total": 780.00},
                {"name": "Stair build & install", "hours": 8, "rate": 75.00, "total": 600.00},
                {"name": "Electrical rough-in (fan/lights)", "hours": 6, "rate": 85.00, "total": 510.00},
                {"name": "Final trim & punch list", "hours": 8, "rate": 65.00, "total": 520.00},
            ],
        },
        "permits": {
            "items": [
                {"name": "Building permit", "cost": 350.00, "notes": "Required — structural deck replacement"},
                {"name": "Electrical permit", "cost": 125.00, "notes": "If adding fan/lights to underporch"},
                {"name": "HOA architectural review", "cost": 0.00, "notes": "Check if applicable — may require submittal"},
                {"name": "Engineering / load calcs", "cost": 400.00, "notes": "May be required by municipality for underporch"},
            ],
        },
        "out_of_scope": [
            {"name": "Landscaping repair / grading", "est_cost": "500 - 1,500", "notes": "Ground disturbance around footings may need landscape restoration"},
            {"name": "Gutter / downspout reroute", "est_cost": "300 - 800", "notes": "If waterproofing system requires new drainage path"},
            {"name": "Ceiling fan + light fixtures", "est_cost": "200 - 600", "notes": "Fixture cost only — electrical labor included if permit pulled"},
            {"name": "Underporch flooring (pavers/concrete)", "est_cost": "1,500 - 4,000", "notes": "Existing surface may need improvement for living space use"},
            {"name": "Outdoor furniture / furnishings", "est_cost": "Varies", "notes": "Not part of construction scope"},
            {"name": "Pest / termite treatment", "est_cost": "200 - 500", "notes": "Recommended before closing in underporch"},
            {"name": "Paint / stain on structural lumber", "est_cost": "300 - 600", "notes": "PT lumber can be left natural or painted — add-on if desired"},
            {"name": "Pergola or shade structure", "est_cost": "2,000 - 8,000", "notes": "Popular add-on for upper deck"},
        ],
    }


@app.get("/")
async def index():
    return FileResponse("static/index.html")


@app.get("/api/data")
async def get_data():
    return load_data()


@app.post("/api/data")
async def update_data(data: dict):
    save_data(data)
    return {"ok": True}


@app.post("/api/images/{category}")
async def upload_image(category: str, file: UploadFile = File(...)):
    if category not in ("current", "rendered"):
        return {"error": "Invalid category"}
    os.makedirs(f"{IMAGES_DIR}/{category}", exist_ok=True)
    path = f"{IMAGES_DIR}/{category}/{file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    data = load_data()
    img_url = f"/static/images/{category}/{file.filename}"
    if img_url not in data["images"][category]:
        data["images"][category].append(img_url)
        save_data(data)
    return {"url": img_url}


@app.delete("/api/images/{category}/{filename}")
async def delete_image(category: str, filename: str):
    path = f"{IMAGES_DIR}/{category}/{filename}"
    if os.path.exists(path):
        os.remove(path)
    data = load_data()
    img_url = f"/static/images/{category}/{filename}"
    if img_url in data["images"].get(category, []):
        data["images"][category].remove(img_url)
        save_data(data)
    return {"ok": True}
