# TripperDeeLabs website

Static GitHub Pages site for https://tripperdeelabs.com, published from main at the repository root.

## Catalog

Historical baseline: 16 public Google Play listings were verified on October 23, 2026 using the US English storefront. See the October 26 rollout below for current availability and prices. `data/apps.json` retains listing URLs, observed prices, icon and screenshot source URLs, and listing descriptions. Pages use editorial summaries in `scripts/build_catalog.py`. Recheck the listings before changing availability, prices, compatibility or features.

Alaska Gold Run has a full homepage game card and SEO page. The owner confirmed Play Console status ‘Changes in review,’ last updated October 24, 2026, for com.tripperdeelabs.alaskagoldrun. Its public listing is not available yet. Real desktop gameplay captures come from the release-preparation assets; see assets/apps/alaska-gold-run/provenance.json. Moments remains a development preview. Do not add purchase offers or label development assets as Play screenshots without a verified public listing.

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

`/wonder-cascade/privacy/` covers the current Android AdMob/UMP/Billing integration and the browser feedback preview. The Android internal-test candidate is 0.11.3; real Play purchase testing remains pending. Wonder Cascade is not in the public Play catalog; `/wonder-cascade/` is an informational development-preview page. The root `app-ads.txt` contains the supplied publisher record for `pub-2800097170975983`.

`/wonder-cascade/play/` is the unlisted, noindex browser feedback preview, version 0.20.0-web.1. The latest update adds compact level recipes through stage 200, continuing seeded variations afterward, a consistent computer-run board scale, updated animations, and a smaller exported game pack (about 9 MB). It includes Strategy Stops every fifth journey level with finite gems and free undo, shorter verified late-level routes, an expanded puzzle library, optional first-clear move previews without spending a move, earned chapter celebrations, a private feedback invitation, a visual first-play introduction, clearer move feedback, puzzle-set celebrations, three daily challenges selected from a verified library with separate saves, polished puzzle cards, six Expert puzzles, responsive phone layouts and eighteen Mind Puzzles with finite gems, one-to-six-move solutions, undo, and separate mastery records. Open Play modes → Mind puzzles. Watch all 18 runs every Mind Puzzle with pause/resume and up to 28× playback; Think ahead → Watch solve starts from an individual puzzle. Computer runs keep personal progress unchanged. It uses the actual Godot game, with no ads, purchases or analytics. Its service worker is scoped to this directory and uses a Wonder Cascade-specific cache prefix. Progress stays in browser storage; feedback opens an email draft only when the player chooses. It is deliberately absent from the app grid and sitemap. Browser compatibility still depends on WebGL 2, WebAssembly, service workers and cross-origin isolation support.

Export source and reproducible staging script live in the adjacent android-chain workspace: `python3 prepare-web-preview.py --stage`. Generated files stay below GitHub's individual file limit. Run the site catalog checker and browser checks before committing updates. Never add signing credentials, APKs or AABs to the website.

## Website analytics

Google Analytics measurement ID: `G-77H5RENPZ3`. Generated home, catalog and product landing pages load `/cookie-consent.js` with `defer`. That script loads Google's tag only after the visitor accepts optional analytics; declining or withdrawing consent disables measurement. Keep this loader in `scripts/build_catalog.py`, not just generated HTML. The catalog checker verifies coverage and rejects direct Google-tag loading on these landing pages. Preserve explicit no-analytics promises on app privacy pages.

On October 26, 2026, the live homepage and Moto Thrash page were confirmed to omit the consent loader even though the live JavaScript contained the correct ID. The generator was corrected locally; a local fix alone does not establish deployment or data receipt.

