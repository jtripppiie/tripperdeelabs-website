"""Compatibility routes for the former FamilyLink development name."""
def build(page):
 for suffix in ['', 'privacy/', 'support/']:
  page('/familylink/'+suffix,'FamilyLink is now NearCrew','The development app has been renamed NearCrew Offline Chat, for adults18+.','<section><h1>FamilyLink is now NearCrew</h1><p>The first release is now designed for adults aged18 and older.</p><p><a href="/nearcrew/'+suffix+'">Open the current NearCrew page</a></p></section>')
