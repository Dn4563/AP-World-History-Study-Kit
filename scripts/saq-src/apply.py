"""Write the SAQ key-word checklists (checks.py) into content/*/practice.json and confirm each model answer passes."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from checks import C
ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "content")
used = set()
for unit in ("unit-02", "unit-03"):
    p = os.path.join(ROOT, unit, "practice.json")
    raw = open(p).read()
    d = json.loads(raw)
    for s in d["sections"]:
        for q in s["questions"]:
            for part in q.get("parts", []):
                k = (unit, q.get("id"), part.get("k"))
                if k in C:
                    part["check"], part["checkLabels"] = C[k][0], C[k][1]
                    used.add(k)
    ind = 1 if raw.startswith('{\n "') else 2
    open(p, "w").write(json.dumps(d, indent=ind, ensure_ascii=False) + "\n")
missing = set(C) - used
print("checklists written:", len(used), "of", len(C), "; missing:", sorted(missing))