After authorized publication, check the live HTML and JavaScript, then use a browser without an analytics blocker: accept analytics, visit a product page, and inspect requests to Google's `g/collect` endpoint for the correct measurement ID. Check the matching property's Realtime report; ordinary reports can take 24–48 hours. Declined visits are intentionally not measured. Never interpret the optional third-party visitor counter as the GA4 total. See [Google's troubleshooting guide](https://developers.google.com/analytics/devguides/collection/ga4/troubleshoot).

## Private Eyes guides

The expanded product page and four Android privacy guides are generated by `scripts/private_eyes_content.py`, called from `scripts/build_catalog.py`. The guides cover hiding versus encryption, removing originals, direct private capture and device-loss recovery limits. The guide index and articles are included in the sitemap; noindex previews remain excluded. Content describes current released features and does not advertise the unreleased 0.10.0 albums update. Verified locally with the catalog checker and 36 page/heading/overflow checks across phone and desktop layouts; screenshots were reviewed.

## Web SEO rollout (October 26, 2026)

The owner approved the home/Parked/Salmon Tracker direction and publication of
all pages. Canopy Quest stays in the directory with its description, features,
screenshots and privacy link intact, prominently labeled **Under maintenance**.
Its unavailable Play link and price offer are omitted. You Rush Alaska has a
coming-soon page at `/you-rush-alaska/`; the existing `/alaska-rush/privacy/`
route stays in place. Its exact product assets have not been confirmed.

The approved detailed landing pages are generated by `scripts/seo_pages.py`
from `scripts/seo_content.py` and the reviewed pilot copy in
`scripts/seo_draft_content.py`. The main catalog generator calls this renderer
before rebuilding the sitemap. Do not edit generated pages alone.

```
python3 scripts/build_catalog.py
python3 scripts/check_catalog.py
python3 scripts/check_seo.py
```

Fourteen detailed pages contain 300–600 words, matching visible FAQs and FAQPage
schema, canonical tags and compressed WebP screenshots. Available apps include
verified Play badges and SoftwareApplication offers. Wonder Cascade and Moments
have informative preview pages with labeled development screenshots; no public
Play listings, prices or purchase offers are invented. You Rush Alaska deliberately
remains a short coming-soon notice until its product assets are confirmed.

US storefront checks on October 26 found 15 catalog listings available: paid
listings show $0.50, while Local Lore, Launch Vector and Kenai Report Data are free.
Canopy Quest's known listing returns 404 and is under maintenance per the owner.
Do not interpret the old catalog total of 16 as 16 currently available apps.
`data/apps.json` records the current observed status, price and check date.

The original review artifacts remain local under ignored `drafts/seo-review/`.
They are not published. The source builder is retained for review reproducibility.
Current validation and remaining Search Console setup are recorded in
`SEO-REPORT.txt`. Publication status must be verified against GitHub Pages and
live HTML; a local build is not evidence of deployment.

Google discontinued FAQ rich results in May 2026. The requested FAQPage schema
remains useful machine-readable content, but no FAQ search enhancement, ranking,
or steady traffic is promised. See https://developers.google.com/search/updates.

Homepage app cards now use compressed, lazy-loaded real screenshot previews,
generated as `assets/apps/<app>/home-preview.webp`. Keep availability labels
visible with the imagery; You Rush Alaska has a coming-soon panel until its
product artwork is confirmed.

Homepage cards show exactly one useful descriptive paragraph per item, with
images, category headings, availability labels and links. Keep detailed features
and connection/storage limits on the app landing pages. Preserve the studio
description and personal introduction; do not reduce summaries to mere titles.

The homepage Wear OS companion section uses a dedicated two-column feature
layout with CSS-framed close-ups of actual Kenai Report Data screens. The
source captures remain unchanged; phone layouts show one readable watch view.

Preserve the studio identity during SEO/layout edits: the original fox-scientist
logo (`assets/tripperdeelabs-logo.png`) belongs in navigation and prominently in
the home hero. Keep “Doing TripperDee things in a TripperDee world.” and the
first-person independent-developer introduction. SEO work is not permission to
remove the owner’s branding, personal copy, or existing useful app information.

## Search, answer discovery, and accessibility

The October 26 pass added stable Organization/WebSite/WebPage identity markup,
visible breadcrumbs with matching structured data, app publisher references, and
linkable FAQ answers. Public content remains static HTML and readable with
JavaScript disabled. Existing robots rules allow search/retrieval crawlers while
retaining the separate training-crawler restrictions. No ranking or AI-citation
guarantee is implied; Search Console verification and account settings remain
unconfirmed.

All 55 public pages have a keyboard skip link. Shared styles provide visible
focus, enlarged navigation targets, reduced-motion support, and wrapping for
large text. Cookie controls are in the document flow, with settings in the
footer, to avoid covering content or keyboard focus. Keep policy prose intact
when changing shared navigation. Run `python3 scripts/check_seo.py` as well as
the catalog check after builds. Browser accessibility checks supplement these
checks; they do not establish full WCAG conformance or screen-reader usability.

## Stick Sprint — October 27, 2026

Coming-soon game page, app-specific privacy policy and support guide: `/stick-sprint/`, `/stick-sprint/privacy/`, `/stick-sprint/support/`. Sources: `seo_content.py`, `seo_pages.py`, `stick_sprint_pages.py`. No Play availability, price, ratings or release date claimed. Development screenshots and provenance are in `assets/apps/stick-sprint/`. Preserve these sources when regenerating the site.
