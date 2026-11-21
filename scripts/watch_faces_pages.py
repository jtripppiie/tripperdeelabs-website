"""Watch-face collection, backed by current Play evidence in data/watch-faces.json."""
from pathlib import Path
from html import escape as E
import json
ROOT=Path(__file__).resolve().parents[1]
def build(page):
 faces=json.loads((ROOT/'data/watch-faces.json').read_text())
 cards=[]
 zodiac_cards=[]
 for i,f in enumerate(faces):
  price=('Free, no ads' if f['price']=='0' else '$0.99, no ads') if f['available'] else 'Planned: $0.99, no ads'
  action=f'<a class="watch-play" href="{E(f["play"])}" aria-label="Get {E(f["name"])} on Google Play">Get it on Google Play</a>' if f['available'] else '<span class="watch-coming">Google Play coming soon</span>'
  (zodiac_cards if f.get('collection')=='zodiac' else cards).append(f'''<article class="watch-card" id="{E(f['id'])}"><div class="watch-art"><img src="{E(f['image'])}" width="512" height="512" loading="{'eager' if i<3 else 'lazy'}" alt="{E(f['name'])} watch face"></div><div class="watch-card-copy"><h3>{E(f['name'])}</h3><p class="watch-description">{E(f['description'])}</p><p class="watch-price">{price}</p>{action}<a class="watch-policy" href="{E(f['privacy'])}">Privacy policy</a></div></article>''')
 body='''<link rel="stylesheet" href="/watch-faces.css"><section class="watch-hero"><p class="eyebrow">TRIPPERDEELABS · WEAR OS</p><h1>Watch Faces</h1><p class="lead">Celestial zodiac scenes, snowy villages, neon nights and everyday classics. Find a face that feels like you.</p><p>Original designs. No ads. Explore the new <a href="#zodiac">zodiac collection</a>, or browse the collection below for available Google Play links.</p></section><section id="zodiac" aria-labelledby="zodiac-heading"><h2 id="zodiac-heading">Written in the stars</h2><p class="lead">Twelve signs. Twelve distinct scenes.</p><p>Coming soon for Wear OS 5 and later: original celestial artwork, sign-inspired quotes and traits, and individual ways to show your steps and battery. Cancer and Pisces also feature a live moon phase.</p><p>Planned at $0.99 each, with no ads or in-app purchases. These previews show the watch faces running on a Wear OS emulator.</p><div class="watch-grid">'''+''.join(zodiac_cards)+'''</div></section><section aria-labelledby="collection-heading"><h2 id="collection-heading">More watch faces</h2><div class="watch-grid" aria-label="Watch face collection">'''+''.join(cards)+'''</div></section><section class="watch-notes"><h2>Made for your Wear OS watch</h2><p>Check each Play listing for supported Wear OS versions and features. These faces are not for Apple Watch or Garmin. Steps, heart rate, weather and other readings depend on your watch and selected providers.</p><p>Kenai and Launch Vector use separate companion apps for their report and launch data. Moments uses the supported watch and paired-phone photo flow.</p><p>Prices shown are US prices checked November 20, 2026. Local pricing and availability are shown by Google Play. Launch Vector is currently free. Puppy Time and the zodiac collection are coming soon; planned prices are not live offers.</p><p><a href="/privacy/watch-faces/">Watch Faces Privacy Policy</a> · <a href="mailto:tripperdeelabs@gmail.com">Support</a></p></section>'''
 page('/watch-faces/','Watch Faces','Explore original TripperDeeLabs Wear OS watch faces: Christmas villages, neon racing dials, photo faces and a new zodiac collection coming soon. No ads.',body)
 # The standalone renderer retains the same accessibility enhancement as the full catalog build.
 p=ROOT/'watch-faces/index.html';s=p.read_text().replace('<body>','<body><a class="skip-link" href="#main-content">Skip to main content</a>').replace('<main class="wrap">','<main id="main-content" tabindex="-1" class="wrap">');p.write_text(s)
if __name__=='__main__':
 from page_template import page
 build(page)
