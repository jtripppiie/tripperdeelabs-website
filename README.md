# TripperDeeLabs website

Static GitHub Pages site for https://tripperdeelabs.com, published from main at the repository root.

## Catalog

16 public Google Play listings were verified on October 23, 2026 using the US English storefront. `data/apps.json` retains listing URLs, observed prices, icon and screenshot source URLs, and listing descriptions. Pages use editorial summaries in `scripts/build_catalog.py`. Recheck the listings before changing availability, prices, compatibility or features.

Alaska Gold Run and Moments have informational pages but are excluded from the live-app grid: their expected public Play URLs returned 404. Alaska Gold Run's local project README also identifies it as unreleased. Do not add purchase offers or label development assets as Play screenshots without a verified public listing.

Kenai Report Data is a separate Wear OS companion app, not a phone app or watch face; its page links to the existing joint Kenai privacy policy. `/garmin/` now describes the verified Wear OS faces.

## Build and verify

Python 3 with CairoSVG builds static pages and 1200×630 PNG social cards:

```
python3 scripts/build_catalog.py
python3 scripts/check_catalog.py
```

The checker also uses Beautiful Soup and Pillow. GitHub Pages serves the generated HTML directly; these packages are only needed when rebuilding/checking locally. Screenshots and icons are unchanged downloads from the official Play listings. The official Google Play badge is stored locally. Source URLs are in the catalog data.

The sitemap includes all public app, privacy, support and contact pages; draft pages are excluded. `robots.txt` points to the sitemap and retains the existing crawler preferences. Every HTML page has a canonical URL. Published debug APKs have been removed.

## Verification limits

SoftwareApplication JSON-LD includes verified offers, OS, category, image, author and canonical product URL. None of the fetched listings supplied aggregate ratings. Do not fabricate ratings or reviews: Google's software-app rich result requires a genuine rating/review in addition to name and price. Local checks do not substitute for Google's interactive Rich Results Test.

## Email and Search Console

Public DNS inspection on October 23, 2026 found no MX or TXT answers; authoritative nameservers are ns-cloud-e1 through ns-cloud-e4.googledomains.com. This does not establish the registrar or the available account permissions.

No DNS records have been changed. Email routing requires the destination Gmail address and access to the actual DNS/forwarding provider. Obtain that provider's exact MX priorities/targets and any required TXT values, and show the exact additions/removals before applying them. Preserve the website's A/CNAME records.

Search Console domain verification requires an account-issued DNS token. Do not invent one. Once the account supplies its exact `google-site-verification=...` TXT value, publish it at the requested DNS name and verify in Search Console. Alternatively, an account-issued HTML verification file can verify the HTTPS URL-prefix property; it does not verify the domain property. Submit https://tripperdeelabs.com/sitemap.xml after ownership verification.

## Wonder Cascade preparation

`/wonder-cascade/privacy/` covers the current Android AdMob/UMP/Billing integration and the browser feedback preview. The Android internal-test candidate is 0.11.3; real Play purchase testing remains pending. Wonder Cascade is not in the public Play catalog. The root `app-ads.txt` contains the supplied publisher record for `pub-2800097170975983`.

`/wonder-cascade/play/` is the unlisted, noindex browser feedback preview, version 0.16.0-web.1. It includes Strategy Stops every fifth journey level with finite gems and free undo, shorter verified late-level routes, an expanded puzzle library, optional first-clear move previews without spending a move, earned chapter celebrations, a private feedback invitation, a visual first-play introduction, clearer move feedback, puzzle-set celebrations, three daily challenges selected from a verified library with separate saves, polished puzzle cards, six Expert puzzles, responsive phone layouts and eighteen Mind Puzzles with finite gems, one-to-six-move solutions, undo, and separate mastery records. Open Play modes → Mind puzzles. Watch all 18 runs every Mind Puzzle with pause/resume and up to 8× playback; Think ahead → Watch solve starts from an individual puzzle. Computer runs keep personal progress unchanged. It uses the actual Godot game, with no ads, purchases or analytics. Its service worker is scoped to this directory and uses a Wonder Cascade-specific cache prefix. Progress stays in browser storage; feedback opens an email draft only when the player chooses. It is deliberately absent from the app grid and sitemap. Browser compatibility still depends on WebGL 2, WebAssembly, service workers and cross-origin isolation support.

Export source and reproducible staging script live in the adjacent android-chain workspace: `python3 prepare-web-preview.py --stage`. Generated files stay below GitHub's individual file limit. Run the site catalog checker and browser checks before committing updates. Never add signing credentials, APKs or AABs to the website.
