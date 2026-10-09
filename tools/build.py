#!/usr/bin/env python3
"""Assemble the RCCG Fuller's Field site.

Every .html page is generated from this file so the header, footer and
floating Give button stay identical everywhere.

Run from the repo root:  python3 tools/build.py
"""
import os, html
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YT = "https://www.youtube.com/@rccgfullersfield"
FB = "https://www.facebook.com/rccgfullersfield/"
IG = "https://instagram.com/rccgfullersfield"
X = "https://x.com/Fullers_Field"
MAPS = "https://maps.app.goo.gl/6pb1X8zB5iHSp81V7"
EMAIL = "rccgfullersfield@gmail.com"
PHONE = "0803 303 0620"
TEL = "+2348033030620"
ADDRESS = "Km 47, Lekki–Epe Expressway, beside DKK Pharmacy &amp; Supermarket, opposite Maple Plaza, Farm Bus Stop, Oko-Ado, Lagos"
IMG = "images/web/"

def mailto(subject, body=""):
    q = "subject=" + quote(subject)
    if body:
        q += "&body=" + quote(body)
    return f"mailto:{EMAIL}?{q}"

# ------------------------------------------------------------------ icons
P = {
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M5.2 5.2l1.4 1.4M17.4 17.4l1.4 1.4M3 12h2M19 12h2M5.2 18.8l1.4-1.4M17.4 6.6l1.4-1.4"/>',
 "book": '<path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/>',
 "users": '<path d="M17 21v-2a4 4 0 00-4-4H7a4 4 0 00-4 4v2"/><circle cx="10" cy="7" r="4"/><path d="M21 21v-2a4 4 0 00-3-3.9M16 3.1a4 4 0 010 7.8"/>',
 "church": '<path d="M3 21h18M5 21V9l7-5 7 5v12M10 21v-5h4v5M12 1v3"/>',
 "heart": '<path d="M20.8 4.6a5.5 5.5 0 00-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 00-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 000-7.8z"/>',
 "music": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
 "video": '<rect x="2" y="5" width="15" height="14" rx="2"/><path d="M17 10l5-3v10l-5-3z"/>',
 "spark": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/>',
 "child": '<circle cx="12" cy="5" r="3"/><path d="M12 8v7M8 21l4-6 4 6M7 11h10"/>',
 "star": '<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
 "pray": '<path d="M12 3v8M8 21l-3-6 4-6 3 2 3-2 4 6-3 6"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 010 20M12 2a15 15 0 000 20"/>',
 "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0014 0M12 17v5"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8 9.9a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/>',
 "pin": '<path d="M12 21s-7-6.2-7-12a7 7 0 0114 0c0 5.8-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "play": '<rect x="3" y="6" width="18" height="12" rx="3"/><path d="M10 9.5l5 2.5-5 2.5z"/>',
 "hands": '<path d="M12 21s-7-5-7-11V4l7 4 7-4v6c0 6-7 11-7 11z"/>',
 "gift": '<rect x="3" y="8" width="18" height="13" rx="1"/><path d="M12 8v13M3 12h18M12 8S10 3 7.5 4 9 8 12 8zM12 8s2-5 4.5-4S15 8 12 8z"/>',
 "chev": '<path d="M6 9l6 6 6-6"/>',
}
def ic(name, sw=2):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>'
def ic_plain(name):  # styled by CSS (stroke set in stylesheet)
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{P[name]}</svg>'

COPY_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 012-2h10"/></svg>'
def copy_btn(v, aria=None, label="Copy"):
    a = f' aria-label="{aria}"' if aria else ""
    return f'<button class="copy-btn" type="button" data-copy="{v}"{a}>{COPY_SVG}<span class="lbl">{label}</span></button>'

FB_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7.5H16l.4-3H13.5V8.4c0-.87.24-1.46 1.5-1.46H16.5V4.3c-.26-.04-1.15-.11-2.19-.11-2.17 0-3.65 1.32-3.65 3.75v2.56H8.2v3h2.46V21h2.84z"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".6" fill="currentColor"/></svg>'
YT_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.6 7.2a2.5 2.5 0 00-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 002.4 7.2C2 8.8 2 12 2 12s0 3.2.4 4.8a2.5 2.5 0 001.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 001.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3z"/></svg>'

# ------------------------------------------------------------------ ministries data
MINISTRIES = [
 dict(fn="hope-of-nations.html", name="Hope of Nations", tag="Youth & Young Adults", when="Sundays, 9:30 – 11:00am",
      who="Teenagers, students and young adults", hero="members17.jpg",
      short="Raising the next generation of world-changers.",
      about=["Hope of Nations is the youth and young adults ministry of Fuller's Field. We are raising the next generation of leaders and influencers for God's kingdom.",
             "Young people face real pressures today. Hope of Nations gives them a place to bring honest questions, grow in their relationship with God and discover their gifts, with friends walking the same road."],
      acts=[("users", "Sunday youth service", "Worship, the Word and prayer every Sunday from 9:30am."),
            ("mic", "Creative arts", "Music, drama and spoken word, like our Easter Praise Concert."),
            ("book", "Career & life workshops", "Practical sessions on work, money, relationships and purpose."),
            ("globe", "Outreach", "Taking the love of Jesus to our neighbourhood and campuses.")],
      gallery=["members17.jpg", "members8.jpg", "members1.jpg", "members14.jpg", "members7.jpg"],
      steps=[("Come on Sunday", "Join us at 9:30am. Just walk in."),
             ("Say hello", "Meet a Hope of Nations leader after service."),
             ("Share your details", "Leave your name and number so we can keep you posted."),
             ("Get involved", "Join a team: music, drama, media, ushering or outreach.")]),
 dict(fn="childrens-church.html", name="Children's Church", tag="Kids", when="Sundays, during service",
      who="Children of the church and visitors", hero="childrenministry.jpg",
      short="A safe, fun, faith-filled space where kids discover God's love.",
      about=["Children's Church is where the youngest members of Fuller's Field learn about Jesus in a way they understand, through Bible stories, songs, prayer and lots of fun.",
             "It runs on Sundays while parents worship, so the whole family can meet God in church."],
      acts=[("book", "Bible stories", "Lessons from the RCCG children's curriculum."),
            ("music", "Songs & praise", "Children learn to worship with joy."),
            ("child", "Safe care", "Teachers look after every child."),
            ("star", "Special days", "Children's Day, Christmas and end-of-year celebrations.")],
      gallery=["childrenministry.jpg", "members19.jpg", "members25.jpg", "members12.jpg", "members2.jpg"],
      steps=[("Bring your child", "Arrive a few minutes early on Sunday."),
             ("Meet a teacher", "An usher will show you where Children's Church meets."),
             ("Register your child", "Share your child's name, age and your phone number."),
             ("Pick up after service", "Collect your child from their teacher.")]),
 dict(fn="wise-women.html", name="Wise Women", tag="60 & Above", when="Speak to a pastor for meeting times",
      who="Women aged 60 and above", hero="womenministry.jpg",
      short="Fellowship, wisdom and faith for women 60 and above.",
      about=["The Wise Women are the mothers of Fuller's Field: women of 60 and above who have walked with God through many seasons.",
             "They meet for fellowship, prayer and care for one another, and pour their wisdom into the younger women and families of the church."],
      acts=[("users", "Fellowship", "Time together to share, encourage and laugh."),
            ("pray", "Prayer", "Standing in prayer for families and the church."),
            ("heart", "Mentoring", "Walking alongside younger women and mothers."),
            ("music", "Praise", "Leading the church in song on special Sundays.")],
      gallery=["womenministry.jpg", "members13.jpg", "members28.jpg", "members21.jpg", "members24.jpg"],
      steps=[("Come on Sunday", "Worship with us at 7:30am or 10:30am."),
             ("Speak to a pastor", "Let a pastor know you would like to join."),
             ("Share your details", "Leave your name and phone number."),
             ("Join the next meeting", "We'll tell you when and where we meet.")]),
 dict(fn="wise-men.html", name="Wise Men", tag="60 & Above", when="Speak to a pastor for meeting times",
      who="Men aged 60 and above", hero="wisemen.jpg",
      short="Mentorship, prayer and purpose for men 60 and above.",
      about=["The Wise Men are the fathers of Fuller's Field: men of 60 and above who meet for brotherhood, prayer and purpose.",
             "They mentor younger men, stand with families in prayer and remind us all that it is never too late to serve God with joy."],
      acts=[("users", "Brotherhood", "Friendship and fellowship among the fathers of the church."),
            ("pray", "Prayer", "Interceding for families, the church and the nation."),
            ("star", "Mentoring", "Guiding younger men in faith, work and family."),
            ("church", "Service", "Supporting church programmes and special services.")],
      gallery=["wisemen.jpg", "members23.jpg", "members6.jpg", "members15.jpg", "members27.jpg"],
      steps=[("Come on Sunday", "Worship with us at 7:30am or 10:30am."),
             ("Speak to a pastor", "Let a pastor know you would like to join."),
             ("Share your details", "Leave your name and phone number."),
             ("Join the next meeting", "We'll tell you when and where we meet.")]),
]

