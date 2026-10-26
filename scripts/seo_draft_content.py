"""Reviewed SEO pilot copy. Promote into catalog generator only after owner approval."""
PAGES = {
 'parked': {
  'title': 'Find where I parked my car — Parked for Android',
  'h1': 'Find where I parked my car',
  'description': 'Save your parking spot with Parked for Android. Use a home-screen widget, keep your pin on your phone, and open walking directions when you return.',
  'intro': 'Parked is an Android parking reminder for the moment you leave your car and the moment you need to find it again. Save one location from the app or its home-screen widget, then open walking directions back to that spot. It is useful for unfamiliar streets, shopping trips, airport lots, and busy event parking.',
  'sections': [
   ('Save your spot before you walk away', 'Tap Park Here while you are near the car and allow foreground location access. Parked records the coordinates, save time, and accuracy reported by Android. The widget puts the parking controls on your home screen, so you do not need to navigate through the app each time. Check the saved accuracy before relying on the pin.'),
   ('Return, share, or replace your parking pin', 'When you are ready to return, use the find-car control to send the saved destination to your chosen maps app. You can also share a map link with someone meeting you at the car. A new parking location replaces the previous one, and the app includes a control to clear it. Parked remembers a single parking spot rather than keeping a history of your journeys.'),
   ('What stays on your phone', 'Saving the pin uses the phone’s location services and does not require internet access. Parked has no account, ads, analytics, background location access, or internet permission. TripperDeeLabs cannot retrieve your saved location. Choosing directions or sharing passes the destination to another app, whose connectivity needs and privacy practices apply. GPS reception and accuracy can be limited by buildings, particularly inside parking garages.')
  ],
  'faq': [
   ('Does Parked work without a signal?', 'You can save a location without internet when your phone can obtain a location fix. Walking directions open in your maps app and may need a connection or previously downloaded maps.'),
   ('Does it remember my parking level?', 'The saved pin is a geographic location. In a multi-level garage, make a separate note of the floor or bay; GPS alone may not distinguish levels.'),
   ('Does it track my car automatically?', 'No. Tap to save your spot when you park. Parked does not request background location access and is not a vehicle tracker.'),
   ('Is Parked a subscription?', 'No. The US Google Play listing offers a one-time $0.50 purchase. Check Google Play for the price and availability in your region.')
  ],
  'screenshots': [(1, 'Parked home-screen widget with Find My Car and App controls'), (2, 'Parked light theme showing no saved car and the Park Here button'), (3, 'Parked dark theme with a saved location, directions, sharing, and clear controls')]
 },
 'salmon-tracker': {
  'title': 'Alaska salmon counts — Salmon Tracker for Android',
  'h1': 'Alaska salmon counts on your Android phone',
  'description': 'Follow Alaska salmon counts for Kenai, Kasilof and Russian River runs. Compare daily totals and past seasons, with optional alerts and cached reports.',
  'intro': 'Salmon Tracker brings public Alaska salmon passage counts to your Android phone. Follow selected Kenai Peninsula runs, view daily counts alongside season totals, and compare reports across years. It is for anglers and anyone following the progress of a salmon run who wants those reports together in a phone app.',
  'sections': [
   ('Choose the rivers and runs you follow', 'Select the count projects that matter to you: Kenai River late-run sockeye, Kenai River kings, Kasilof River sockeye, and Russian River early- and late-run sockeye. The app retrieves public Alaska Department of Fish and Game reports. Reporting dates and available counts depend on the source; a new calendar day does not necessarily mean a new count has been published.'),
   ('Read daily counts in context', 'Use daily and cumulative charts to look beyond a single number. Seven-day, fourteen-day, and season views let you examine different periods, while prior-season comparisons show how reported passage differs between years. Optional notifications can alert you to new counts or changes. Settings include quiet hours, synchronization controls, and a Wi-Fi-only option. You can also request a manual check for new counts.'),
   ('Cached reports when coverage drops', 'An internet connection is needed to download updates. Reports already downloaded remain available when your connection drops, so check the reporting date before treating a cached number as current. Salmon Tracker has no ads or account requirement. Preferences and downloaded counts stay on your device. Requests go directly to the public data service, which may receive normal connection information such as your IP address.')
  ],
  'faq': [
   ('Is this an official Alaska government app?', 'No. Salmon Tracker is an independent, unofficial client. It is not affiliated with or endorsed by the State of Alaska or the Alaska Department of Fish and Game.'),
   ('Can I read counts offline?', 'Yes, if they were downloaded previously. New reports, revisions, and fresh alerts require a connection; cached reports do not update while you are offline.'),
   ('Do fish counts predict what I will catch?', 'No. Passage reports describe counted fish, not your likely catch. Consult official fishing regulations, emergency orders, and local conditions before fishing.'),
   ('Do I have to enable notifications?', 'No. Notifications are optional. You can turn them off and open the app to check counts yourself. The US Play listing is a one-time $0.50 purchase, with regional prices shown by Google Play.')
  ],
  'screenshots': [(4, 'Salmon Tracker showing an offline cached Kenai sockeye report and its last-check time'), (2, 'Kenai sockeye daily passage chart with prior-year comparison and cumulative total'), (3, 'Salmon Tracker settings for quiet hours, Wi-Fi sync, and followed river projects')]
 }
}
