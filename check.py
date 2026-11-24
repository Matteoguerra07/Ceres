#!/usr/bin/env python3

import json, sys
from pathlib import Path
from build import VARIANTS, SYN, TRAFFIC


def lum(h):
    h = h.lstrip("#")[:6]
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


bad = 0
for slug, p in VARIANTS.items():
    path = Path("themes") / f"{slug}-color-theme.json"
    json.loads(path.read_text())  # solleva se il JSON e' rotto
    print(f"\n{p['label']}  (editor {p['bg1']})")
    checks = {"testo": p["fg"], "commenti": p["mute"], "num.riga": p["dim"], "accento": p["accent"]}
    checks |= {k: v for k, v in SYN.items()} | {f"semaforo-{k}": v for k, v in TRAFFIC.items()}
    for name, col in checks.items():
        r = ratio(col, p["bg1"])
        floor = 3.0 if name == "num.riga" else 4.5
        flag = "" if r >= floor else "  <-- BASSO"
        bad += bool(flag)
        print(f"  {name:16s} {col}  {r:5.2f}{flag}")
    # sidebar e tab inattive (testo mute su bg2/bg0)
    for lbl, fg, bg in [("sidebar", p["mute"], p["bg2"]), ("tab inatt.", p["mute"], p["bg0"]),
                        ("selezione", p["fg"], p["bg3"])]:
        r = ratio(fg, bg)
        flag = "" if r >= 4.5 else "  <-- BASSO"
        bad += bool(flag)
        print(f"  {lbl:16s} {r:5.2f}{flag}")
print(f"\nproblemi: {bad}")
sys.exit(1 if bad else 0)