DEPTS = [
 ("Ushering", "users", "Welcome people at the door, help them find a seat and receive the offering.", []),
 ("Choir & Music", "music", "Lead the church in praise and worship as a singer or instrumentalist.", ["Attend a short audition with the music director."]),
 ("Media & Technical", "video", "Run sound, cameras, the livestream, projection and photography.", ["Shadow the team for a few Sundays."]),
 ("Sanctuary Keepers", "spark", "Prepare and care for the house of God before and after every service.", []),
 ("Children's Teachers", "child", "Teach and care for children in Children's Church every Sunday.", ["Complete a short child-safety briefing."]),
 ("Protocol & Hospitality", "star", "Look after first-time guests, visiting ministers and special programmes.", []),
 ("Welfare & Evangelism", "heart", "Visit and support members in need and take the gospel into our community.", []),
 ("Prayer Team", "pray", "Stand in the gap for the church, its pastors and its programmes.", []),
 ("Security & Car Park", "shield", "Keep everyone safe and help with parking on busy Sundays.", []),
]

VENUE = "RCCG Fuller's Field, Km 47 Lekki–Epe Expressway, beside DKK Pharmacy &amp; Supermarket, Oko-Ado, Lagos"
EVENTS = [
 dict(rule="nth,1,4", time="18:30", d="–", m="", tag="Monthly", meta="First Thursday · 6:30pm", title="Healing in His Wings",
      when='First Thursday of every month, 6:30pm. Next: <span class="next-full">–</span>',
      lead="A special Faith Clinic service of prayer for healing and restoration.",
      more=f"<ul><li>Ministering: Pastor (Mrs.) Abosede Obayomi</li><li>Host: Pastor Wole Obayomi</li><li>Theme scripture: Malachi 4:2</li><li>Venue: {VENUE}</li></ul>",
      img="event2.jpg", alt="Flyer for Healing in His Wings"),
 dict(rule="nth,3,0", time="10:30", d="–", m="", tag="Monthly", meta="Third Sunday · 10:30am", title="Arise and Shine",
      when='Third Sunday of every month, 10:30am. Next: <span class="next-full">–</span>',
      lead="Our monthly service of thanksgiving, prayer and breakthrough.",
      more=f"<ul><li>Held during the 10:30am second service</li><li>Come with your testimonies and prayer requests</li><li>Venue: {VENUE}</li></ul>",
      img="members27.jpg", alt="A pastor praying for a member at the altar"),
 dict(rule="date,11,31", time="21:00", d="31", m="Dec", tag="Yearly", meta="31 December · 9pm", title="Crossover Service",
      when="31 December, 9pm until we cross into the new year",
      lead="End the year in worship and thanksgiving and pray into the new one with us.",
      more=f"<ul><li>Host: Pastor Wole Obayomi</li><li>Venue: {VENUE}</li><li>Also live on YouTube @rccgfullersfield</li></ul>",
      img="event1.jpg", alt="Flyer for the Crossover Service"),
 dict(rule=None, time=None, d="Easter", m="Yearly", tag="Yearly", meta="Easter Sunday · 4pm", title="Easter Praise Concert",
      when="Easter Sunday, 4pm. Last held 12 April 2026",
      lead="Hope of Nations celebrates the risen Christ in song.",
      more="<ul><li>Worship, the Word, praise, drama, spoken word and more</li><li>Host: Pastor Wole Obayomi</li><li>Theme: He Is Risen (Matthew 28:6)</li><li>The 2027 date will be announced here.</li></ul>",
      img="event3.jpg", alt="Flyer for the Easter Praise Concert"),
]

FUNDS = [
 ("Tabernacle Fund", "Our church building project", "0212009335"),
 ("Mission Fund", "Evangelism and RCCG missions", "3490010950"),
 ("CSR", "Projects that serve our community", "0210002112"),
 ("Welfare", "Help for members and families in need", "0213000786"),
 ("Hope of Nations", "Our youth and young adults ministry", "3490030961"),
 ("Special Funds", "Special seeds, vows and projects", "0213061101"),
]

MV = ["To make heaven.",
      "To take as many people with us.",
      "To have a member of RCCG in every family of all nations.",
      "To accomplish No. 1 above, holiness will be our lifestyle.",
      "To accomplish No. 2 and 3 above, we will plant churches within five minutes walking distance in every city and town of developing countries and within five minutes driving distance in every city and town of developed countries.",
      "We will pursue these objectives until every Nation in the world is reached for the Lord Jesus Christ."]

