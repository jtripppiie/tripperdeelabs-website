"""Render the ClapFind development, privacy, and support pages."""


def build(page):
    page(
        "/clap-find/",
        "ClapFind — Find Your Nearby Phone by Clapping",
        "ClapFind is an Android phone finder in development. Clap nearby to make your phone ring, vibrate, and flash.",
        '''<section class="catalog-hero">
<p class="eyebrow">Android utility · In development</p>
<h1>ClapFind</h1>
<p class="lead">Clap once. Find your phone nearby.</p>
<p>ClapFind is a simple phone finder for the moments your Android phone is close by but out of sight. Turn listening on, put the phone down, and clap to make it ring, vibrate, and flash.</p>
<p><strong>In development.</strong> A public Google Play listing is not available yet. The planned US price is $0.50 as a one-time download; the final listing price will be confirmed before release.</p>
</section>
<section><h2>How it works</h2><ol><li>Tap Start listening and allow microphone access.</li><li>Place your phone nearby with the microphone unobstructed.</li><li>Clap to trigger the phone’s alarm, vibration, and optional flashlight signal.</li></ol><p>An ongoing Android notification stays visible while listening is on. Stop listening from the app or its notification. ClapFind only helps locate a phone within sound range; it is not a remote tracker.</p></section>
<section><h2>Adjust it for your room</h2><p>Choose high, medium, or low sensitivity. Softer claps may need high sensitivity; a noisy room may need low. Sudden sounds can sometimes be mistaken for a clap, so accuracy may vary with the room, phone placement, and device.</p></section>
<section><h2>Audio stays on your phone</h2><p>The prototype analyzes microphone samples on-device and does not save or upload audio. Listening starts only when you turn it on and stops when you turn it off. Camera access is used only for the optional flashlight alert. Read the <a href="/clap-find/privacy/">privacy policy</a> for details.</p></section>
<p><a href="/clap-find/support/">Help and support</a> · <a href="mailto:tripperdeelabs@gmail.com">Contact TripperDeeLabs</a></p>''',
    )

    page(
        "/clap-find/privacy/",
        "ClapFind Privacy Policy",
        "How ClapFind uses microphone and optional camera permissions to find your nearby Android phone.",
        '''<section class="catalog-hero"><p class="eyebrow">ClapFind · Android · In development</p><h1>Privacy policy</h1><p class="lead">Updated November 22, 2026</p><p>Publisher: TripperDeeLabs · Contact: <a href="mailto:tripperdeelabs@gmail.com">tripperdeelabs@gmail.com</a></p></section>
<section><h2>Microphone</h2><p>ClapFind requests microphone permission to detect a clap while listening is enabled. The Android app analyzes short audio samples in memory on your device. It does not save raw audio recordings, send audio to a server, or upload microphone samples. Listening starts only after you turn it on and stops when you turn it off, use Stop in the ongoing notification, or Android ends the service. Clap detection requires the phone to be powered on and within microphone range.</p></section>
<section><h2>Camera and flashlight</h2><p>The app may request camera permission to flash the phone’s built-in torch after a clap. The camera is not used to take photos or video. If camera permission is not granted or a flashlight is unavailable, the sound and vibration alerts can still work.</p></section>
<section><h2>Settings and other data</h2><p>The current prototype stores the selected clap-sensitivity level and listening state locally on the device. It does not require an account and contains no ads, analytics SDK, or internet permission. No personal information is sent to TripperDeeLabs.</p></section>
<section><h2>Device controls</h2><p>You can revoke microphone or camera permission in Android Settings. Turn listening off in ClapFind or use the Stop action in its notification. Clearing app storage or uninstalling removes local settings.</p></section>
<section><h2>Children and changes</h2><p>ClapFind is a nearby phone-finding utility and does not ask for a birth date or account. This policy may change if the app’s features or included software change. Any update will be posted on this page with a revised date.</p></section>
<p><a href="/clap-find/">ClapFind</a> · <a href="/clap-find/support/">Support</a></p>''',
    )

    page(
        "/clap-find/support/",
        "ClapFind Support",
        "Help with microphone access, clap sensitivity, alerts, and finding a nearby Android phone with ClapFind.",
        '''<section class="catalog-hero"><p class="eyebrow">ClapFind · Android · In development</p><h1>Help and support</h1><p class="lead">Get help finding your nearby phone.</p><p>ClapFind is still in development. It is not available for download from Google Play yet.</p></section>
<section><h2>Turn listening on and off</h2><p>Open ClapFind and tap Start listening before putting your phone down. Android shows an ongoing notification while the microphone service is active. Tap Stop in that notification, or return to the app and turn listening off.</p></section>
<section><h2>Claps are missed or trigger by mistake</h2><p>Keep the microphone uncovered and clap within hearing distance. Try High sensitivity in a quiet room or Low in a noisy room. Sudden sounds, distance, phone placement, and device-specific microphone behavior can affect detection.</p></section>
<section><h2>No sound, vibration, or flashlight</h2><p>Check your alarm volume and Do Not Disturb settings. Vibration and flashlight alerts depend on the phone’s hardware and Android settings. Microphone access is required for listening; camera access is optional and only used for the flashlight.</p></section>
<section><h2>Contact</h2><p>For questions or corrections, email <a href="mailto:tripperdeelabs@gmail.com">tripperdeelabs@gmail.com</a>. Include your phone model and Android version. Do not send recordings, passwords, or payment details.</p></section>
<p><a href="/clap-find/">ClapFind</a> · <a href="/clap-find/privacy/">Privacy policy</a></p>''',
    )
