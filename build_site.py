#!/usr/bin/env python3
"""Regenerate the AnchorFare website (index.html) from deals.json.

Refresh flow for the every-two-day price re-check:
  1. Update deals.json with the new verified prices/deals (same shape:
     windows a/b/c, each with title, range, deals[], also[]).
  2. Run:  python3 build_site.py
  3. Commit + push index.html and deals.json — GitHub Pages rebuilds.

The page design lives in template.html; only the deal data is injected.
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).parent

def main() -> int:
    deals = json.loads((HERE / "deals.json").read_text(encoding="utf-8"))
    windows = deals["windows"]
    template = (HERE / "template.html").read_text(encoding="utf-8")
    if "__DEALS_JSON__" not in template:
        print("ERROR: template.html is missing the __DEALS_JSON__ placeholder", file=sys.stderr)
        return 1
    injected = json.dumps(windows, ensure_ascii=False, indent=2)
    html = template.replace("__DEALS_JSON__", injected, 1)
    (HERE / "index.html").write_text(html, encoding="utf-8")
    total = sum(len(w["deals"]) for w in windows.values())
    also = sum(len(w.get("also", [])) for w in windows.values())
    print(f"index.html written: {len(html)} bytes | {total} featured deals, {also} also-tracked | data updated {deals.get('updated')}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