# ------------------------------------------------------------------ shell
def header(active):
    def link(href, label):
        cur = ' aria-current="page"' if href == active else ""
        return f'<a href="{href}" class="nav-link"{cur}>{label}</a>'
    mega = "\n".join(
        f'          <a class="mega-card" href="{m["fn"]}"><div class="mega-tag">{m["tag"]}</div><h4>{m["name"]}</h4><p>{m["short"]}</p><span class="mega-link">Explore →</span></a>'
        for m in MINISTRIES)
    min_cur = ' aria-current="page"' if active in ["ministries.html"] + [m["fn"] for m in MINISTRIES] else ""
    return f'''  <header class="site-header" id="siteHeader">
    <a href="index.html" class="logo">
      <span class="logo-mark"><img src="{IMG}logo.png" alt=""></span>
      <span>Fuller's Field Parish<small>The Redeemed Christian Church of God</small></span>
    </a>
    <nav class="main-nav" id="mainNav" aria-label="Main">
      <ul>
        <li>{link("index.html", "Home")}</li>
        <li>{link("about.html", "About")}</li>
        <li class="has-mega">
          <a href="ministries.html" class="nav-link"{min_cur}>Ministries {ic("chev")}</a>
          <div class="mega-panel">
{mega}
          </div>
        </li>
        <li>{link("workers.html", "Serve")}</li>
        <li>{link("events.html", "Events")}</li>
        <li>{link("contact.html", "Contact")}</li>
      </ul>
      <div class="mobile-extra">
        <a href="give.html" class="btn btn-red">{ic("heart")} Give</a>
        <a href="{YT}" target="_blank" rel="noopener" class="btn btn-outline"><span class="live-dot"></span> Watch live</a>
      </div>
    </nav>
    <div class="header-actions">
      <a href="{YT}" target="_blank" rel="noopener" class="live-btn"><span class="live-dot"></span> Live</a>
      <div class="socials">
        <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{FB_SVG}</a>
        <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{IG_SVG}</a>
        <a href="{YT}" target="_blank" rel="noopener" aria-label="YouTube">{YT_SVG}</a>
      </div>
      <a href="give.html" class="btn btn-red give-nav">{ic("heart")} Give</a>
      <button class="hamburger" id="hamburgerBtn" type="button" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </header>
'''

FOOTER = f'''  <footer class="site-footer" id="contact">
    <div class="footer-grid">
      <div>
        <div class="footer-logo"><span class="logo-mark"><img src="{IMG}logo.png" alt=""></span> Fuller's Field Parish</div>
        <p>A parish of The Redeemed Christian Church of God.</p>
        <address style="margin-top:10px">{ADDRESS}</address>
      </div>
      <div><h5>Quick links</h5><ul><li><a href="about.html">About</a></li><li><a href="ministries.html">Ministries</a></li><li><a href="workers.html">Serve</a></li><li><a href="events.html">Events</a></li><li><a href="give.html">Give</a></li></ul></div>
      <div><h5>Services</h5><ul><li>Sun · 7:30am &amp; 10:30am</li><li>Sun · 9:30am Sunday School &amp; Hope of Nations</li><li>Tue · Digging Deep 6:30pm</li><li>Thu · Faith Clinic 6:30pm</li></ul></div>
      <div><h5>Contact</h5><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{YT}" target="_blank" rel="noopener">YouTube</a> · <a href="{FB}" target="_blank" rel="noopener">Facebook</a> · <a href="{IG}" target="_blank" rel="noopener">Instagram</a></li></ul></div>
    </div>
    <div class="footer-bottom">© <span data-year>2026</span> Fuller's Field Parish · The Redeemed Christian Church of God</div>
  </footer>
'''

FAB = f'  <a class="fab-give" href="give.html"><span class="fab-ic">{ic("heart")}</span>Give</a>\n'

CLOSE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
EV_DIALOG = f'''  <dialog class="ev-dialog" id="evDialog" aria-label="Event details">
    <button class="ev-close" type="button" aria-label="Close">{CLOSE_SVG}</button>
    <div class="inner">
      <div class="flyer"><img src="" alt=""></div>
      <div class="details">
        <h3>Event</h3>
        <p class="when"></p>
        <div class="desc"></div>
        <div class="btn-row" style="margin-top:8px">
          <a class="btn btn-red btn-sm" href="{YT}" target="_blank" rel="noopener">Watch live</a>
          <a class="btn btn-line btn-sm" href="contact.html">Ask a question</a>
        </div>
      </div>
    </div>
  </dialog>
'''
PHOTO_DIALOG = f'''  <dialog class="ev-dialog photo-dialog" id="photoDialog" aria-label="Photo">
    <button class="ev-close" type="button" aria-label="Close">{CLOSE_SVG}</button>
    <img src="" alt="">
  </dialog>
'''

def page(fn, title, desc, main, active=None, fab=True, extra=""):
    out = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#22125F">
  <link rel="icon" href="{IMG}logo.png">
  <link rel="preload" href="fonts/fraunces.woff" as="font" type="font/woff" crossorigin>
  <link rel="preload" href="fonts/jakarta.woff" as="font" type="font/woff" crossorigin>
  <link rel="stylesheet" href="style.css">
  <script>document.documentElement.classList.add("js")</script>
</head>
<body>
{header(active or fn)}
  <main id="main">
{main.rstrip()}
  </main>

{FOOTER}{FAB if fab else ""}{extra}
  <script src="script.js"></script>
