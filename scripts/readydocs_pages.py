"""Generate the ReadyDocs website pages and add its directory links."""

from bs4 import BeautifulSoup
from page_template import BASE, ROOT, page

SLUG = "/readydocs/"
ICON = "/assets/apps/readydocs/icon.webp"
MAIL = "tripperdeelabs@gmail.com"
LINKS = """
<p><a href="/readydocs/">ReadyDocs overview</a> ·
<a href="/readydocs/privacy/">Privacy policy</a> ·
<a href="/readydocs/support/">Support</a></p>
"""


def ready_page(path, title, description, body, image=None):
    page(path, title, description, body, image)
    output = ROOT / path.strip("/") / "index.html"
    html = output.read_text(encoding="utf-8")
    html = html.replace("<body>", '<body><a class="skip-link" href="#main-content">Skip to main content</a>', 1)
    html = html.replace('<main class="wrap">', '<main class="wrap" id="main-content" tabindex="-1">', 1)
    output.write_text(html, encoding="utf-8")


def build():
    ready_page(
        SLUG,
        "ReadyDocs for Android",
        "Show selected PDFs or images on a securely locked Android phone. ReadyDocs also offers a separate emergency card and an encrypted vault.",
        """
<section class="catalog-hero">
  <img src="/assets/apps/readydocs/icon.webp" width="112" height="112" alt="">
  <h1>ReadyDocs</h1>
  <p class="lead">Hand over the document. Keep your phone locked.</p>
  <p>Show a selected PDF or image to someone on your phone without opening your other apps. ReadyDocs displays your selected files in a read-only viewer over Android’s secure lock screen.</p>
  <p class="availability">In development · Android 11 and newer</p>
  <p style="display:flex;flex-wrap:wrap;align-items:center;gap:.75rem"><a class="button" href="/readydocs/support/">How to use ReadyDocs</a> <a href="/readydocs/privacy/">Privacy policy</a></p>
</section>
<article class="prose">
  <h2>Choose what to show</h2>
  <p>Save up to three documents in your encrypted vault. ReadyDocs can guide you through photographing both sides of a driver’s license, a health insurance card, or a car insurance card. You can also import a PDF or image. Choose the files for this handoff and let ReadyDocs lock the phone after one-time setup, or lock it yourself. Wake the phone without unlocking. The recipient can navigate the selected PDFs and images. Exiting the viewer returns them to Android’s lock screen.</p>
  <h2>Set up a separate emergency card</h2>
  <p>Add the name, emergency contact or medical notes you choose to make visible on the lock screen. On phones that support lock-screen widgets, the optional ReadyDocs Emergency widget opens the card directly. There is also a Quick Settings tile for phones that allow access to tiles while locked.</p>
  <h2>Keep your files on your device</h2>
  <p>ReadyDocs uses Android Keystore and works offline. It has no account, ads or cloud sync. Your original files stay with the provider you selected.</p>
</article>
""",
        BASE + ICON,
    )
    ready_page(
        SLUG + "privacy/",
        "ReadyDocs privacy policy",
        "How ReadyDocs handles imported documents, emergency information, Android screen-lock verification, local encryption and deletion.",
        f"""
<article class="prose">
  <h1>ReadyDocs privacy policy</h1>
  <p>Effective November 22, 2026</p>
  <p>This policy covers the ReadyDocs Android app, package <code>com.tripperdeelabs.readydocs</code>, provided by TripperDeeLabs.</p>
  <h2>Documents and emergency information</h2>
  <p>ReadyDocs reads the PDFs or images you select in Android’s file picker and stores encrypted copies on your phone. Imported copies can retain information embedded in the original files. The optional emergency card stores the name, emergency contact details and medical notes you choose to enter. The app can display the files you select for a handoff and the separate card while Android reports that the phone is securely locked. Anyone who can see that screen can read the information displayed.</p>
  <h2>Optional card photos</h2>
  <p>The guided flow opens your phone’s camera app to capture the front and back of a card. ReadyDocs grants the camera access to a temporary destination inside ReadyDocs. The app removes its temporary photo after processing and re-encodes the image without copying the original camera metadata. If you save the pair, ReadyDocs stores it as one encrypted vault item with the generic card type. The camera app may handle photos under its own settings and policy.</p>
  <h2>Local processing and screen-lock verification</h2>
  <p>ReadyDocs stores vault copies in app-private storage using AES-256-GCM authenticated encryption. Android Keystore manages the encryption key. Android performs the screen-lock verification used for owner setup. ReadyDocs receives the verification result without receiving your PIN, pattern or password. ReadyDocs uses Android’s secure-window controls to block ordinary screenshots and screen recording of the viewer, but a person can still photograph the display with another device.</p>
  <h2>Optional automatic lock and shortcuts</h2>
  <p>If you opt in through Android Settings, ReadyDocs uses Android’s force-lock device administrator capability when you start an automatic document handoff or tap the emergency Quick Settings tile while your phone is unlocked. You can disable it in owner setup or in Android’s device admin settings. The emergency widget and tile display a generic label and open the separate card only while the phone is securely locked. They do not include document or card content in their label or preview. You can also opt in to a quiet emergency notification. Its generic title and shortcut contain no saved data. ReadyDocs can restore the notification after a restart if you left it enabled, after Android makes the app storage available.</p>
  <h2>Network access and providers</h2>
  <p>The app requests no network permission and includes no account, advertising, analytics, payment feature, developer-operated sync or automatic crash reporting. TripperDeeLabs receives no vault contents or emergency-card entries from the app. If you select a file from a cloud-backed document provider, that provider handles the original under its own policy. ReadyDocs leaves the original in place.</p>
  <h2>Retention and deletion</h2>
  <p>Encrypted copies and the emergency card remain in ReadyDocs until you replace or remove them. You can do that in owner setup. Clearing app storage or uninstalling ReadyDocs removes the local vault. The app excludes vault data from Android backup and has no remote recovery service. Removing a ReadyDocs copy leaves originals and other external copies in place.</p>
  <h2>Children and families</h2>
  <p>ReadyDocs is intended for families, including children with help from a parent or guardian. ReadyDocs does not ask for a birth date or create a child profile. The same local handling applies to all ages. Parents and guardians can review what a child stores and remove it using the phone’s owner setup. Only share documents and emergency information that you have permission to show.</p>
  <h2>Support and website</h2>
  <p>If you email <a href="mailto:{MAIL}">{MAIL}</a>, we receive the details you send and use them to respond. Leave documents, medical details and device credentials out of support messages. This site’s data practices are described in the <a href="/privacy/">website privacy policy</a>.</p>
{LINKS}
</article>
""",
    )
    ready_page(
        SLUG + "support/",
        "ReadyDocs support",
        "Set up automatic or manual document handoff, troubleshoot imports, and add the separate ReadyDocs Emergency widget or Quick Settings tile.",
        f"""
<article class="prose">
  <h1>ReadyDocs support</h1>
  <h2>Start a document handoff</h2>
  <ol>
    <li>Set an Android PIN, pattern or password. After restarting your phone, unlock it once before using ReadyDocs.</li>
    <li>Open ReadyDocs, tap <strong>Unlock owner setup</strong> and verify your screen lock.</li>
    <li>Import one or more files and select the files to show. Use <strong>Enable automatic lock</strong> and approve Android’s prompt to use <strong>Lock phone and start handoff</strong>. For manual locking, use <strong>Start selected handoff</strong>.</li>
    <li>Within one minute, wake the phone without unlocking. If you chose manual locking, turn off the screen first and let Android lock the phone. The viewer ends after three minutes, on unlock or when you leave it.</li>
  </ol>
  <h2>Turn off automatic lock</h2>
  <p>Use <strong>Disable automatic lock</strong> in owner setup or switch off ReadyDocs in Android’s device admin settings. Android may require your PIN, pattern or password after an automatic lock. If Android blocks uninstalling ReadyDocs, turn off its device administrator access first.</p>
  <h2>The viewer keeps asking you to lock the phone</h2>
  <p>Wait until Android actually requires authentication before waking the screen. Android’s lock delay and settings such as Extend Unlock can keep the phone unlocked with the screen off. Review those settings if the viewer stays on the waiting screen.</p>
  <h2>Photograph both sides of a card</h2>
  <p>Tap <strong>Add ID and insurance photos</strong> and choose a driver’s license, health insurance card, or car insurance card. Keep all four corners visible. Accept each shot in the camera, then tap <strong>Save both sides</strong> in ReadyDocs. Use <strong>Retake</strong> if the text is hard to read. Each pair takes one vault slot.</p>
  <h2>A file won’t import</h2>
  <p>Use a readable PDF or image. Each file must be 12 MiB or smaller, and a PDF can have up to 80 pages. If your provider offers an online-only file, make it available to Android’s file picker and try again.</p>
  <h2>Show the emergency card</h2>
  <p>Save the card in owner setup. The <strong>Set up lock-screen access</strong> screen explains how to look for <strong>ReadyDocs Emergency</strong> in your phone’s lock-screen widget editor. On Android 13 and newer, tap <strong>Add Quick Settings tile</strong> to open Android’s confirmation. The same screen explains manual tile setup. Tap <strong>Show emergency notification</strong> to try a quiet shortcut on the lock screen. Android controls whether and where it appears, including on a charging or always-on display. Lock your phone and try the shortcut. The widget and tile open only the emergency card, and some phones require unlocking to use the tile.</p>
  <p>With automatic lock enabled in owner setup, tapping the Quick Settings tile on an unlocked phone turns the screen off and locks it. Wake the phone without unlocking to read the card.</p>
  <h2>Contact</h2>
  <p>Email <a href="mailto:{MAIL}?subject=ReadyDocs%20support">{MAIL}</a> with your device model, Android version, ReadyDocs version and the steps you tried. Leave private documents and medical information out of your email.</p>
{LINKS}
</article>
""",
    )
    add_directory_links()


