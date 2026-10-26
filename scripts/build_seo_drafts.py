"""Build unpublished, noindex review pages without changing production pages."""
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
import html, json
from seo_draft_content import PAGES
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'drafts/seo-review'
BASE = 'https://tripperdeelabs.com'
E = html.escape
apps = {a['slug']: a for a in json.loads((ROOT/'data/apps.json').read_text())}
OUT.mkdir(parents=True, exist_ok=True)
STYLE = '''.seo-copy{max-width:780px}.seo-copy h2{margin-top:2rem}.seo-faq{max-width:780px}.seo-faq h3{margin-top:1.6rem}.screenshots figure{margin:0;flex:0 0 240px}.screenshots figure img{height:auto;width:240px;max-width:100%}.screenshots figcaption{font-size:.85rem;color:#bbcbd4;line-height:1.5;margin-top:10px}.review-note{padding:12px 18px;border:1px solid #8ed8c0;border-radius:8px;margin-top:24px;font-size:.9rem}.app-directory{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,290px),1fr));gap:18px;list-style:none;padding:0}.app-directory li{background:#142a3a;border:1px solid #385064;border-radius:12px;padding:20px}.app-directory strong{display:block}.app-directory p{margin:6px 0 0}.pending{color:#bbcbd4;font-size:.9rem}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}'''
def shell(slug):
 s=BeautifulSoup((ROOT/slug/'index.html').read_text(),'html.parser')
 s.head.append(s.new_tag('meta',attrs={'name':'robots','content':'noindex,follow'}))
 style=s.new_tag('style');style.string=STYLE;s.head.append(style)
 return s

def finish(s,slug):
 note=s.new_tag('aside',attrs={'class':'review-note'})
 note.append(BeautifulSoup('Unpublished review draft · <a href="/drafts/seo-review/">Home draft</a> · <a href="/drafts/seo-review/parked/">Parked draft</a> · <a href="/drafts/seo-review/salmon-tracker/">Salmon Tracker draft</a>', 'html.parser'))
 s.main.insert(0,note)
 path=OUT/slug/'index.html';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(str(s)+'\n')

for slug,c in PAGES.items():
 a=apps[slug];s=shell(slug)
 schema_node=s.select_one('script[type="application/ld+json"]')
 app_schema=json.loads(schema_node.string);app_schema['offers']['price']='0.50'
 if slug=='salmon-tracker':app_schema['name']='Salmon Tracker: Kenai Counts'
 schema_node.string=json.dumps(app_schema)
 s.title.string=c['title']+' | TripperDeeLabs'
 s.select_one('meta[name="description"]')['content']=c['description']
 for selector,value in [('meta[property="og:title"]',c['title']),('meta[name="twitter:title"]',c['title']),('meta[property="og:description"]',c['description']),('meta[name="twitter:description"]',c['description'])]:s.select_one(selector)['content']=value
 s.main.clear()
 body=f'<section class="catalog-hero"><img class="app-icon" src="/assets/apps/{slug}/icon.png" width="112" height="112" alt=""><p class="eyebrow">{E(a["name"])} · Android</p><h1>{E(c["h1"])}</h1><p class="lead">{E(c["intro"])}</p><a class="play-link" href="{E(a["play"])}"><img class="play-badge" src="/assets/google-play-badge.png" width="194" height="75" alt="Get it on Google Play"></a><p class="price">$0.50 USD · US Play listing checked October 26, 2026. Regional price and availability may vary.</p></section>'
 body+='<section aria-label="How it works" class="seo-copy">'+''.join(f'<h2>{E(h)}</h2><p>{E(p)}</p>' for h,p in c['sections'])+'</section>'
 body+='<section><h2>Inside the app</h2><p>Real screenshots from the Google Play listing. Fish counts and dates shown are examples, not current reports.</p><div class="screenshots">' if slug=='salmon-tracker' else '<section><h2>Inside the app</h2><p>Real screenshots from the Google Play listing.</p><div class="screenshots">'
 for i,alt in c['screenshots']:
  src=ROOT/f'assets/apps/{slug}/screenshot-{i}.png';out=OUT/f'assets/{slug}-{i}.webp';out.parent.mkdir(exist_ok=True)
  im=Image.open(src).convert('RGB');im.thumbnail((640,1120));im.save(out,'WEBP',quality=84,method=6)
  url='/drafts/seo-review/assets/'+out.name
  body+=f'<figure><a href="{url}"><img src="{url}" width="{im.width}" height="{im.height}" loading="lazy" decoding="async" alt="{E(alt)}"></a><figcaption>{E(alt)}</figcaption></figure>'
 body+='</div></section><section class="seo-faq"><h2>Frequently asked questions</h2>'
 body+=''.join(f'<h3>{E(q)}</h3><p>{E(ans)}</p>' for q,ans in c['faq'])+'</section>'
 body+=f'<p><a href="{a["privacy"]}">App privacy policy</a> · <a href="/">Studio home</a> · <a href="mailto:feedback@tripperdeelabs.com">Contact support</a></p>'
 s.main.append(BeautifulSoup(body,'html.parser'))
 schema=s.new_tag('script',attrs={'type':'application/ld+json'})
 schema.string=json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':ans}} for q,ans in c['faq']]})
 s.head.append(schema);finish(s,slug)