</body>
</html>
'''
    open(os.path.join(ROOT, fn), "w").write(out)

def page_hero(img, eyebrow, title, sub, buttons="", card="", pos="center"):
    btns = f'\n          <div class="btn-row">{buttons}</div>' if buttons else ""
    return f'''    <section class="page-hero" style="background-image:url('{IMG}{img}'); background-position:{pos}">
      <div class="hero-inner">
        <div class="hero-copy">
          <span class="eyebrow" style="color:var(--gold-light)">{eyebrow}</span>
          <h1>{title}</h1>
          <p class="hero-sub">{sub}</p>{btns}
        </div>{card}
      </div>
    </section>'''

def person_card(img, name, title, quote):
    return f'''
        <div class="person-card">
          <img src="{IMG}{img}" alt="{name}">
          <div><div class="p-name">{name}</div><div class="p-title">{title}</div><div class="p-quote">“{quote}”</div></div>
        </div>'''

COUNTDOWN = f'''    <div class="countdown" data-countdown>
      <div class="cd-label"><span class="cd-eyebrow">Next gathering</span><span class="cd-name">Sunday · First Service</span></div>
      <div class="cd-timer">
        <div class="cd-unit"><span data-u="d">00</span><small>Days</small></div><span class="cd-sep">:</span>
        <div class="cd-unit"><span data-u="h">00</span><small>Hrs</small></div><span class="cd-sep">:</span>
        <div class="cd-unit"><span data-u="m">00</span><small>Min</small></div><span class="cd-sep">:</span>
        <div class="cd-unit"><span data-u="s">00</span><small>Sec</small></div>
      </div>
      <span class="cd-live"><span class="live-dot"></span> Join us in church or online</span>
      <a href="{YT}" target="_blank" rel="noopener" class="cd-watch">{ic("play")} Watch live</a>
    </div>'''

def flow_step(icon, time, name):
    return f'''            <div class="flow-step"><div class="fs-icon">{ic_plain(icon)}</div><div><div class="fs-time">{time}</div><div class="fs-name">{name}</div></div></div>'''

SERVICES = f'''    <section class="section" id="services">
      <div class="wrap">
        <div class="head-c reveal"><span class="eyebrow">Our rhythm</span><h2 class="h2">Worship Service Times</h2><p>Every service also streams live on YouTube and Facebook @rccgfullersfield.</p></div>
        <div class="sunday-flow reveal">
          <div class="flow-label"><h3>Sunday Mornings</h3><span class="flow-badge">Weekly</span></div>
          <div class="flow-steps">
{flow_step("sun", "7:30 – 9:30 AM", "First Service")}
{flow_step("book", "9:30 – 10:30 AM", "Sunday School<br>Bible Study")}
{flow_step("users", "9:30 – 11:00 AM", "Hope of Nations<br>Youth Service")}
{flow_step("church", "10:30 AM – 12:00 PM", "Second Service")}
          </div>
        </div>
        <div class="midweek-row reveal">
          <div class="ticket"><div class="ticket-stub">Tue</div><div class="ticket-body"><h4>Digging Deep</h4><p class="ticket-time">6:30 – 7:45 PM</p><p class="ticket-desc">Interactive midweek Bible study.</p></div></div>
          <div class="ticket"><div class="ticket-stub">Thu</div><div class="ticket-body"><h4>Faith Clinic</h4><p class="ticket-time">6:30 – 7:45 PM</p><p class="ticket-desc">A powerful prayer encounter.</p></div></div>
        </div>
        <div class="spotlight reveal">
          <div><small>Monthly special service</small><h3>Arise and Shine</h3><p>Every third Sunday: thanksgiving, prayer and breakthrough.</p></div>
          <a href="events.html" class="btn btn-outline">See all events</a>
        </div>
        <div class="first-grid swipe reveal">
          <div class="first-card card"><span class="ic">{ic_plain("users")}</span><h4>When You Arrive</h4><p>Our ushers will welcome you at the door and help you find a seat. Come as you are.</p></div>
          <div class="first-card card"><span class="ic">{ic_plain("child")}</span><h4>Bringing Children</h4><p>Children's Church runs during service, so kids learn about Jesus while you worship.</p></div>
          <div class="first-card card"><span class="ic">{ic_plain("play")}</span><h4>Can't Come in Person?</h4><p>Every service streams live on YouTube and Facebook @rccgfullersfield.</p></div>
        </div>
        <div class="location-box reveal">
          <div class="location-map"><iframe title="Map showing RCCG Fuller's Field" src="https://www.google.com/maps?q=Km+47+Lekki-Epe+Expressway+Sangotedo+Ajah+Lagos&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
          <div class="location-info"><h4>Visit Us</h4><p>{ADDRESS}</p><a href="{MAPS}" target="_blank" rel="noopener" class="btn btn-red btn-sm">Get Directions</a></div>
        </div>
      </div>
    </section>'''

def event_card(e):
    r = f' data-rule="{e["rule"]}" data-time="{e["time"]}"' if e["rule"] else ""
    return f'''          <article class="event-card"{r} tabindex="0" role="button" aria-label="Open the flyer for {html.escape(e["title"])}">
            <div class="event-img"><img src="{IMG}{e["img"]}" alt="{e["alt"]}" loading="lazy"><div class="date-badge"><span class="d">{e["d"]}</span><span class="m">{e["m"]}</span></div></div>
            <div class="event-body">
              <div class="event-meta"><span class="ev-tag">{e["tag"]}</span><span>{e["meta"]}</span></div>
              <h3>{e["title"]}</h3>
              <p>{e["lead"]}</p>
              <span class="ev-when" hidden>{e["when"]}</span>
              <div class="ev-more">{e["more"]}</div>
              <span class="btn-text">View flyer →</span>
            </div>
          </article>'''

def events_section(eyebrow="What's coming up", title="Upcoming Events"):
    cards = "\n".join(event_card(e) for e in EVENTS)
    return f'''    <section class="section events-sec" id="events">
      <div class="wrap">
        <div class="head-c reveal"><span class="eyebrow">{eyebrow}</span><h2 class="h2">{title}</h2><p>Tap an event to see its flyer and details.</p></div>
        <div class="events-grid swipe">
{cards}
        </div>
        <p class="swipe-hint">Swipe to see more</p>
      </div>
    </section>'''

def ministry_card(m):
    return f'''          <a class="ministry-card" href="{m["fn"]}">
            <img src="{IMG}{m["hero"]}" alt="{m["name"]}" loading="lazy">
            <div class="ministry-body"><small>{m["tag"]}</small><h3>{m["name"]}</h3><p>{m["short"]}</p><span class="go">Learn more →</span></div>
          </a>'''

def ministries_section(title="Our Ministries", eyebrow="Find your place"):
    cards = "\n".join(ministry_card(m) for m in MINISTRIES)
    return f'''    <section class="section ministries-sec on-dark" id="ministries">
      <div class="head-c reveal"><span class="eyebrow">{eyebrow}</span><h2 class="h2">{title}</h2><p>A family within the family for every age and season.</p></div>
      <div class="ministry-grid swipe reveal">
{cards}
      </div>
      <p class="swipe-hint">Swipe to see more</p>
    </section>'''

def leader_card(img, name, role, bio, pos="center 18%"):
    return f'''        <article class="leader-card">
          <div class="leader-img"><img src="{IMG}{img}" alt="{name}" loading="lazy" style="object-position:{pos}"></div>
          <div class="leader-info"><h3>{name}</h3><p class="leader-role">{role}</p><p class="leader-bio">{bio}</p></div>
        </article>'''

LEADERS = "\n".join([
  leader_card("pastor-portrait.jpg", "Wole Obayomi", "Pastor-in-Charge", "Leads with a heart for discipleship and community transformation."),
  leader_card("pastor-mrs-portrait.jpg", "Bose Obayomi", "Mother of the Parish", "Nurtures the flock with wisdom, prayer and care for families."),
  leader_card("assistant1.jpg", "Imoh Akpan", "Assistant Pastor", "Faithfully supports pastoral care and the running of the parish.", "30% 20%"),
  leader_card("assistant2.jpg", "Patience Akpan", "Assistant Leader", "Serves with grace and compassion.", "70% 30%"),
])

GIVE_STRIP = f'''    <section class="give-strip on-dark" id="give">
      <span class="eyebrow">Sow a seed</span>
      <h2>Give Cheerfully, Give in Faith</h2>
      <p>Your tithes, offerings and seeds help us care for families and reach our community with the gospel.</p>
      <a href="give.html" class="btn btn-red">{ic("heart")} Give Online</a>
    </section>'''

# ------------------------------------------------------------------ HOME
DEPT_TILES = "\n".join(f'          <a class="dept-tile" href="workers.html#departments"><span class="ic">{ic_plain(i)}</span><strong>{html.escape(n)}</strong></a>' for n, i, _d, _e in DEPTS)
def gi(cls, img, alt):
    return f'          <div class="g-item {cls}"><img src="{IMG}{img}" alt="{alt}" loading="lazy"></div>'
GALLERY = "\n".join([
  gi("g-tall", "members25.jpg", "A mother in a green hat smiling with her baby"),
  gi("g-small", "members16.jpg", "A member singing in worship"),
  gi("g-xtall", "members26.jpg", "A member dancing in praise"),
  gi("g-med", "members23.jpg", "Members greeting one another"),
  gi("g-wide", "members15.jpg", "A minister at the keyboard"),
  gi("g-tall", "members19.jpg", "A woman in a wide hat carrying a child"),
  gi("g-small", "members6.jpg", "A man praying"),
  gi("g-med", "community1.jpg", "Two women embracing after service"),
  gi("g-xtall", "members13.jpg", "A minister speaking"),
  gi("g-wide", "members8.jpg", "The congregation in worship"),
  gi("g-med", "wisemen.jpg", "The Wise Men celebrating"),
  gi("g-tall", "members10.jpg", "A woman singing in worship"),
])

def slide(img, pos, h1, sub, btns, card=""):
    return f'''      <div class="hero-slide{{active}}" style="background-image:url('{IMG}{img}'); background-position:{pos}">
        <div class="hero-inner">
          <div class="hero-copy">
            <h1>{h1}</h1>
            <p class="hero-sub">{sub}</p>
            <div class="btn-row">{btns}</div>
          </div>{card}
        </div>
      </div>'''

slides = [
  slide("churchbuilding.jpg", "center 40%", "Take a Step Toward the Light",
        "Discover faith, hope and a family for your soul. Whatever season you're in, there's a seat for you here.",
        f'<a href="#services" class="btn btn-red">Join Us This Sunday</a><a href="{YT}" target="_blank" rel="noopener" class="btn btn-outline">Watch Live</a>',
        person_card("pastor-portrait.jpg", "Pastor Wole Obayomi", "Pastor-in-Charge", "Welcome home. Come as you are and discover God's purpose for you.")),
  slide("community1.jpg", "center 35%", "To Make Heaven, Together",
        "We exist to reach the lost and raise disciples who make heaven, taking as many people with us as possible.",
        '<a href="about.html#mission" class="btn btn-red">Our Mission &amp; Vision</a>',
        person_card("generaloverseerheadshot.jpg", "Pastor E.A. Adeboye", "General Overseer, RCCG", "Our mandate is simple: to make heaven, and to take as many people with us as possible.")),
  slide("members17.jpg", "center 30%", "Raising a Generation on Fire for God",
        "Hope of Nations meets every Sunday at 9:30am. Young people, there's a place for you.",
        '<a href="hope-of-nations.html" class="btn btn-red">Meet Hope of Nations</a><a href="ministries.html" class="btn btn-outline">All Ministries</a>'),
  slide("offeringhero.jpg", "center", "Sow a Seed, Reap a Harvest",
        "Giving is an act of worship. Every seed sown here helps us reach our community and beyond.",
        f'<a href="give.html" class="btn btn-red">{ic("heart")} Give / Sow a Seed</a><a href="workers.html" class="btn btn-outline">Serve With Us</a>'),
]
slides_html = "\n".join(s.replace("{active}", " active" if i == 0 else "") for i, s in enumerate(slides))
dots_html = "".join(f'<button{" class=\"active\"" if i == 0 else ""} data-i="{i}" aria-label="Slide {i+1}"></button>' for i in range(len(slides)))

home = f'''    <section class="hero" id="home">
{slides_html}
      <div class="hero-dots" id="heroDots">{dots_html}</div>
    </section>