def add_directory_links():
    home = ROOT / "index.html"
    html = home.read_text(encoding="utf-8")
    if 'href="/readydocs/"' not in html:
        soup = BeautifulSoup(html, "html.parser")
        section = soup.select_one("#in-development .app-directory")
        if section is None:
            raise ValueError("Homepage development directory has moved")
        card = f"""<li><a class="directory-preview" href="{SLUG}"><img src="{ICON}" width="256" height="256" loading="lazy" alt="ReadyDocs"></a><div class="directory-copy"><h3><a href="{SLUG}">ReadyDocs</a></h3><p class="availability">In development</p><p>Show selected PDFs and images while your phone stays locked, with a separate emergency card.</p><p><a href="{SLUG}privacy/">Privacy</a> · <a href="{SLUG}support/">Support</a></p></div></li>"""
        section.insert(0, BeautifulSoup(card, "html.parser").li)
        home.write_text(str(soup), encoding="utf-8")

    directory = ROOT / "privacy/apps/index.html"
    html = directory.read_text(encoding="utf-8")
    if 'href="/readydocs/privacy/"' not in html:
        anchor = '<li><a href="/retro-arcade/privacy/">'
        if html.count(anchor) != 1:
            raise ValueError("App privacy directory has moved")
        link = '<li><a href="/readydocs/privacy/">ReadyDocs Privacy Policy</a></li>'
        directory.write_text(html.replace(anchor, link + anchor, 1), encoding="utf-8")


if __name__ == "__main__":
    build()
