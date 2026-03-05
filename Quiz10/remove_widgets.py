import json

path = "Quiz10.ipynb"   # change if your filename is different
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# remove broken widget metadata
if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=2)

print("Removed metadata.widgets and saved:", path)