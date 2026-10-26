"""Render the approved SEO pages using the site's existing static shell."""
from pathlib import Path
from html import escape as E
import json
from PIL import Image
from seo_content import PAGES
ROOT=Path(__file__).resolve().parents[1]
BASE='https://tripperdeelabs.com'

def gallery(slug,shots,development=False):
 body='<section><h2>Inside the app</h2><p>'+('Development-build screenshots; features may change before release.' if development else ('Real app screenshots. Displayed dates, counts, and readings are examples, not live reports.' if slug in ['salmon-tracker','kenai-fishing-report','launch-vector'] else 'Real app screenshots.'))+'</p><div class="screenshots">'
 for i,alt in shots:
  folder=ROOT/'assets/apps'/slug;src=folder/f'screenshot-{i}.png';out=folder/f'screenshot-{i}.webp'
  im=Image.open(src).convert('RGB');im.thumbnail((960,1120));im.save(out,'WEBP',quality=84,method=6)
  url=f'/assets/apps/{slug}/screenshot-{i}.webp'
  body+=f'<figure><a href="{url}"><img src="{url}" width="{im.width}" height="{im.height}" loading="lazy" decoding="async" alt="{E(alt)}"></a><figcaption>{E(alt)}</figcaption></figure>'
 return body+'</div></section>'