{COUNTDOWN}

    <section class="stats">
      <div class="stats-grid">
        <div><div class="stat-number">12+</div><div class="stat-label">Years of Faith</div></div>
        <div><div class="stat-number">5</div><div class="stat-label">Active Ministries</div></div>
        <div><div class="stat-number">5</div><div class="stat-label">Weekly Gatherings</div></div>
        <div><div class="stat-number">1,000+</div><div class="stat-label">Lives Impacted</div></div>
      </div>
    </section>

    <section class="section" id="welcome">
      <div class="welcome reveal">
        <div class="welcome-photo"><img src="{IMG}pastor-portrait.jpg" alt="Pastor Wole Obayomi"></div>
        <div class="welcome-text">
          <span class="eyebrow">A word from our Pastor</span>
          <h2 class="h2">Welcome Home</h2>
          <p>Whether this is your first visit or you have worshipped with us for years, I am glad you are here. Fuller's Field is a family devoted to loving God, loving people and doing good.</p>
          <div class="scripture-box"><p>“I was glad when they said unto me, Let us go into the house of the LORD.”</p><span>Psalm 122:1</span></div>
          <p>Whatever season you are in, there is a seat for you, a family to belong to and a God who has a purpose for your life. Come as you are.</p>
          <div class="signature"><img src="{IMG}pastor-portrait.jpg" alt=""><div><strong>Pastor Wole Obayomi</strong><span>Pastor-in-Charge</span></div></div>
        </div>
      </div>
    </section>

    <section class="section leadership" id="leadership">
      <div class="head-c reveal"><span class="eyebrow">Our leadership</span><h2 class="h2">Meet Our Pastoral Team</h2><p>Devoted leaders serving with love and vision.</p></div>
      <div class="leader-grid swipe reveal">
{LEADERS}
      </div>
      <p class="swipe-hint">Swipe to see more</p>
    </section>

    <section class="gallery on-dark" aria-labelledby="gal-title">
      <div class="gallery-head"><span class="eyebrow">Life at Fuller's Field</span><h2 class="h2" id="gal-title">Moments From Our Family</h2></div>
      <div class="marquee" id="marquee">
{GALLERY}
      </div>
      <div class="gallery-foot"><a href="{FB}" target="_blank" rel="noopener" class="btn-text">More photos on Facebook →</a></div>
    </section>

{SERVICES}

{events_section()}

{ministries_section()}

    <section class="section" id="serve">
      <div class="serve-home reveal">
        <div>
          <span class="eyebrow">Serve with us</span>
          <h2 class="h2">Serve in God's House</h2>
          <p class="sub">Sundays at Fuller's Field run on willing hands. Every worker starts with Workers in Training (WIT).</p>
          <ol class="wit-mini">
            <li><span><strong>Worship with us</strong> on Sundays</span></li>
            <li><span><strong>Register for WIT</strong> at the parish office or by email</span></li>
            <li><span><strong>Join a department</strong> and start serving</span></li>
          </ol>
          <div class="btn-row"><a href="workers.html#wit" class="btn btn-red">Become a Worker</a><a href="workers.html" class="btn btn-line">All Departments</a></div>
        </div>
        <div class="dept-tiles">
{DEPT_TILES}
        </div>
      </div>
    </section>

    <section class="cta-banner" style="background-image:url('{IMG}members8.jpg')">
      <h2>Ready to Take Your Next Step?</h2>
      <p>There is a place for your gifts and a family for your journey. Join a ministry, or serve in God's house through Workers in Training.</p>
      <div class="cta-buttons">
        <a href="ministries.html" class="btn btn-white">Join a Ministry</a>
        <a href="workers.html" class="btn btn-white">Become a Worker</a>
        <a href="#services" class="btn btn-red">Plan a Visit</a>
      </div>
    </section>

