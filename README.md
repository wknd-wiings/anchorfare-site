# AnchorFare — website (anchorfare.com)

Static site served by GitHub Pages from this repo (`wknd-wiings/anchorfare-site`),
custom domain `anchorfare.com` (see `CNAME`). It mirrors the AnchorFare cruise
deal tracker so anyone — including Android users, who have no app at launch —
can reach the deals. Skin: Golden Age Liner (navy / cream / coral).

## Files
- `index.html` — the published page. **Generated** by `build_site.py`; do not hand-edit.
- `template.html` — the page design (Golden Age Liner skin, hero, Gold Strike
  Fly & Sail panel, window switcher, games strip, footer).
- `deals.json` — the deal data (windows a/b/c: featured deals + also-tracked),
  exactly as shown in the tracker.
- `build_site.py` — injects `deals.json` into `template.html` → `index.html`.

## Refreshing prices (every-two-day re-check)
1. Update `deals.json` with the newly verified prices/deals (keep the shape).
2. Run `python3 build_site.py`.
3. Commit and push `index.html` + `deals.json`. Pages rebuilds automatically.
