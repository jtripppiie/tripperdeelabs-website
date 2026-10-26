"""Check crawlable SEO content, truthful offers, FAQ parity and preserved routes."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup
import json,xml.etree.ElementTree as ET
from seo_content import PAGES
ROOT=Path(__file__).resolve().parents[1];BASE='https://tripperdeelabs.com'
apps={a['slug']:a for a in json.loads((ROOT/'data/apps.json').read_text())}
urls={n.text for n in ET.parse(ROOT/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
home=BeautifulSoup((ROOT/'index.html').read_text(),'html.parser')
assert home.select_one('a[href="mailto:feedback@tripperdeelabs.com"]')
robot=RobotFileParser();robot.parse((ROOT/'robots.txt').read_text().splitlines())
for slug in [*PAGES,'canopy-quest','you-rush-alaska']:
 path='/'+slug+'/';s=BeautifulSoup((ROOT/slug/'index.html').read_text(),'html.parser')
 assert home.select_one(f'a[href="{path}"]'),slug+' home link'
 assert BASE+path in urls,slug+' sitemap'
 for crawler in ['Googlebot','Bingbot','OAI-SearchBot','Claude-SearchBot','PerplexityBot']:
  assert robot.can_fetch(crawler,BASE+path),(slug,crawler,'robots')
 assert s.select_one('link[rel="canonical"]')['href']==BASE+path
 assert not s.select_one('meta[name="robots"][content*="noindex"]')
 assert len(s.select('h1'))==1
 privacy='/alaska-rush/privacy/' if slug=='you-rush-alaska' else path+'privacy/'
 assert s.select_one(f'a[href="{privacy}"]'),slug+' privacy'
 if slug not in PAGES:continue
 data=json.loads(s.select_one('script[type="application/ld+json"]').string)['@graph']
 software,faq=data
 assert software['@type']=='SoftwareApplication'
 assert not any(k in software for k in ['aggregateRating','review'])
 if slug in apps:
  assert software['offers']['price']==apps[slug]['price']
  assert software['offers']['url']==apps[slug]['play']
  assert s.select_one(f'a[href="{apps[slug]["play"]}"] img.play-badge')
 else:
  assert 'offers' not in software and not s.select('.play-badge')
 assert 3<=len(faq['mainEntity'])<=5
 for q in faq['mainEntity']:
  assert q['name'] in s.get_text() and q['acceptedAnswer']['text'] in s.get_text(),slug+' FAQ mismatch'
 assert 135<=len(s.select_one('meta[name="description"]')['content'])<=165
 images=s.select('.screenshots img');assert 2<=len(images)<=4
 for img in images:
  assert len(img['alt'])>30 and img.get('width') and img.get('height')
  assert img['src'].endswith('.webp') and img['loading']=='lazy'
  assert (ROOT/img['src'].lstrip('/')).stat().st_size<250_000
 for node in s.select('.screenshots,.price'):node.decompose()
 words=len(s.main.get_text(' ',strip=True).split());assert 300<=words<=600,(slug,words)
 print(f'{slug}: {words} words, {len(images)} screenshots, 4 matching FAQs')
# Every public index page is in the sitemap; no draft or noindex previews leak in.
for p in ROOT.rglob('index.html'):
 rel=p.relative_to(ROOT).as_posix()
 if rel.startswith(('.git/','drafts/')):continue
 s=BeautifulSoup(p.read_text(),'html.parser');url=BASE+'/'+rel[:-10]
 if 'noindex' not in p.read_text().lower():
  assert s.select_one('html[lang]') and s.select_one('title') and s.select_one('meta[name=description]'),rel
  assert s.select_one('a.skip-link[href="#main-content"]') and s.select_one('main#main-content[tabindex="-1"]'),rel
  ids=[n['id'] for n in s.select('[id]')];assert len(ids)==len(set(ids)),rel+' duplicate IDs'
 assert (url in urls)==('noindex' not in p.read_text().lower()),rel+' sitemap coverage'
 for node in s.select('a[href],img[src],link[href],script[src]'):
  raw=node.get('href',node.get('src',''));u=urlsplit(raw)
  if u.scheme or u.netloc:continue
  target=(ROOT/unquote(u.path.lstrip('/')) if u.path.startswith('/') else p.parent/unquote(u.path)) if u.path else p
  assert target.exists(),(rel,raw)
  if u.fragment and node.name=='a':
   if target.is_dir():target=target/'index.html'
   if target.suffix=='.html':
    dest=BeautifulSoup(target.read_text(),'html.parser')
    assert dest.find(id=unquote(u.fragment)) or dest.find('a',attrs={'name':unquote(u.fragment)}),(rel,raw,'fragment')
print('PASS: SEO content, image budget, schema, navigation, local links/fragments and sitemap coverage.')