{GIVE_STRIP}'''
page("index.html", "Fuller's Field Parish | RCCG, Lekki–Epe Expressway",
     "RCCG Fuller's Field Parish, Km 47 Lekki–Epe Expressway, Lagos. Sunday services 7:30am and 10:30am. Hope of Nations 9:30am.",
     home, extra=EV_DIALOG)

# ------------------------------------------------------------------ ABOUT
mv_items = "\n".join(f"          <li><p>{t}</p></li>" for t in MV)
about = f'''{page_hero("members23.jpg", "About us", "We Are Fuller's Field", "A place of hope, love and spiritual transformation, rooted in The Redeemed Christian Church of God.",
   '<a href="#story" class="btn btn-red">Our Story</a><a href="#pastors" class="btn btn-outline">Meet Our Pastors</a>',
   person_card("generaloverseerheadshot.jpg", "Pastor E.A. Adeboye", "General Overseer, RCCG", "Our mandate is simple: to make heaven, and to take as many people with us as possible."), "center 35%")}

    <section class="section" id="story">
      <div class="split reveal">
        <div class="photo"><img src="{IMG}churchbuilding.jpg" alt="The Fuller's Field church building"></div>
        <div>
          <span class="eyebrow">Who we are</span>
          <h2 class="h2">A Place Where Faith Meets Family</h2>
          <p>Fuller's Field Parish is a home for seekers, believers and families looking to anchor their lives in Jesus Christ. As a parish of the Redeemed Christian Church of God, we are rooted in timeless biblical truth.</p>
          <p>Located on the Lekki–Epe Expressway in Sangotedo, our church family is dedicated to helping every person encounter the love of God, heal from the past and step into their God-given purpose.</p>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="head-c reveal"><span class="eyebrow">Our journey</span><h2 class="h2">How God Has Led Us</h2></div>
      <ul class="timeline swipe reveal">
        <li class="card"><p class="yr">2012</p><h3>The Foundation</h3><p>Fuller's Field Parish was planted to serve families along the Lekki–Epe corridor.</p></li>
        <li class="card"><p class="yr">2016</p><h3>Expanding Ministries</h3><p>Hope of Nations began, alongside fellowships for our seniors.</p></li>
        <li class="card"><p class="yr">2020</p><h3>Reaching Further</h3><p>Services began streaming online as our outreach grew.</p></li>
        <li class="card"><p class="yr">Today</p><h3>Growing Stronger</h3><p>Making disciples and shining God's light in Sangotedo and beyond.</p></li>
      </ul>
    </section>

    <section class="section mv on-dark" id="mission">
      <div class="head-c reveal"><span class="eyebrow">The RCCG mandate</span><h2 class="h2">Mission &amp; Vision</h2></div>
      <ol class="mv-list reveal">
{mv_items}
      </ol>
    </section>

    <section class="section">
      <div class="head-c reveal"><span class="eyebrow">What guides us</span><h2 class="h2">Our Core Values</h2></div>
      <ul class="values-grid swipe reveal">
        <li class="card"><h3>The Word First</h3><p>The Bible is our foundation and final authority.</p></li>
        <li class="card"><h3>Open Arms</h3><p>Come as you are. Everyone belongs here.</p></li>
        <li class="card"><h3>Prayer &amp; Worship</h3><p>We seek God's presence with praise and prayer.</p></li>
        <li class="card"><h3>Every Generation</h3><p>From children to our Wise Women and Men.</p></li>
      </ul>
    </section>

    <section class="section leadership" id="pastors">
      <div class="head-c reveal"><span class="eyebrow">Servant leaders</span><h2 class="h2">Our Pastors</h2></div>
      <article class="pastor-row card reveal">
        <img src="{IMG}p1andwifecontemp.jpg" alt="Pastor Wole and Pastor (Mrs.) Bose Obayomi">
        <div>
          <h3>Pastor Wole &amp; Pastor (Mrs.) Bose Obayomi</h3>
          <p class="leader-role">Pastor-in-Charge</p>
          <p>Pastor Wole and Pastor (Mrs.) Bose Obayomi lead Fuller's Field Parish. Their heart is to build a warm, Christ-centred church where people from all walks of life can meet God, heal and grow.</p>
          <p>Pastor Wole brings a passionate teaching ministry focused on purpose and spiritual growth, while Pastor Bose shepherds families, women's fellowship and welfare.</p>
        </div>
      </article>
      <article class="pastor-row card reveal">
        <img src="{IMG}assistant1.jpg" alt="Pastor Imoh Akpan" style="object-position:30% 20%">
        <div>
          <h3>Pastor Imoh &amp; Patience Akpan</h3>
          <p class="leader-role">Assistant Pastor</p>
          <p>Pastor Imoh serves as Assistant Pastor alongside his wife, Patience. Together they oversee ministry administration, pastoral care and welcoming new members, so everyone finds connection and support.</p>
        </div>
      </article>
      <div class="go-card card reveal">
        <img src="{IMG}generaloverseerheadshot.jpg" alt="Pastor E.A. Adeboye">
        <div><h3>Part of a Worldwide Family</h3><p>Fuller's Field is a parish of The Redeemed Christian Church of God, led by our General Overseer, Pastor E.A. Adeboye.</p><a href="https://www.rccg.org" target="_blank" rel="noopener" class="btn-text">Visit rccg.org →</a></div>
      </div>
    </section>