def build(page,apps,badge,copy):
 lookup={a['slug']:a for a in apps}
 for slug,c in PAGES.items():
  a=lookup.get(slug);upcoming=a is None
  name=a['name'] if a else {'moments':'Moments','wonder-cascade':'Wonder Cascade'}[slug]
  os=a['os'] if a else ('Wear OS 6 or newer' if slug=='moments' else 'Android')
  # Prices in FAQ answers follow the verified catalog rather than frozen draft prices.
  faqs=[(q,ans.replace('$0.50', '$'+a['price']) if a else ans) for q,ans in c['faq']]
  app_schema={'@context':'https://schema.org','@type':'SoftwareApplication','name':name,'operatingSystem':os,'url':BASE+'/'+slug+'/','applicationCategory':a['category'] if a else ('GameApplication' if slug=='wonder-cascade' else 'UtilitiesApplication')}
  if a:app_schema.update(offers={'@type':'Offer','price':a['price'],'priceCurrency':a['currency'],'url':a['play']},installUrl=a['play'])
  faq_schema={'@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':ans}} for q,ans in faqs]}
  schema={'@context':'https://schema.org','@graph':[app_schema,faq_schema]}
  icon=f'/assets/apps/{slug}/icon.png'
  body='<section class="catalog-hero">'
  if (ROOT/icon.lstrip('/')).exists():
   im=Image.open(ROOT/icon.lstrip('/')).convert('RGBA');im.thumbnail((224,224))
   icon=icon.replace('.png','.webp');im.save(ROOT/icon.lstrip('/'),'WEBP',quality=85,method=6)
   body+=f'<img class="app-icon" src="{icon}" width="112" height="112" alt="">'
  body+=f'<p class="eyebrow">{E(name)} · {E(os)}</p>'
  if upcoming:body+='<p class="availability">In development · Public Play listing unavailable</p>'
  body+=f'<h1>{E(c["h1"])}</h1><p class="lead">{E(c["intro"])}</p>'
  if a:body+=badge(a)+f'<p class="price">'+('Free' if float(a['price'])==0 else '$'+a['price']+' USD')+f' · US Play listing checked {a["verified"]}. Regional price and availability may vary.</p>'
  body+='</section><section class="seo-copy" aria-label="How it works">'+''.join(f'<h2>{E(h)}</h2><p>{E(p)}</p>' for h,p in c['sections'])+'</section>'
  body+=gallery(slug,c['screenshots'],upcoming)
  body+='<section class="seo-faq"><h2>Frequently asked questions</h2>'+''.join(f'<h3>{E(q)}</h3><p>{E(ans)}</p>' for q,ans in faqs)+'</section>'
  if slug=='private-eyes':
   from private_eyes_content import links
   body+='<section><h2>Android photo privacy guides</h2>'+links()+'</section>'
  if slug=='kenai-fishing-report':body+='<p><a href="/kenai-report-data/">Kenai Report Data companion app</a></p>'
  body+=f'<p><a href="/{slug}/privacy/">App privacy policy</a> · <a href="/">Studio home</a> · <a href="mailto:feedback@tripperdeelabs.com">Contact support</a></p>'
  page('/'+slug+'/',c['title'],c['description'],body,BASE+f'/assets/apps/{slug}/social.png',schema)
 # Preserve the game information while making availability unmistakable.
 a=lookup['canopy-quest'];title,p1,p2,features=copy['canopy-quest']
 body=f'<section class="catalog-hero"><p class="eyebrow">Canopy Quest</p><p class="availability">Under maintenance</p><h1>{E(title)}</h1><p>{E(p1)}</p><p>{E(p2)}</p><p>Canopy Quest is currently under maintenance. The game information and screenshots remain here for reference; downloads are unavailable at present.</p></section><section><h2>Features</h2><ul>'+''.join(f'<li>{E(f)}</li>' for f in features)+'</ul></section>'
 body+=gallery('canopy-quest',[(1,'Canopy Quest jungle platformer at a saved camp with ladder controls'),(2,'Canopy Quest Moonlit Basin with platforms, water, and a vine'),(3,'Canopy Quest ladder route toward Starlight Camp'),(4,'Canopy Quest Sun Temple platforms with water and ladder')])
 body+='<p><a href="/canopy-quest/privacy/">App privacy policy</a> · <a href="/">Studio home</a> · <a href="mailto:feedback@tripperdeelabs.com">Contact support</a></p>'
 page('/canopy-quest/',title+' — Under maintenance','Canopy Quest is under maintenance. Read about its offline jungle platforming, field map, camps and local progress, and view screenshots and privacy details.',body,BASE+'/assets/apps/canopy-quest/social.png',{'@context':'https://schema.org','@type':'SoftwareApplication','name':a['name'],'operatingSystem':a['os'],'applicationCategory':a['category'],'url':BASE+'/canopy-quest/'})
 # No claimed features or screenshots for an identity not yet verified against assets.
 page('/you-rush-alaska/','You Rush Alaska — Coming soon','You Rush Alaska is coming soon from TripperDeeLabs. Check this page for release information, read the existing Alaska Rush privacy policy, or contact us.', '<section class="catalog-hero"><p class="eyebrow">TripperDeeLabs · In development</p><h1>You Rush Alaska — Coming soon</h1><p>This app is not yet available on Google Play. We will add release information and a verified download link here when it is ready.</p><p>No release date or price has been announced on this page.</p></section><section><h2>Questions about the project?</h2><p>Email <a href="mailto:feedback@tripperdeelabs.com">feedback@tripperdeelabs.com</a> for questions or feedback.</p><p><a href="/alaska-rush/privacy/">Existing Alaska Rush privacy policy</a> · <a href="/">Studio home</a></p></section>')
 # Home follows the approved editorial directory and includes all requested products.
 labels={'parked':'Parked','local-lore':'Local Lore','roboball':'RoboBall','you-rush-alaska':'You Rush Alaska','salmon-tracker':'Salmon Tracker','wonder-cascade':'Wonder Cascade','private-eyes':'Private Eyes','moto-thrash':'Moto Thrash','captain-quack':'Captain Quack','summit-line':'Summit Line','launch-vector':'Launch Vector','kenai-fishing-report':'Kenai Fishing Report','amelia-navigator':'Amelia Navigator','dive-watch':'Dive Watch','moments':'Moments','canopy-quest':'Canopy Quest'}
 body='<section class="catalog-hero"><p class="eyebrow">Independent Android studio</p><h1>Useful Android apps.<br>Games and watch faces.</h1><p class="lead">TripperDeeLabs makes practical Android apps, offline games, and Wear OS watch faces, with clear privacy information for each product.</p><p><a href="#apps">Find an app</a> · <a href="mailto:feedback@tripperdeelabs.com">feedback@tripperdeelabs.com</a></p></section><section id="apps"><h2>Explore the apps</h2><ul class="app-directory">'
 for slug,label in labels.items():
  desc=PAGES[slug]['h1'] if slug in PAGES else ('Release information will appear here when ready.' if slug=='you-rush-alaska' else 'Offline jungle platforming with a field map and camp saves.')
  status={'canopy-quest':'Under maintenance','you-rush-alaska':'Coming soon','wonder-cascade':'In development','moments':'In development'}.get(slug)
  preview=''
  if slug!='you-rush-alaska':
   index,alt=(PAGES[slug]['screenshots'][0] if slug in PAGES else (1,'Canopy Quest jungle platformer at a saved camp'))
   # Favor the close-up watch captures where supplied by the actual listing.
   if slug in ['summit-line','kenai-fishing-report','parked']:
    index,alt=PAGES[slug]['screenshots'][-1]
   source=ROOT/f'assets/apps/{slug}/screenshot-{index}.png'
   thumb=ROOT/f'assets/apps/{slug}/home-preview.webp'
   im=Image.open(source).convert('RGB');im.thumbnail((640,480));im.save(thumb,'WEBP',quality=82,method=6)
   preview=f'<a class="directory-preview" href="/{slug}/" tabindex="-1"><img src="/assets/apps/{slug}/home-preview.webp" width="{im.width}" height="{im.height}" alt="{E(alt)}" loading="lazy" decoding="async"></a>'
  else:
   preview='<div class="directory-preview coming-soon-art" aria-hidden="true"><span>Coming soon</span></div>'
  body+=f'<li>{preview}<div class="directory-copy"><strong><a href="/{slug}/">{E(label)}</a></strong><p>{E(desc)}</p>'+(f'<p class="availability">{status}</p>' if status else '')+'</div></li>'
 body+='</ul></section><section><h2>More tools and projects</h2><p><a href="/boss-button/">Boss Button</a> · <a href="/mock-location/">Mock Location</a> · <a href="/kenai-report-data/">Kenai Report Data</a> · <a href="/alaska-gold-run/">Alaska Gold Run (in development)</a></p></section><section id="about"><h2>About the studio</h2><p>Built by an independent developer. Each app page explains its purpose, connection requirements, and privacy choices, so you can decide whether it fits your needs.</p><p>Questions or feedback? Email <a href="mailto:feedback@tripperdeelabs.com">feedback@tripperdeelabs.com</a>.</p></section>'
 page('/','Android Apps, Games and Wear OS Watch Faces','Explore TripperDeeLabs Android apps, offline games and Wear OS watch faces. Find screenshots, privacy details, download links and project availability.',body)
