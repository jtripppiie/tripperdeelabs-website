"""Render the approved SEO pages using the site's existing static shell."""
from pathlib import Path
from html import escape as E
import json
from PIL import Image
from seo_content import PAGES
ROOT=Path(__file__).resolve().parents[1]
BASE='https://tripperdeelabs.com'

def gallery(slug,shots,development=False):
 body='<section><h2>Inside the app</h2><p>'+('Real desktop gameplay captures from release preparation; the final Android display may differ.' if slug=='alaska-gold-run' else 'Development-build screenshots; features may change before release.' if development else ('Real app screenshots. Displayed dates, counts, and readings are examples, not live reports.' if slug in ['salmon-tracker','kenai-fishing-report','launch-vector'] else 'Real app screenshots.'))+'</p><div class="screenshots">'
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
  name=a['name'] if a else {'moments':'Moments','wonder-cascade':'Wonder Cascade','alaska-gold-run':'Alaska Gold Run'}[slug]
  os=a['os'] if a else ('Wear OS 6 or newer' if slug=='moments' else 'Android')
  # Prices in FAQ answers follow the verified catalog rather than frozen draft prices.
  faqs=[(q,ans.replace('$0.50', '$'+a['price']) if a else ans) for q,ans in c['faq']]
  app_schema={'@context':'https://schema.org','@type':'SoftwareApplication','name':name,'operatingSystem':os,'url':BASE+'/'+slug+'/','applicationCategory':a['category'] if a else ('GameApplication' if slug in ['wonder-cascade','alaska-gold-run'] else 'UtilitiesApplication')}
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
  if upcoming:body+='<p class="availability">'+E(c.get('status','In development · Public Play listing unavailable'))+'</p>'
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
 # Keep the informative catalog summaries alongside the visual cards.
 labels={'alaska-gold-run':'Alaska Gold Run','parked':'Parked','local-lore':'Local Lore','roboball':'RoboBall','you-rush-alaska':'You Rush Alaska','salmon-tracker':'Salmon Tracker','wonder-cascade':'Wonder Cascade','private-eyes':'Private Eyes','moto-thrash':'Moto Thrash','captain-quack':'Captain Quack','summit-line':'Summit Line','launch-vector':'Launch Vector','kenai-fishing-report':'Kenai Fishing Report','amelia-navigator':'Amelia Navigator','dive-watch':'Dive Watch','moments':'Moments','canopy-quest':'Canopy Quest','boss-button':'Boss Button','mock-location':'Mock Location','kenai-report-data':'Kenai Report Data'}
 groups=[('phone-apps','Phone apps',['parked','local-lore','salmon-tracker','private-eyes','boss-button','mock-location']),('phone-games','Phone games',['roboball','moto-thrash','captain-quack','canopy-quest','alaska-gold-run']),('watch-faces','Wear OS watch faces',['summit-line','launch-vector','kenai-fishing-report','amelia-navigator','dive-watch']),('watch-data','Wear OS companion apps',['kenai-report-data']),('in-development','In development',['wonder-cascade','moments','you-rush-alaska'])]
 body='<section class="catalog-hero home-hero"><div class="home-intro"><div><p class="eyebrow">Independent Android studio</p><h1>Useful Android apps.<br>Games and watch faces.</h1><p class="lead">TripperDeeLabs makes practical Android apps, offline games, and Wear OS watch faces, with clear privacy information for each product.</p><p>Find a saved parking spot, explore local history, follow Alaska salmon counts, or keep selected photos in an encrypted vault. For downtime, explore arcade games; for your wrist, choose a watch face built around the information you want to see.</p><p><a href="#phone-apps">Phone apps</a> · <a href="#phone-games">Games</a> · <a href="#watch-faces">Watch faces</a> · <a href="#in-development">Coming soon</a></p></div><img class="studio-logo" src="/assets/tripperdeelabs-logo.png" width="200" height="200" alt="TripperDeeLabs fox scientist logo" fetchpriority="high"></div></section><div id="apps">'
 for anchor,heading,slugs in groups:
  body+=f'<section id="{anchor}"><h2>{heading}</h2><ul class="app-directory">'
  for slug in slugs:
   label=labels[slug]
   if slug=='alaska-gold-run':
    desc='Alaska Gold Run is an offline Android runner with three-lane swiping, jumping, sliding, skiing, and frozen-lake skating. Collect gold, earn gear, and explore snowy trails, railway tunnels, and ice caves. Submitted to Google Play; changes are in review as of October 24, 2026.'
   elif slug in copy:
    desc,detail=copy[slug][1:3]
   elif slug=='wonder-cascade':
    desc='Wonder Cascade is a match-3 puzzle game in development. Swap gems, combine powers, and plan a sequence of moves through finite-board challenges.'
    detail='The preview includes Strategy Stops, Mind puzzles, and a relaxed pace without countdown timers. Screenshots show the development build; a public Google Play release is not yet available.'
   elif slug=='moments':
    desc='Moments is a personal-photo watch face project for Wear OS 6. A curved image panel sits beside digital time, battery information, and customizable data fields.'
    detail='Photo selection uses the supported paired-phone system flow. Development screenshots are available; a public Google Play listing has not been confirmed.'
   else:
    desc='You Rush Alaska is coming soon from TripperDeeLabs.'
    detail='Visit its project page for release information when available. No public download, release date, or price has been announced here.'
   status={'alaska-gold-run':'Changes in review','canopy-quest':'Under maintenance','you-rush-alaska':'Coming soon','wonder-cascade':'In development','moments':'In development'}.get(slug)
   preview=''
   if slug!='you-rush-alaska':
    if slug in PAGES:
     index,alt=PAGES[slug]['screenshots'][-1] if slug in ['summit-line','kenai-fishing-report','parked'] else PAGES[slug]['screenshots'][0]
    else:
     index,alt={'canopy-quest':(1,'Canopy Quest jungle platformer at a saved camp'),'boss-button':(2,'Boss Button app with floating-button setup and privacy-cover controls'),'mock-location':(1,'Mock Location app showing five local coordinate bookmark slots'),'kenai-report-data':(1,'Kenai Report Data watch app displaying sockeye count and report date')}[slug]
    source=ROOT/f'assets/apps/{slug}/screenshot-{index}.png'
    thumb=ROOT/f'assets/apps/{slug}/home-preview.webp'
    im=Image.open(source).convert('RGB');im.thumbnail((640,480));im.save(thumb,'WEBP',quality=82,method=6)
    preview=f'<a class="directory-preview" href="/{slug}/" tabindex="-1"><img src="/assets/apps/{slug}/home-preview.webp" width="{im.width}" height="{im.height}" alt="{E(alt)}" loading="lazy" decoding="async"></a>'
   else:
    preview='<div class="directory-preview coming-soon-art" aria-hidden="true"><span>Coming soon</span></div>'
   if slug=='kenai-report-data':
    preview='<div class="companion-visual"><p class="companion-kicker">REPORTS ON YOUR WRIST</p><div class="companion-screens">'
    for number,caption in [(1,'Fish counts'),(2,'River conditions')]:
     source=ROOT/f'assets/apps/{slug}/screenshot-{number}.png'
     target=ROOT/f'assets/apps/{slug}/home-detail-{number}.webp'
     im=Image.open(source).convert('RGB');im.save(target,'WEBP',quality=88,method=6)
     preview+=f'<figure><div class="watch-bezel"><div class="watch-screen"><img src="/assets/apps/{slug}/home-detail-{number}.webp" width="900" height="1600" loading="lazy" decoding="async" alt="Kenai Report Data actual watch screen: {caption.lower()}"></div></div><figcaption>{caption}</figcaption></figure>'
    preview+='</div><p class="companion-caption">Actual app screens · Example reports, not live readings</p></div>'
   body+=f'<li>{preview}<div class="directory-copy"><h3><a href="/{slug}/">{E(label)}</a></h3>'+(f'<div class="availability">{status}</div>' if status else '')+f'<p class="app-summary">{E(desc)}</p><a class="directory-more" href="/{slug}/">Explore {E(label)} →</a>'
   if slug in lookup and not status:body+=badge(lookup[slug])
   body+='</div></li>'
  body+='</ul></section>'
 body+='</div><section id="about"><h2>About TripperDeeLabs</h2><p>I’m the independent developer behind TripperDeeLabs. I make Android games, practical phone apps and Wear OS watch faces, with projects ranging from Alaska fish reports to retro arcade games.</p><p>Each app page explains what the app does, who it is for, and what stays on your device. Offline games save progress locally. Apps that use maps, public reports, or launch schedules need a connection for fresh information. Watch readings depend on the device and the providers you choose.</p><p>Read the app’s privacy policy for its specific permissions, storage, and external services. For questions, ideas, or support, email <a href="mailto:feedback@tripperdeelabs.com">feedback@tripperdeelabs.com</a> or visit the <a href="/feedback/">feedback page</a>.</p></section>'
 page('/','Android Apps, Games and Wear OS Watch Faces','Explore TripperDeeLabs Android apps, offline games and Wear OS watch faces. Find screenshots, privacy details, download links and project availability.',body)