{GIVE_STRIP}'''
page("about.html", "About | Fuller's Field Parish", "Our story, the RCCG mission and vision, our values and pastors at Fuller's Field Parish, Sangotedo, Lagos.", about)

# ------------------------------------------------------------------ MINISTRIES OVERVIEW
mins = f'''{page_hero("members8.jpg", "Find your place", "Our Ministries", "Church is more than Sunday. Each ministry is a family where you can grow, be known and serve.", '<a href="#list" class="btn btn-red">Explore Ministries</a><a href="workers.html" class="btn btn-outline">Serve in a Department</a>', pos="center 30%")}

    <section class="section" id="list">
      <div class="head-c reveal"><span class="eyebrow">Ministries</span><h2 class="h2">Choose a Ministry</h2><p>Tap a ministry to see photos, meeting times and how to join.</p></div>
      <div class="ministry-grid swipe reveal">
{chr(10).join(ministry_card(m) for m in MINISTRIES)}
      </div>
      <p class="swipe-hint">Swipe to see more</p>
    </section>

    <section class="cta-banner" style="background-image:url('{IMG}members15.jpg')">
      <h2>Want to Serve Too?</h2>
      <p>Use your gifts in one of our departments. Every worker starts with Workers in Training.</p>
      <div class="cta-buttons"><a href="workers.html" class="btn btn-white">See Departments</a></div>
    </section>'''
page("ministries.html", "Ministries | Fuller's Field Parish", "Hope of Nations, Children's Church, Wise Women and Wise Men at RCCG Fuller's Field Parish.", mins)

# ------------------------------------------------------------------ MINISTRY PAGES
for m in MINISTRIES:
    acts = "\n".join(f'          <li class="card"><span class="ic">{ic_plain(i)}</span><div><strong>{t}</strong><span>{d}</span></div></li>' for i, t, d in m["acts"])
    gal = "\n".join(f'        <button type="button" aria-label="Enlarge photo {k+1}"><img src="{IMG}{g}" alt="{m["name"]}, photo {k+1}" loading="lazy"></button>' for k, g in enumerate(m["gallery"]))
    steps = "\n".join(f'        <li class="card"><strong>{t}</strong><span>{d}</span></li>' for t, d in m["steps"])
    others = "\n".join(ministry_card(o) for o in MINISTRIES if o is not m)
    about_p = "\n".join(f"          <p>{p}</p>" for p in m["about"])
    body = f'''{page_hero(m["hero"], m["tag"], m["name"], m["short"], '<a href="#join" class="btn btn-red">How to Join</a><a href="ministries.html" class="btn btn-outline">All Ministries</a>', pos="center 30%")}

    <div class="facts">
      <div class="card"><small>When</small><strong>{m["when"]}</strong></div>
      <div class="card"><small>Who</small><strong>{m["who"]}</strong></div>
      <div class="card"><small>Where</small><strong>Fuller's Field, Km 47 Lekki–Epe Expy</strong></div>
    </div>

    <section class="section">
      <div class="split reveal" style="align-items:start">
        <div>
          <span class="eyebrow">About us</span>
          <h2 class="h2">Welcome to {m["name"]}</h2>
{about_p}
        </div>
        <ul class="acts">
{acts}
        </ul>
      </div>
    </section>

    <section class="section leadership">
      <div class="head-c reveal"><span class="eyebrow">Moments</span><h2 class="h2">{m["name"]} in Pictures</h2><p>Tap a photo to see it bigger.</p></div>
      <div class="photo-grid reveal">
{gal}
      </div>
    </section>

    <section class="section" id="join">
      <div class="head-c reveal"><span class="eyebrow">Join us</span><h2 class="h2">How to Join</h2></div>
      <ol class="steps-grid swipe reveal">
{steps}
      </ol>
      <div class="reach reveal">
        <p>Prefer to reach out first? Email us or call the parish office and we'll connect you with the {m["name"]} leaders.</p>
        <div class="btn-row">
          <a class="btn btn-red btn-sm" href="{mailto("I want to join " + html.unescape(m["name"]), "Hello, my name is ... and I would like to join " + html.unescape(m["name"]) + ". My phone number is ...")}">{ic("mail")} Email Us</a>
          <a class="btn btn-white btn-sm" href="tel:{TEL}">{ic("phone")} {PHONE}</a>
        </div>
      </div>
    </section>

    <section class="section ministries-sec on-dark">
      <div class="head-c reveal"><span class="eyebrow">Keep exploring</span><h2 class="h2">Other Ministries</h2></div>
      <div class="ministry-grid swipe reveal" style="grid-template-columns:repeat(3,1fr)">
{others}
      </div>
    </section>'''
    page(m["fn"], f"{html.unescape(m['name'])} | Fuller's Field Parish", f"{html.unescape(m['name'])} at RCCG Fuller's Field Parish. {m['when']}.", body, active=m["fn"], extra=PHOTO_DIALOG)

# ------------------------------------------------------------------ WORKERS
def dept_card(name, icon, desc, extra):
    plain = html.unescape(name)
    steps = ["Worship with us regularly at Fuller's Field.", "Register for Workers in Training (WIT).",
             f"Tell us you'd like to join {plain}; we'll introduce you to the head of department."] + extra + ["Start serving after training."]
    lis = "".join(f"<li><span>{html.escape(s)}</span></li>" for s in steps)
    return f'''        <article class="dept-card card">
          <span class="ic">{ic_plain(icon)}</span>
          <h3>{html.escape(name)}</h3>
          <p>{desc}</p>
          <details>
            <summary>How to join</summary>
            <ol class="mini-steps">{lis}</ol>
            <a class="btn btn-red btn-sm" href="{mailto("I want to join " + plain, "Hello, my name is ... and I would like to join " + plain + ". My phone number is ...")}">{ic("mail")} Email to join</a>
          </details>
        </article>'''

workers = f'''{page_hero("members15.jpg", "Serve with us", "Serve in God's House", "Use your gifts to bless others. Pick a department, see how to join and reach us in one tap.", '<a href="#wit" class="btn btn-red">Become a Worker</a><a href="#departments" class="btn btn-outline">See Departments</a>', pos="center 30%")}

    <section class="section" id="wit">
      <div class="wit reveal">
        <div>
          <span class="eyebrow">Start here</span>
          <h2 class="h2">Workers in Training</h2>
          <p class="sub">Every worker at Fuller's Field begins with Workers in Training (WIT), the RCCG course that grounds you in the faith and prepares you to serve.</p>
          <div class="btn-row"><a class="btn btn-red" href="{mailto("Register me for Workers in Training", "Hello, my name is ... and I would like to register for Workers in Training. My phone number is ...")}">{ic("mail")} Register for WIT</a></div>
        </div>
        <ol class="wit-steps">
          <li class="card"><div><strong>Worship with us</strong><span>Be part of the Fuller's Field family on Sundays.</span></div></li>
          <li class="card"><div><strong>Register for WIT</strong><span>Sign up at the parish office or by email.</span></div></li>
          <li class="card"><div><strong>Join a department</strong><span>Choose where to serve and start after training.</span></div></li>
        </ol>
      </div>
    </section>

    <section class="section leadership" id="departments">
      <div class="head-c reveal"><span class="eyebrow">Departments</span><h2 class="h2">Where You Can Serve</h2><p>Tap “How to join” on any department.</p></div>
      <div class="dept-grid reveal">
{chr(10).join(dept_card(*d) for d in DEPTS)}
      </div>
    </section>

    <section class="cta-banner" style="background-image:url('{IMG}members23.jpg')">
      <h2>Not Sure Where You Fit?</h2>
      <p>Talk to us and we'll help you find the right place to serve.</p>
      <div class="cta-buttons"><a href="{mailto("Help me find a department")}" class="btn btn-white">Email Us</a><a href="tel:{TEL}" class="btn btn-red">Call {PHONE}</a></div>
    </section>'''
page("workers.html", "Serve | Fuller's Field Parish", "Departments at RCCG Fuller's Field Parish and how to join, starting with Workers in Training.", workers)

# ------------------------------------------------------------------ EVENTS
events = f'''{page_hero("members27.jpg", "What's on", "Events &amp; Programmes", "Monthly special services, yearly celebrations and our weekly rhythm. Tap any event to see its flyer.", '<a href="#events" class="btn btn-red">Upcoming Events</a>', pos="center 30%")}

{COUNTDOWN}

{events_section("Mark your calendar", "Upcoming Events")}