s=shell('');s.main.clear()
body='<section class="catalog-hero"><p class="eyebrow">Independent Android studio</p><h1>Useful Android apps.<br>Games and watch faces.</h1><p class="lead">TripperDeeLabs makes practical Android apps, offline games, and Wear OS watch faces, with clear privacy information for each product.</p><p><a href="#apps">Find an app</a> · <a href="mailto:feedback@tripperdeelabs.com">feedback@tripperdeelabs.com</a></p></section><section id="apps"><h2>Explore the apps</h2><ul class="app-directory">'
items=[('parked','Parked','Save a parking spot and open directions back to your car.'),('local-lore','Local Lore','Explore nearby history, landmarks, and local stories.'),('roboball','RoboBall','Practice timed basketball shots in an offline arcade game.'),('you-rush-alaska','You Rush Alaska','Coming soon. Not yet available on Google Play.'),('salmon-tracker','Salmon Tracker','Follow Kenai Peninsula salmon passage counts and past seasons.'),('wonder-cascade','Wonder Cascade','A puzzle game in development; public Play availability unconfirmed.'),('private-eyes','Private Eyes','Keep selected photos and files in an offline encrypted vault.'),('moto-thrash','Moto Thrash','Race motocross tracks and build your own courses offline.'),('captain-quack','Captain Quack','Steer through an offline space shooter with local scores.'),('summit-line','Summit Line','A mountain-themed digital watch face for Wear OS.'),('launch-vector','Launch Vector','A rocket countdown watch face with a separate data companion.'),('kenai-fishing-report','Kenai Fishing Report','A Wear OS face for fish counts, river readings, and tides.'),('amelia-navigator','Amelia Navigator','An aviation-style Wear OS face with an aircraft animation.'),('dive-watch','Dive Watch','An analog dive-style Wear OS face; not a dive computer.'),('moments','Moments','A photo watch face project; public Play availability unconfirmed.')]
for slug,name,desc in items:
 url='/drafts/seo-review/'+slug+'/' if slug in PAGES else '/'+slug+'/'
 label=f'<a href="{url}">{E(name)}</a>' if (ROOT/slug/'index.html').exists() else E(name)+' <span class="pending">· Page planned</span>'
 body+=f'<li><strong>{label}</strong><p>{E(desc)}</p></li>'
body+='</ul></section><section><h2>More tools</h2><p><a href="/boss-button/">Boss Button</a> · <a href="/mock-location/">Mock Location</a> · <a href="/kenai-report-data/">Kenai Report Data</a></p></section><section id="about"><h2>About the studio</h2><p>Built by an independent developer. Each app page explains its purpose, connection requirements, and privacy choices, so you can decide whether it fits your needs.</p><p>Questions or feedback? Email <a href="mailto:feedback@tripperdeelabs.com">feedback@tripperdeelabs.com</a>.</p></section>'
s.main.append(BeautifulSoup(body,'html.parser'));finish(s,'')
print('Built home, Parked and Salmon Tracker review drafts. Production files unchanged.')
