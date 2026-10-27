import json
import re
import sys
from pathlib import Path

p = Path(sys.argv[1])
txt = p.read_text(encoding="utf-8", errors="replace")

print("== img src ==")
for m in re.finditer(r"<img[^>]+>", txt):
    tag = m.group(0)
    src = re.search(r'src="([^"]+)"', tag)
    alt = re.search(r'alt="([^"]*)"', tag)
    print(" -", src.group(1) if src else "?", "| alt:", alt.group(1) if alt else "")

print("== ld+json ==")
for m in re.finditer(r'type="application/ld\+json"[^>]*>(.*?)</script>', txt, re.S):
    try:
        d = json.loads(m.group(1))
        print(json.dumps(d, ensure_ascii=False)[:2500])
    except Exception as e:  # noqa: BLE001
        print("parse err", e, m.group(1)[:300])

print("== img.jiling.cc urls ==")
for u in sorted(set(re.findall(r"https?://img\.jiling\.cc[^\"' )<>]+", txt))):
    print(" *", u)