{SERVICES}

    <section class="section leadership">
      <div class="head-c reveal"><span class="eyebrow">With the wider RCCG family</span><h2 class="h2">RCCG Programmes</h2><p>Held at Redemption City and streamed online. See rccg.org for exact dates.</p></div>
      <ul class="values-grid swipe reveal" style="grid-template-columns:repeat(3,1fr)">
        <li class="card"><h3>Holy Ghost Service</h3><p>First Friday of every month, with our General Overseer.</p></li>
        <li class="card"><h3>Annual Convention</h3><p>Every August at Redemption City.</p></li>
        <li class="card"><h3>Holy Ghost Congress</h3><p>Every December at Redemption City.</p></li>
      </ul>
    </section>'''
page("events.html", "Events | Fuller's Field Parish", "Monthly special services, yearly events and service times at RCCG Fuller's Field Parish.", events, extra=EV_DIALOG)

# ------------------------------------------------------------------ GIVE
funds = "\n".join(f'''        <article class="fund card">
          <h3>{n}</h3>
          <p>{u}</p>
          <div class="row"><span class="num">{num}</span>{copy_btn(num, aria="Copy " + n + " account number")}</div>
        </article>''' for n, u, num in FUNDS)
give = f'''{page_hero("offeringhero.jpg", "Sow a seed", "Give Cheerfully, Give in Faith", "Your tithes, offerings and seeds fund ministry, missions and care for families. Thank you for giving.")}

    <div style="padding:0 6vw">
      <div class="acct-main card">
        <small>Tithe, first fruit &amp; love offering</small>
        <h3>RCCG Fuller's Field</h3>
        <p class="bank">Ecobank Nigeria</p>
        <div class="acct-num-row"><span class="acct-num">0212009328</span>{copy_btn("0212009328", aria="Copy tithe account number")}</div>
        <p class="note">Always check that the account name reads <strong>RCCG Fuller's Field</strong> before you send.</p>
      </div>
    </div>

    <section class="section">
      <div class="head-c reveal"><span class="eyebrow">Online transfers</span><h2 class="h2">Choose Where Your Seed Goes</h2><p>All accounts are with Ecobank Nigeria, in the name RCCG Fuller's Field.</p></div>
      <div class="fund-grid reveal">
{funds}
      </div>
    </section>

    <section class="section leadership" id="ussd">
      <div class="ussd reveal">
        <div>
          <span class="eyebrow">No data? No problem</span>
          <h2 class="h2">Give via USSD</h2>
          <p class="sub">Give from any phone, even without internet.</p>
          <div class="ussd-code"><span class="code">*326#</span>{copy_btn("*326#", aria="Copy USSD code")}</div>
        </div>
        <ol class="num-steps">
          <li class="card"><span>Dial <strong>*326#</strong> from the number linked to your bank account and choose <strong>Transfer</strong>.</span></li>
          <li class="card"><span>Choose <strong>Ecobank</strong> as the receiving bank.</span></li>
          <li class="card"><span>Enter the account number for your fund, then the amount.</span></li>
          <li class="card"><span>Check the name reads <strong>RCCG Fuller's Field</strong>, then enter your PIN.</span></li>
        </ol>
      </div>
    </section>

    <section class="section">
      <div class="head-c reveal"><span class="eyebrow">Good to know</span><h2 class="h2">Giving FAQs</h2></div>
      <div class="faq reveal">
        <details class="card"><summary>Which account should I use for my tithe?</summary><p>Use the Tithe, first fruit &amp; love offering account (0212009328) for your tithe, first fruit and regular offerings.</p></details>
        <details class="card"><summary>Is my giving secure?</summary><p>Yes. All accounts are official Ecobank accounts in the name RCCG Fuller's Field. Always confirm the account name before completing a transfer.</p></details>
        <details class="card"><summary>Can I get a receipt?</summary><p>Yes. Contact the parish office after giving and we will send you a giving statement.</p></details>
      </div>
    </section>

    <section class="verse-strip">
      <p>“Give, and it shall be given unto you; good measure, pressed down, and shaken together, and running over.”</p>
      <cite>Luke 6:38</cite>
    </section>'''
page("give.html", "Give | Fuller's Field Parish", "Give your tithes and offerings to RCCG Fuller's Field by bank transfer or USSD. All accounts are with Ecobank Nigeria.", give, fab=False)

# ------------------------------------------------------------------ CONTACT
contact = f'''{page_hero("churchbuilding.jpg", "Get in touch", "We'd Love to Hear From You", "Visit us on Sunday, call the parish office, or send us a prayer request.", pos="center 40%")}

    <div class="contact-grid">
      <div class="contact-card card"><span class="ic">{ic_plain("pin")}</span><h3>Visit</h3><address>Km 47, Lekki–Epe Expressway, Oko-Ado, Sangotedo, Lagos</address><a class="btn btn-red btn-sm" href="{MAPS}" target="_blank" rel="noopener">Get Directions</a></div>
      <div class="contact-card card"><span class="ic">{ic_plain("phone")}</span><h3>Call</h3><span class="big">{PHONE}</span><p>The parish office</p><a class="btn btn-navy btn-sm" href="tel:{TEL}">Call Now</a></div>
      <div class="contact-card card"><span class="ic">{ic_plain("mail")}</span><h3>Email</h3><span class="big">rccgfullersfield@<wbr>gmail.com</span><a class="btn btn-navy btn-sm" href="mailto:{EMAIL}">Send an Email</a></div>
      <div class="contact-card card"><span class="ic">{ic_plain("play")}</span><h3>Watch &amp; Follow</h3><p>@rccgfullersfield on YouTube, Facebook and Instagram.</p><a class="btn btn-red btn-sm" href="{YT}" target="_blank" rel="noopener">Watch on YouTube</a></div>
    </div>

    <section class="section">
      <div class="location-box reveal" style="max-width:1100px">
        <div class="location-map"><iframe title="Map showing RCCG Fuller's Field" src="https://www.google.com/maps?q=Km+47+Lekki-Epe+Expressway+Sangotedo+Ajah+Lagos&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        <div class="location-info">
          <h4>Finding Us</h4>
          <ul class="landmarks">
            <li>Km 47, Lekki–Epe Expressway</li>
            <li>Beside DKK Pharmacy &amp; Supermarket</li>
            <li>Opposite Maple Plaza</li>
            <li>Farm Bus Stop, Oko-Ado</li>
          </ul>
          <p><strong>Sundays</strong> 7:30am &amp; 10:30am · <strong>Tue</strong> 6:30pm · <strong>Thu</strong> 6:30pm</p>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="prayer-box card reveal">
        <span class="eyebrow">Need prayer?</span>
        <h2 class="h2">You Don't Have to Carry It Alone</h2>
        <p>Send your prayer request to the parish office and our pastors will stand with you in prayer. Or join us at Faith Clinic on Thursdays at 6:30pm.</p>
        <div class="btn-row">
          <a class="btn btn-red" href="{mailto("Prayer request")}">{ic("mail")} Send a Prayer Request</a>
          {copy_btn(EMAIL, label="Copy email")}
        </div>
      </div>
    </section>'''
page("contact.html", "Contact | Fuller's Field Parish", "Address, directions, phone, email and prayer requests for RCCG Fuller's Field Parish, Km 47 Lekki–Epe Expressway, Lagos.", contact)

print("built")
