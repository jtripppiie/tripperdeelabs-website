from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
from urllib.parse import urlsplit,unquote
import json,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1];apps=json.loads((root/'data/apps.json').read_text());errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
# Generated landing pages must retain the consent-gated analytics entry point.
# Policy pages with an explicit no-analytics promise are intentionally excluded.
landing_pages=['index.html','garmin/index.html','alaska-gold-run/index.html','moments/index.html']+[a['slug']+'/index.html' for a in apps]
for rel in landing_pages:
 soup=BeautifulSoup((root/rel).read_text(),'html.parser')
 loaders=soup.select('script[src="/cookie-consent.js"]')
 check(len(loaders)==1 and loaders[0].has_attr('defer'),rel+' missing/duplicate consent loader or missing defer')
 check(not soup.select('script[src*="googletagmanager.com"]'),rel+' bypasses consent with a direct Google tag')
check("var GA_ID = 'G-77H5RENPZ3';" in (root/'cookie-consent.js').read_text(),'unexpected Analytics measurement ID')
titles=set();descriptions=set()
for a in apps:
 slug=a['slug'];p=root/slug/'index.html';s=BeautifulSoup(p.read_text(),'html.parser')
 check(len(s.select('h1'))==1,slug+' H1')
 title=s.title.text;desc=s.select_one('meta[name="description"]')['content']
 check(title not in titles,slug+' duplicate title');titles.add(title)
 check(desc not in descriptions,slug+' duplicate description');descriptions.add(desc)
 data=json.loads(s.select_one('script[type="application/ld+json"]').string)
 check(data['offers']['price']==a['price'],slug+' price');check(data['operatingSystem']==a['os'],slug+' OS')
 check(s.select_one(f'a[href="{a["play"]}"]') is not None,slug+' Play link')
 check(s.select_one(f'a[href="{a["privacy"]}"]') is not None,slug+' privacy link')
 check(Image.open(root/'assets/apps'/slug/'social.png').size==(1200,630),slug+' social dimensions')
 for i in range(len(a['screenshotSources'])):Image.open(root/'assets/apps'/slug/f'screenshot-{i+1}.png').verify()
 if slug in ['local-lore','salmon-tracker','kenai-fishing-report','launch-vector']:
  check('offline' not in s.get_text().lower(),slug+' offline claim')
for p in root.rglob('*.html'):
 s=BeautifulSoup(p.read_text(),'html.parser');check(len(s.select('link[rel="canonical"]'))==1,str(p)+' canonical')
 for tag,attr in [('a','href'),('img','src'),('link','href'),('script','src')]:
  for node in s.select(f'{tag}[{attr}]'):
   url=urlsplit(node[attr])
   if url.scheme or url.netloc or not url.path:continue
   dest=root/unquote(url.path.lstrip('/')) if url.path.startswith('/') else p.parent/unquote(url.path)
   check(dest.exists(),f'{p.relative_to(root)} missing {url.path}')
urls=[e.text for e in ET.parse(root/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
for a in apps:check('https://tripperdeelabs.com/'+a['slug']+'/' in urls,a['slug']+' sitemap')
check('Sitemap: https://tripperdeelabs.com/sitemap.xml' in (root/'robots.txt').read_text(),'robots sitemap')
check(not list(root.rglob('*.apk')),'APK published')
print('\n'.join(errors) if errors else f'PASS: {len(apps)} live app pages; metadata, offers, screenshots, social cards, local links, sitemap and APK removal.')
raise SystemExit(bool(errors))
