"""Generate SQL to seed Supabase from project_data.json"""
import json

with open("project_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def esc(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

lines = []

# 1. Project
p = data["project"]
lines.append(f"""INSERT INTO project (id, name, description, address, contractor, start_date, completion_date)
VALUES ('00000000-0000-0000-0000-000000000001', {esc(p['name'])}, {esc(p['description'])}, {esc(p['address'])}, {esc(p['contractor'])},
  {esc(p['start_date']) if p['start_date'] else 'NULL'}, {esc(p['completion_date']) if p['completion_date'] else 'NULL'});""")

PROJECT_ID = "'00000000-0000-0000-0000-000000000001'"

# 2. Product options (no project_id)
for cat_key, products in data["product_options"].items():
    for i, pr in enumerate(products):
        lines.append(f"""INSERT INTO product_options (category, product_id, name, brand, type, unit, wholesale, retail, offered, notes, sort_order)
VALUES ({esc(cat_key)}, {esc(pr['id'])}, {esc(pr['name'])}, {esc(pr['brand'])}, {esc(pr['type'])}, {esc(pr['unit'])}, {pr['wholesale']}, {pr['retail']}, {pr['offered']}, {esc(pr['notes'])}, {i});""")

# 3. Selections
for cat_key, prod_id in data["selections"].items():
    lines.append(f"""INSERT INTO selections (project_id, category, product_id)
VALUES ({PROJECT_ID}, {esc(cat_key)}, {esc(prod_id)});""")

# 4. Quantities
qty_labels = {
    'deck_sqft': 'Deck area (sq ft)',
    'deck_board_lf': 'Decking boards (linear ft)',
    'railing_lf': 'Railing (linear ft)',
    'underporch_sqft': 'Underporch area (sq ft)',
    'screening_lf': 'Screening perimeter (linear ft)',
    'screen_panels': 'Screen panels (if retractable)',
    'stairs_count': 'Stair sections',
    'stair_treads_lf': 'Stair treads (linear ft)',
}
for key, val in data["quantities"].items():
    label = qty_labels.get(key, key)
    lines.append(f"""INSERT INTO quantities (project_id, key, label, value)
VALUES ({PROJECT_ID}, {esc(key)}, {esc(label)}, {val});""")

# 5. Structural items
for i, item in enumerate(data["structural"]["items"]):
    lines.append(f"""INSERT INTO structural_items (project_id, name, qty, unit, wholesale, retail, offered, sort_order)
VALUES ({PROJECT_ID}, {esc(item['name'])}, {item['qty']}, {esc(item['unit'])}, {item['wholesale']}, {item['retail']}, {item['offered']}, {i});""")

# 6. Labor items
for i, item in enumerate(data["labor"]["items"]):
    lines.append(f"""INSERT INTO labor_items (project_id, name, hours, rate, total, sort_order)
VALUES ({PROJECT_ID}, {esc(item['name'])}, {item['hours']}, {item['rate']}, {item['total']}, {i});""")

# 7. Permit items
for i, item in enumerate(data["permits"]["items"]):
    lines.append(f"""INSERT INTO permit_items (project_id, name, cost, notes, sort_order)
VALUES ({PROJECT_ID}, {esc(item['name'])}, {item['cost']}, {esc(item['notes'])}, {i});""")

# 8. Scope items
for i, item in enumerate(data["out_of_scope"]):
    lines.append(f"""INSERT INTO scope_items (project_id, name, est_cost, notes, sort_order)
VALUES ({PROJECT_ID}, {esc(item['name'])}, {esc(item['est_cost'])}, {esc(item['notes'])}, {i});""")

# 9. Images
for cat in ["current", "rendered"]:
    for i, url in enumerate(data["images"][cat]):
        lines.append(f"""INSERT INTO images (project_id, category, url, sort_order)
VALUES ({PROJECT_ID}, {esc(cat)}, {esc(url)}, {i});""")

sql = "\n".join(lines)
with open("seed.sql", "w", encoding="utf-8") as f:
    f.write(sql)
print(f"Generated {len(lines)} INSERT statements")
