from pathlib import Path
import html,json,re
ROOT=Path(__file__).resolve().parents[1]
BASE="https://tripperdeelabs.com"
E=lambda s:html.escape(str(s),quote=True)
HEADER='<header class="site-header"><nav class="nav wrap" aria-label="Main navigation"><a class="brand" href="/"><img class="brand-logo" src="/assets/tripperdeelabs-logo.png" width="48" height="48" alt="">TripperDeeLabs</a><div class="links"><a href="/#apps">Apps</a><a href="/wear-os/">Wear OS</a><a href="/watch-faces/">Watch Faces</a><a href="/#about">About</a></div></nav></header>'
FOOTER='<footer class="studio-footer"><div class="wrap"><div class="studio-footer-main"><div class="studio-footer-brand"><a href="/">TripperDeeLabs</a><p>Doing TripperDee things in a TripperDee world.</p></div><nav class="studio-footer-nav" aria-label="Footer navigation"><a href="/#apps">Apps</a><a href="/#about">About the developer</a><a href="mailto:tripperdeelabs@gmail.com">Contact</a><a href="/feedback/">Feedback</a><a href="/privacy/">Website privacy</a></nav></div><div class="studio-footer-bottom"><span>© 2026 TripperDeeLabs</span><span>Google Play and the Google Play logo are trademarks of Google LLC.</span></div></div></footer>'
def page(path,title,desc,body,image=None,schema=None):
 url=BASE+path; image=image or BASE+'/assets/tripperdeelabs-logo.png'
 tags=f'<title>{E(title)} — TripperDeeLabs</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">'
 for prop,val in [('og:type','website'),('og:title',title),('og:description',desc),('og:url',url),('og:image',image),('og:image:alt',title)]:tags+=f'<meta property="{prop}" content="{E(val)}">'
 if '/social.png' in image:tags+='<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
 for name,val in [('twitter:card','summary_large_image'),('twitter:title',title),('twitter:description',desc),('twitter:image',image),('twitter:image:alt',title)]:tags+=f'<meta name="{name}" content="{E(val)}">'
 if schema:tags+='<script type="application/ld+json">'+json.dumps(schema).replace('<','\\u003c')+'</script>'
 # Stable studio/site identity helps consumers connect each page to its publisher.
 organization={'@type':'Organization','@id':BASE+'/#studio','name':'TripperDeeLabs','url':BASE+'/','logo':BASE+'/assets/tripperdeelabs-logo.png','email':'tripperdeelabs@gmail.com'}
 website={'@type':'WebSite','@id':BASE+'/#website','url':BASE+'/','name':'TripperDeeLabs','publisher':{'@id':BASE+'/#studio'},'inLanguage':'en'}
 webpage={'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':desc,'isPartOf':{'@id':BASE+'/#website'},'publisher':{'@id':BASE+'/#studio'},'inLanguage':'en'}
 identity={'@context':'https://schema.org','@graph':[organization,website,webpage]}
 if path!='/':
  identity['@graph'].append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':BASE+'/'},{'@type':'ListItem','position':2,'name':title,'item':url}]})
  body='<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="/">Home</a> <span aria-hidden="true">/</span> <span aria-current="page">'+E(title)+'</span></nav>'+body
 tags+='<script type="application/ld+json">'+json.dumps(identity).replace('<','\\u003c')+'</script>'
 doc='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'+tags+'<link rel="icon" href="/assets/tripperdeelabs-logo.png" type="image/png"><link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/catalog.css"><script defer src="/cookie-consent.js"></script></head><body>'+HEADER+'<main class="wrap">'+body+'</main>'+FOOTER+'</body></html>'
 out=ROOT/path.strip('/')/'index.html';out.parent.mkdir(exist_ok=True,parents=True);out.write_text(doc+'\n')
