#!/usr/bin/env python3
"""Assemble the RCCG Fuller's Field site: shared header/footer + page bodies.

Run: python3 tools/build.py  (regenerates every .html page from this file and tools/prev_*.html)
"""
import os, re, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = os.path.dirname(os.path.abspath(__file__))
YT = "https://www.youtube.com/@rccgfullersfield"
EMAIL = "rccgfullersfield@gmail.com"
PHONE = "0803 303 0620"
TEL = "+2348033030620"

def prev(name):
    return open(f"{B}/prev_{name}.html").read()

def between(s, start, end):
    i = s.index(start); j = s.index(end, i)
    return s[i:j]

# ---------------------------------------------------------------- icons
I = {
 "heart": '<path d="M20.8 4.6a5.5 5.5 0 00-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 00-7.8 7.8l1 1.1L12 21l7.8-7.5 1-1.1a5.5 5.5 0 000-7.8z"/>',
 "users": '<path d="M17 21v-2a4 4 0 00-4-4H7a4 4 0 00-4 4v2"/><circle cx="10" cy="7" r="4"/><path d="M21 21v-2a4 4 0 00-3-3.9M16 3.1a4 4 0 010 7.8"/>',
 "music": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
 "video": '<rect x="2" y="5" width="15" height="14" rx="2"/><path d="M17 10l5-3v10l-5-3z"/>',
 "spark": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 17l.8 2.2L22 20l-2.2.8L19 23l-.8-2.2L16 20l2.2-.8z"/>',
 "child": '<circle cx="12" cy="5" r="3"/><path d="M12 8v7M8 21l4-6 4 6M7 11h10"/>',
 "star": '<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 "hands": '<path d="M12 21s-7-5-7-11V4l7 4 7-4v6c0 6-7 11-7 11z"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
 "book": '<path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "church": '<path d="M3 21h18M5 21V10l7-5 7 5v11M10 21v-5h4v5M12 2v3"/>',
 "fire": '<path d="M12 22c4 0 7-3 7-7 0-5-5-7-5-12-3 2-4 5-4 7-1-1-2-2-2-4-2 2-3 5-3 9 0 4 3 7 7 7z"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 010 20M12 2a15 15 0 000 20"/>',
 "home": '<path d="M3 11l9-8 9 8v10a1 1 0 01-1 1h-5v-7H9v7H4a1 1 0 01-1-1z"/>',
 "gift": '<rect x="3" y="8" width="18" height="13" rx="1"/><path d="M12 8v13M3 12h18M12 8S10 3 7.5 4 9 8 12 8zM12 8s2-5 4.5-4S15 8 12 8z"/>',
 "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0014 0M12 17v5"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8 9.9a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/>',
 "pray": '<path d="M12 3v8M8 21l-3-6 4-6 3 2 3-2 4 6-3 6"/>',
 "chat": '<path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/>',
 "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
}
def svg(name, extra=""):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{extra}>{I[name]}</svg>'

COPY_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 012-2h10"/></svg>'
def copy_btn(value, label="Copy", aria=None):
    a = f' aria-label="{aria}"' if aria else ""
    return f'<button class="copy-btn" type="button" data-copy="{value}"{a}>{COPY_SVG}<span class="lbl">{label}</span></button>'

def mailto(subject, body=""):
    from urllib.parse import quote
    q = "subject=" + quote(subject)
    if body: q += "&body=" + quote(body)
    return f"mailto:{EMAIL}?{q}"

# ---------------------------------------------------------------- shell
NAV = [("index.html", "Home"), ("about.html", "About"), ("ministries.html", "Ministries"),
       ("workers.html", "Serve"), ("events.html", "Events"), ("contact.html", "Contact")]

def header(active):
    items = "\n".join(
        f'          <li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f'''  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="index.html">
        <img src="images/web/logo.png" alt="" width="46" height="46">
        <span><span class="brand-name">Fuller's Field</span><span class="brand-sub">The Redeemed Christian Church of God</span></span>
      </a>
      <nav class="main-nav" aria-label="Main">
        <ul>
{items}
        </ul>
        <div class="mobile-actions">
          <a class="btn btn-red btn-give" href="give.html">{svg("heart")} Give</a>
          <a class="btn btn-line on-light" href="{YT}" target="_blank" rel="noopener"><span class="live-dot"></span> Watch live on YouTube</a>
        </div>
      </nav>
      <div class="header-actions">
        <a class="live-link" href="{YT}" target="_blank" rel="noopener"><span class="live-dot"></span><span class="lbl">Watch live</span></a>
        <a class="btn btn-red btn-give" href="give.html">{svg("heart")} Give</a>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-label="Open menu">
          <svg class="icon-open" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
          <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
        </button>
      </div>
    </div>
  </header>
'''

FOOTER = f'''  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">
            <img src="images/web/logo.png" alt="" width="52" height="52">
            <span><strong>Fuller's Field</strong>The Redeemed Christian Church of God</span>
          </div>
          <address>Km 47, Lekki–Epe Expressway, beside DKK Pharmacy &amp; Supermarket, opposite Maple Plaza, Farm Bus Stop, Oko-Ado, Lagos</address>
        </div>
        <div>
          <h4>Services</h4>
          <ul>
            <li>Sunday 7:30am &amp; 10:30am</li>
            <li>Sunday school 9:30am</li>
            <li>Hope of Nations 9:30am</li>
            <li>Tuesday 6:30pm, Digging Deep</li>
            <li>Thursday 6:30pm, Faith Clinic</li>
          </ul>
        </div>
        <div>
          <h4>Get involved</h4>
          <ul>
            <li><a href="give.html">Give</a></li>
            <li><a href="ministries.html">Ministries</a></li>
            <li><a href="workers.html">Serve in a department</a></li>
            <li><a href="events.html">Events</a></li>
            <li><a href="contact.html">Contact &amp; prayer</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="tel:{TEL}">{PHONE}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><a href="{YT}" target="_blank" rel="noopener">YouTube</a> · <a href="https://www.facebook.com/rccgfullersfield/" target="_blank" rel="noopener">Facebook</a></li>
            <li><a href="https://instagram.com/rccgfullersfield" target="_blank" rel="noopener">Instagram</a> · <a href="https://x.com/Fullers_Field" target="_blank" rel="noopener">X</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span data-year>2026</span> RCCG Fuller's Field</span>
        <a href="https://www.rccg.org" target="_blank" rel="noopener">A parish of The Redeemed Christian Church of God</a>
      </div>
    </div>
  </footer>
'''

FAB = f'''  <a class="fab-give" href="give.html"><span class="fab-ic">{svg("heart")}</span>Give</a>
'''

EV_DIALOG = f'''  <dialog class="ev-dialog" id="evDialog" aria-label="Event details">
    <button class="ev-close" type="button" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    <div class="inner">
      <div class="flyer"><img src="" alt=""></div>
      <div class="details">
        <h3>Event</h3>
        <p class="when"></p>
        <div class="desc"></div>
        <div class="btn-row">
          <a class="btn btn-red" href="{YT}" target="_blank" rel="noopener">Watch live on YouTube</a>
          <a class="btn btn-line on-light" href="contact.html">Ask a question</a>
        </div>
      </div>
    </div>
  </dialog>
'''
PHOTO_DIALOG = '''  <dialog class="ev-dialog photo-dialog" id="photoDialog" aria-label="Photo">
    <button class="ev-close" type="button" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    <img src="" alt="">
  </dialog>
'''

def page(fn, title, desc, main, active=None, fab=True, extra=""):
    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#28166F">
  <link rel="icon" href="images/web/logo.png">
  <link rel="preload" href="fonts/archivo-var.woff" as="font" type="font/woff" crossorigin>
  <link rel="stylesheet" href="style.css">
</head>
<body>
'''
    out = head + header(active or fn) + "\n" + main.rstrip() + "\n\n" + FOOTER + (FAB if fab else "") + extra + '''
  <script src="script.js"></script>
</body>
</html>
'''
    open(os.path.join(ROOT, fn), "w").write(out)

# ---------------------------------------------------------------- shared blocks
def step(icon, time, name, youth=False):
    cls = "flow-step youth" if youth else "flow-step"
    tag = ' <span class="pill">Youth</span>' if youth else ""
    return f'''            <div class="{cls}">
              <div class="fs-ic"><svg viewBox="0 0 24 24" aria-hidden="true">{I[icon]}</svg></div>
              <div><div class="fs-time">{time}</div><div class="fs-name">{name}{tag}</div></div>
            </div>'''

SERVICES = f'''    <section class="sec" id="services" aria-labelledby="svc-title">
      <div class="wrap">
        <div class="sec-head-c">
          <span class="kicker">Our rhythm</span>
          <h2 id="svc-title">Worship service times</h2>
          <p>Every service also streams live on YouTube and Facebook at @rccgfullersfield.</p>
        </div>
        <div class="sunday-card">
          <div class="head"><h3>Sunday mornings</h3><span class="pill">Every week</span></div>
          <div class="flow">
{step("sun", "7:30 – 9:30am", "First service")}
{step("book", "9:30 – 10:30am", "Sunday school (Bible study)")}
{step("users", "9:30 – 11:00am", "Hope of Nations", youth=True)}
{step("church", "10:30am – 12:00pm", "Second service")}
          </div>
        </div>
        <div class="midweek">
          <div class="ticket"><div class="ticket-day">Tue<small>Weekly</small></div><div class="ticket-body"><h4>Digging Deep</h4><p class="ticket-time">6:30 – 7:45pm</p><p class="ticket-desc">Interactive midweek Bible study. Bring your Bible and your questions.</p></div></div>
          <div class="ticket"><div class="ticket-day">Thu<small>Weekly</small></div><div class="ticket-body"><h4>Faith Clinic</h4><p class="ticket-time">6:30 – 7:45pm</p><p class="ticket-desc">An evening of powerful prayer for healing, help and breakthrough.</p></div></div>
        </div>
        <div class="spotlight">
          <div><small>Monthly special service, every third Sunday</small><h3>Arise and Shine</h3><p>Thanksgiving, prayer and breakthrough during the 10:30am service.</p></div>
          <a class="btn btn-indigo" href="events.html">See all events</a>
        </div>
      </div>
    </section>'''

def event(rule, time, d, m, title, when, lead, more, img, alt, date_word=False):
    rattr = f' data-rule="{rule}" data-time="{time}"' if rule else ""
    dcls = "d word" if date_word else "d"
    return f'''          <li class="event"{rattr} tabindex="0" role="button" aria-label="View flyer and details for {html.escape(title)}">
            <div class="event-date"><span class="{dcls}">{d}</span><span class="m">{m}</span></div>
            <div>
              <h3>{title}</h3>
              <p class="when">{when}</p>
              <p class="ev-lead">{lead}</p>
              <div class="ev-more">{more}</div>
              <span class="ev-open">View flyer &amp; details</span>
            </div>
            <img src="images/web/{img}" alt="{alt}" loading="lazy">
          </li>'''

VENUE = "RCCG Fuller's Field, Km 47 Lekki–Epe Expressway, beside DKK Pharmacy &amp; Supermarket, Oko-Ado, Lagos"
EVENTS = [
 event("nth,1,4", "18:30", "–", "&nbsp;", "Healing in His Wings",
       'First Thursday of every month, 6:30pm. Next: <span class="next-full">–</span>',
       "A special Faith Clinic service of prayer for healing and restoration.",
       f"<ul><li>Ministering: Pastor (Mrs.) Abosede Obayomi</li><li>Host: Pastor Wole Obayomi, Pastor-in-Charge</li><li>Theme scripture: Malachi 4:2</li><li>Venue: {VENUE}</li><li>Can't come? Join live on YouTube and Facebook at @rccgfullersfield.</li></ul>",
       "event2.jpg", "Flyer for the Healing in His Wings special Faith Clinic service"),
 event("nth,3,0", "10:30", "–", "&nbsp;", "Arise and Shine",
       'Third Sunday of every month, 10:30am. Next: <span class="next-full">–</span>',
       "Our monthly service of thanksgiving, prayer and breakthrough.",
       f"<ul><li>Held during the 10:30am second service</li><li>Come with your testimonies, thanksgiving and prayer requests</li><li>Venue: {VENUE}</li></ul>",
       "members27.jpg", "Pastor praying for a member at the altar"),
 event("date,11,31", "21:00", "31", "Dec", "Crossover Service",
       "31 December, 9pm until we cross into the new year",
       "We end the year in worship and thanksgiving and pray into the new one together. Bring the whole family.",
       f"<ul><li>Host: Pastor Wole Obayomi</li><li>Starts 9pm on 31 December</li><li>Venue: {VENUE}</li><li>Join live on YouTube at @rccgfullersfield.</li></ul>",
       "event1.jpg", "Flyer for the Fuller's Field Crossover Service"),
 event(None, None, "Easter", "Yearly", "Easter Praise Concert",
       "Every Easter season, 4pm. Last held Sunday 12 April 2026",
       "Hope of Nations and the Young Adult and Youth Affairs team celebrate the risen Christ in song.",
       "<ul><li>Worship, the Word, praise, drama, spoken word and more</li><li>Host: Pastor Wole Obayomi</li><li>Theme: He Is Risen (Matthew 28:6)</li><li>The 2027 date will be announced here before Easter.</li></ul>",
       "event3.jpg", "Flyer for the Easter Praise Concert, He Is Risen", date_word=True),
]

def events_section(heading, sub, sid="monthly"):
    items = "\n".join(EVENTS)
    return f'''    <section class="events" id="{sid}" aria-labelledby="ev-title">
      <div class="wrap">
        <div class="section-head">
          <h2 id="ev-title">{heading}</h2>
          <p>{sub}</p>
        </div>
        <ul class="event-list">
{items}
        </ul>
      </div>
    </section>'''

COUNTDOWN = f'''    <section class="countdown" data-countdown aria-label="Countdown to the next gathering">
      <div class="wrap">
        <div class="cd-label"><small class="cd-when">Next gathering</small><strong class="cd-name">Sunday first service</strong></div>
        <div class="cd-timer">
          <div class="cd-unit"><span data-u="d">00</span><small>Days</small></div>
          <div class="cd-unit"><span data-u="h">00</span><small>Hours</small></div>
          <div class="cd-unit"><span data-u="m">00</span><small>Mins</small></div>
          <div class="cd-unit"><span data-u="s">00</span><small>Secs</small></div>
        </div>
        <span class="cd-live"><span class="live-dot"></span> Join us in church or online</span>
        <a class="btn btn-white" href="{YT}" target="_blank" rel="noopener">Watch live</a>
      </div>
    </section>'''

# ---------------------------------------------------------------- departments
DEPTS = [
 ("ushering", "Ushering", "users", "bg-red", "Welcome people at the door, help them find a seat and receive the offering.", []),
 ("choir", "Choir &amp; music", "music", "bg-gold", "Lead the church in praise and worship as a singer or instrumentalist.", ["Attend a short audition with the music director."]),
 ("media", "Media &amp; technical", "video", "bg-indigo", "Run sound, cameras, the livestream, projection and photography.", ["Shadow the team for a few Sundays to learn the equipment."]),
 ("sanctuary", "Sanctuary keepers", "spark", "bg-green", "Prepare and care for the house of God before and after every service.", []),
 ("children", "Children's teachers", "child", "bg-rose", "Teach and care for children in Children's Church every Sunday.", ["Complete a short child-safety briefing before you serve."]),
 ("protocol", "Protocol &amp; hospitality", "star", "bg-ink", "Look after first-time guests, visiting ministers and special programmes.", []),
 ("welfare", "Welfare &amp; evangelism", "heart", "bg-red", "Visit and support members in need and take the gospel into our community.", []),
 ("prayer", "Prayer team", "pray", "bg-gold", "Stand in the gap for the church, its pastors and its programmes.", []),
 ("security", "Security &amp; car park", "shield", "bg-green", "Keep everyone safe and help with parking on busy Sundays.", []),
]

def dept_tile(d):
    sid, name, ic, bg, desc, _ = d
    return f'''          <a class="dept" href="workers.html#{sid}"><span class="ic {bg}">{svg(ic)}</span><span><strong>{name}</strong><span class="sub">{desc.split(",")[0].split(" and ")[0]}</span></span></a>'''

def dept_card(d):
    sid, name, ic, bg, desc, extra = d
    plain = html.unescape(name)
    steps = ["Be a member who worships with us regularly at Fuller's Field.",
             "Register for Workers in Training (WIT) at the parish office.",
             f"Tell us you would like to join {plain.lower()}; we will introduce you to the head of department."] + extra + \
            ["Start serving once you finish WIT and your department orientation."]
    lis = "".join(f"<li><span>{html.escape(s)}</span></li>" for s in steps)
    return f'''          <article class="dept-card" id="{sid}">
            <div class="top"><span class="ic {bg}">{svg(ic)}</span><div><h3>{name}</h3><p>{desc}</p></div></div>
            <details>
              <summary>How to join</summary>
              <div class="how">
                <ol class="mini-steps">{lis}</ol>
                <div class="btn-row">
                  <a class="btn btn-red btn-sm" href="{mailto("I want to join " + plain, "Hello, my name is ... and I would like to join the " + plain + " department. My phone number is ...")}">{svg("mail")} Email to join</a>
                  <a class="btn btn-line on-light btn-sm" href="tel:{TEL}">{svg("phone")} Call the office</a>
                </div>
              </div>
            </details>
          </article>'''

WIT_CARD = f'''        <div class="wit-card">
          <div>
            <h3>Become a worker</h3>
            <p>Every worker at Fuller's Field starts with Workers in Training (WIT), the RCCG course that grounds you in the faith and prepares you to serve.</p>
            <div class="btn-row" style="margin-top:22px">
              <a class="btn btn-red" href="{mailto("Register me for Workers in Training", "Hello, my name is ... and I would like to register for Workers in Training. My phone number is ...")}">Register for WIT</a>
              <a class="btn btn-line" href="workers.html">See all departments</a>
            </div>
          </div>
          <ol class="wit-steps">
            <li><div><strong>Worship with us</strong><span>Be part of the Fuller's Field family on Sundays.</span></div></li>
            <li><div><strong>Register for WIT</strong><span>Sign up at the parish office or by email.</span></div></li>
            <li><div><strong>Join a department</strong><span>Pick where you want to serve and start after training.</span></div></li>
          </ol>
        </div>'''

# ---------------------------------------------------------------- ministries data
MINISTRIES = [
 dict(fn="hope-of-nations.html", name="Hope of Nations", tag="Sundays 9:30 – 11:00am", who="Teenagers, students and young adults",
      when="Every Sunday, 9:30 – 11:00am", hero="members17.jpg",
      short="Our youth and young adults ministry: worship, the Word and real conversations.",
      about=["Hope of Nations is the youth and young adults ministry of Fuller's Field. We are raising the next generation of leaders and influencers for God's kingdom.",
             "Young people face real pressures today. Hope of Nations gives them a place to bring honest questions, grow in their relationship with God and discover their gifts, with friends who are walking the same road."],
      acts=[("users", "bg-red", "Sunday youth service", "Worship, teaching and prayer every Sunday from 9:30am."),
            ("mic", "bg-gold", "Creative arts", "Music, drama and spoken word, like our Easter Praise Concert."),
            ("book", "bg-indigo", "Career and life workshops", "Practical sessions on work, money, relationships and purpose."),
            ("globe", "bg-green", "Outreach", "Taking the love of Jesus to our neighbourhood and campuses.")],
      gallery=["members17.jpg", "members8.jpg", "members1.jpg", "members14.jpg", "members7.jpg"],
      steps=[("Come on Sunday", "Join us at 9:30am. No sign-up needed: just walk in."),
             ("Say hello", "Meet one of the Hope of Nations leaders after the service."),
             ("Share your details", "Give us your name and number so we can keep you updated."),
             ("Get involved", "Join a team: music, drama, media, ushering or outreach.")]),
 dict(fn="childrens-church.html", name="Children's Church", tag="Every Sunday", who="Children of the church and visitors",
      when="Sundays, during service", hero="childrenministry.jpg",
      short="A safe, joyful place for children to meet Jesus every Sunday.",
      about=["Children's Church is where the youngest members of Fuller's Field learn about Jesus in a way they understand, through Bible stories, songs, prayer and lots of fun.",
             "It runs on Sundays while parents worship, so the whole family can meet God in church. Our teachers love children and are trained to keep them safe."],
      acts=[("book", "bg-indigo", "Bible stories", "Lessons from the RCCG children's curriculum."),
            ("music", "bg-gold", "Songs and praise", "Children learn to worship with joy."),
            ("child", "bg-rose", "Safe care", "Trained teachers look after every child."),
            ("star", "bg-green", "Special days", "Children's Day, Christmas and end-of-year celebrations.")],
      gallery=["childrenministry.jpg", "members19.jpg", "members25.jpg", "members12.jpg", "members2.jpg"],
      steps=[("Bring your child on Sunday", "Arrive a few minutes early for the service."),
             ("Meet a teacher", "An usher will show you where Children's Church meets."),
             ("Register your child", "Share your child's name, age and your phone number."),
             ("Pick up after service", "Collect your child from their teacher when service ends.")]),
 dict(fn="wise-women.html", name="Wise Women", tag="Women 60 and above", who="Women aged 60 and above",
      when="Speak to a pastor for meeting times", hero="womenministry.jpg",
      short="Fellowship, prayer and the wisdom of women who have walked with God.",
      about=["The Wise Women are the mothers of Fuller's Field: women of 60 and above who have walked with God through many seasons.",
             "They meet for fellowship, prayer and care for one another, and they pour their wisdom and faith into the younger women and families of the church."],
      acts=[("users", "bg-gold", "Fellowship", "Time together to share, encourage and laugh."),
            ("pray", "bg-red", "Prayer", "Standing in prayer for families and the church."),
            ("heart", "bg-rose", "Mentoring", "Walking alongside younger women and mothers."),
            ("music", "bg-indigo", "Praise", "Leading the church in song on special Sundays.")],
      gallery=["womenministry.jpg", "members13.jpg", "members28.jpg", "members21.jpg", "members24.jpg"],
      steps=[("Come on Sunday", "Worship with us at 7:30am or 10:30am."),
             ("Speak to a pastor", "Let Pastor (Mrs.) Obayomi or a pastor know you would like to join."),
             ("Share your details", "Give us your name and phone number."),
             ("Join the next meeting", "We will tell you when and where the Wise Women meet.")]),
 dict(fn="wise-men.html", name="Wise Men", tag="Men 60 and above", who="Men aged 60 and above",
      when="Speak to a pastor for meeting times", hero="wisemen.jpg",
      short="Brotherhood, mentoring and prayer for the fathers of our church.",
      about=["The Wise Men are the fathers of Fuller's Field: men of 60 and above who meet for brotherhood, prayer and purpose.",
             "They mentor younger men, stand with families in prayer and remind us all that it is never too late to serve God with joy."],
      acts=[("users", "bg-indigo", "Brotherhood", "Friendship and fellowship among the fathers of the church."),
            ("pray", "bg-red", "Prayer", "Interceding for families, the church and the nation."),
            ("star", "bg-gold", "Mentoring", "Guiding younger men in faith, work and family."),
            ("church", "bg-green", "Service", "Supporting church programmes and special services.")],
      gallery=["wisemen.jpg", "members23.jpg", "members6.jpg", "members15.jpg", "members27.jpg"],
      steps=[("Come on Sunday", "Worship with us at 7:30am or 10:30am."),
             ("Speak to a pastor", "Let Pastor Wole or a pastor know you would like to join."),
             ("Share your details", "Give us your name and phone number."),
             ("Join the next meeting", "We will tell you when and where the Wise Men meet.")]),
]

def min_card(m):
    return f'''          <a class="min-card" href="{m["fn"]}">
            <img src="images/web/{m["hero"]}" alt="" loading="lazy">
            <div class="body"><span class="tag">{m["tag"]}</span><h3>{m["name"]}</h3><p>{m["short"]}</p><span class="min-go">Visit the {m["name"]} page</span></div>
          </a>'''

def ministry_page(m):
    acts = "\n".join(f'''            <li><span class="ic {bg}">{svg(ic)}</span><div><strong>{t}</strong><span>{d}</span></div></li>''' for ic, bg, t, d in m["acts"])
    gal = "\n".join(f'''          <button type="button" aria-label="Enlarge photo {i+1}"><img src="images/web/{g}" alt="{m["name"]} at Fuller's Field, photo {i+1}" loading="lazy"></button>''' for i, g in enumerate(m["gallery"]))
    steps = "\n".join(f'''            <li><div><strong>{t}</strong><span>{d}</span></div></li>''' for t, d in m["steps"])
    others = "\n".join(min_card(o) for o in MINISTRIES if o["fn"] != m["fn"])
    about = "\n".join(f"          <p>{p}</p>" for p in m["about"])
    main = f'''  <main id="main">
    <section class="page-hero">
      <img src="images/web/{m["hero"]}" alt="">
      <div class="wrap">
        <div>
          <span class="hero-pill">{m["tag"]}</span>
          <h1>{m["name"]}</h1>
          <p class="lead">{m["short"]}</p>
          <div class="btn-row">
            <a class="btn btn-red" href="#join">How to join</a>
            <a class="btn btn-line" href="ministries.html">All ministries</a>
          </div>
        </div>
      </div>
    </section>

    <section class="facts" aria-label="At a glance">
      <div class="wrap">
        <div><small>When</small><strong>{m["when"]}</strong></div>
        <div><small>Who</small><strong>{m["who"]}</strong></div>
        <div><small>Where</small><strong>RCCG Fuller's Field, Km 47 Lekki–Epe Expressway</strong></div>
      </div>
    </section>

    <section class="sec about-min" aria-labelledby="about-title">
      <div class="wrap">
        <div class="prose">
          <span class="kicker">About us</span>
          <h2 id="about-title">Welcome to {m["name"]}</h2>
{about}
        </div>
        <ul class="activities" aria-label="What we do">
{acts}
        </ul>
      </div>
    </section>

    <section class="sec sec-tint" aria-labelledby="gal-title" style="padding-top:72px">
      <div class="wrap">
        <div class="section-head"><h2 id="gal-title">Moments</h2><p>Tap a photo to see it bigger.</p></div>
        <div class="gallery-grid">
{gal}
        </div>
      </div>
    </section>

    <section class="sec join" id="join" aria-labelledby="join-title">
      <div class="wrap">
        <div>
          <span class="kicker" style="color:var(--indigo-deep)">Join us</span>
          <h2 id="join-title">How to join {m["name"]}</h2>
          <div class="reach">
            <p>Prefer to reach out first? Send us an email or call the parish office and we will connect you with the {m["name"]} leaders.</p>
            <div class="row">
              <a class="btn btn-red btn-sm" href="{mailto("I want to join " + m["name"], "Hello, my name is ... and I would like to join " + m["name"] + ". My phone number is ...")}">{svg("mail")} Email us</a>
              <a class="btn btn-white btn-sm" href="tel:{TEL}">{svg("phone")} {PHONE}</a>
            </div>
          </div>
        </div>
        <ol class="join-steps">
{steps}
        </ol>
      </div>
    </section>

    <section class="sec" aria-labelledby="other-title">
      <div class="wrap">
        <div class="section-head"><h2 id="other-title">Other ministries</h2><p><a class="text-link" href="workers.html">Or serve in a department</a></p></div>
        <div class="min-cards other-min">
{others}
        </div>
      </div>
    </section>
  </main>'''
    page(m["fn"], f"{m['name']} | RCCG Fuller's Field", f"{m['name']} at RCCG Fuller's Field: {html.unescape(m['short'])} {m['when']}.",
         main, active="ministries.html", extra=PHOTO_DIALOG)

# ---------------------------------------------------------------- home
p_index = prev("index")
HERO = between(p_index, "    <!-- Hero -->", "    <!-- Countdown -->")
VISIT = between(p_index, "    <!-- Plan a visit -->", "    <!-- Ministries -->")
GIVE_BAND = between(p_index, "    <!-- Give -->", "  </main>")

def tile(cls, imgs):
    first, rest = imgs[0], imgs[1:]
    s = f'<img src="images/web/{first[0]}" alt="{first[1]}">' + "".join(f'<img src="images/web/{i}" alt="{a}" loading="lazy">' for i, a in rest)
    return f'          <div class="tile {cls}">{s}</div>'

MOSAIC = "\n".join([
 tile("t-a", [("members23.jpg", "Members greeting one another before service"), ("members8.jpg", "The congregation standing in worship"), ("wisemen.jpg", "The Wise Men celebrating")]),
 tile("t-b", [("members25.jpg", "A mother in a green hat smiling with her baby"), ("members13.jpg", "A minister speaking"), ("members28.jpg", "A mother of the church in prayer")]),
 tile("t-c", [("members15.jpg", "A minister singing at the keyboard"), ("members9.jpg", "A minister speaking"), ("members4.jpg", "A minister with a microphone")]),
 tile("t-d", [("members26.jpg", "A member dancing in praise"), ("members5.jpg", "A member sharing a testimony"), ("members20.jpg", "A minister preaching")]),
 tile("t-e", [("members6.jpg", "A man praying with his hand on his chest"), ("members3.jpg", "A woman praying with her eyes closed"), ("members10.jpg", "A woman singing in worship")]),
 tile("t-f", [("community1.jpg", "Two women embracing after service"), ("members21.jpg", "Members chatting after service"), ("members24.jpg", "A member lifting her hand in praise")]),
 tile("t-g", [("members19.jpg", "A woman carrying a sleeping child"), ("childrenministry.jpg", "Children gathered at a celebration"), ("members11.jpg", "A woman worshipping")]),
])
STRIP = "\n".join(f'            <img src="images/web/{i}" alt="" loading="lazy">' for i in
  ["members2.jpg", "members14.jpg", "members16.jpg", "members18.jpg", "members22.jpg", "members7.jpg", "members12.jpg", "members27.jpg", "members1.jpg", "womenministry.jpg"])

home_main = f'''  <main id="main">
{HERO.rstrip()}

    <!-- Countdown -->
{COUNTDOWN}

    <!-- Services -->
{SERVICES}

    <!-- A word from our pastor -->
    <section class="sec sec-tint pastor-word" aria-labelledby="pw-title">
      <div class="wrap">
        <figure class="pw-photo">
          <img src="images/web/pastor-portrait.jpg" alt="Pastor Wole Obayomi" loading="lazy">
          <figcaption>Pastor Wole Obayomi<span>Pastor-in-Charge</span></figcaption>
        </figure>
        <div>
          <span class="kicker">A word from our pastor</span>
          <h2 id="pw-title">Welcome home</h2>
          <div class="pw-body">
            <p>Whether this is your first visit or you have worshipped with us for years, I am glad you are here.</p>
            <p>Fuller's Field is a family that loves God, loves people and does good. Whatever season you are in, there is a seat for you, a family to belong to and a God who has a purpose for your life.</p>
          </div>
          <div class="scripture-box"><p>“I was glad when they said unto me, Let us go into the house of the LORD.”</p><cite>Psalm 122:1</cite></div>
          <p class="signature">Pastor Wole Obayomi<span>Pastor-in-Charge, RCCG Fuller's Field</span></p>
          <p style="margin-top:22px"><a class="text-link" href="about.html">Read our story</a></p>
        </div>
      </div>
    </section>

{VISIT.rstrip()}

    <!-- Ministries -->
    <section class="sec" id="ministries" aria-labelledby="min-title">
      <div class="wrap">
        <div class="section-head">
          <h2 id="min-title">Find your people</h2>
          <p>Each ministry is a smaller family where you can grow, be known and serve. <a class="text-link" href="ministries.html">All ministries</a></p>
        </div>
        <div class="min-cards">
{chr(10).join(min_card(m) for m in MINISTRIES)}
        </div>
      </div>
    </section>

    <!-- Serve -->
    <section class="sec sec-tint" id="serve" aria-labelledby="serve-title">
      <div class="wrap">
        <div class="section-head">
          <h2 id="serve-title">Serve in God's house</h2>
          <p>Sundays at Fuller's Field run on willing hands. Find a department that fits your gifts.</p>
        </div>
        <div class="dept-grid">
{chr(10).join(dept_tile(d) for d in DEPTS[:8])}
        </div>
{WIT_CARD}
      </div>
    </section>

    <!-- Events -->
{events_section("Coming up", 'Tap any event to see the flyer and details. <a class="text-link" href="events.html" style="color:#fff">All events</a>')}

    <!-- Gallery -->
    <section class="sec" aria-labelledby="gal-title">
      <div class="wrap">
        <div class="section-head">
          <h2 id="gal-title">Sundays at Fuller's Field</h2>
          <p><a class="text-link" href="https://www.facebook.com/rccgfullersfield/" target="_blank" rel="noopener">More photos on Facebook</a></p>
        </div>
        <div class="mosaic">
{MOSAIC}
        </div>
      </div>
      <div class="strip" aria-hidden="true">
        <div class="strip-track">
{STRIP}
        </div>
      </div>
    </section>

{GIVE_BAND.rstrip()}
  </main>'''
page("index.html", "RCCG Fuller's Field | Church in Sangotedo, Lekki–Epe Expressway",
     "RCCG Fuller's Field is a parish of The Redeemed Christian Church of God at Km 47, Lekki–Epe Expressway, Lagos. Sunday services at 7:30am and 10:30am.",
     home_main, extra=EV_DIALOG)

# ---------------------------------------------------------------- ministries overview
min_main = f'''  <main id="main">
    <section class="page-hero">
      <img src="images/web/members8.jpg" alt="">
      <div class="wrap">
        <div>
          <span class="hero-pill">Find your people</span>
          <h1>Ministries</h1>
          <p class="lead">Church is more than Sunday. Each ministry at Fuller's Field is a smaller family where you can grow, be known and serve.</p>
        </div>
      </div>
    </section>

    <section class="sec" aria-labelledby="mins-title">
      <div class="wrap">
        <div class="section-head"><h2 id="mins-title">Choose a ministry</h2><p>Tap a ministry to see photos, meeting times and how to join.</p></div>
        <div class="min-cards">
{chr(10).join(min_card(m) for m in MINISTRIES)}
        </div>
        <div class="min-small">
          <a href="events.html#services"><img src="images/web/members16.jpg" alt="" loading="lazy"><div><strong>Sunday school</strong><span>Bible study classes every Sunday, 9:30 – 10:30am.</span></div></a>
          <a href="events.html#services"><img src="images/web/members6.jpg" alt="" loading="lazy"><div><strong>Prayer &amp; Bible study</strong><span>Digging Deep on Tuesdays and Faith Clinic on Thursdays, 6:30pm.</span></div></a>
        </div>
      </div>
    </section>

    <section class="sec sec-tint" aria-labelledby="serve-title">
      <div class="wrap">
        <div class="section-head"><h2 id="serve-title">Want to serve too?</h2><p>Join one of our departments. <a class="text-link" href="workers.html">See all departments</a></p></div>
{WIT_CARD}
      </div>
    </section>
  </main>'''
page("ministries.html", "Ministries | RCCG Fuller's Field",
     "Hope of Nations, Children's Church, Wise Women and Wise Men at RCCG Fuller's Field, Sangotedo, Lagos.", min_main)

for m in MINISTRIES:
    ministry_page(m)

# ---------------------------------------------------------------- workers
workers_main = f'''  <main id="main">
    <section class="page-hero">
      <img src="images/web/members15.jpg" alt="">
      <div class="wrap">
        <div>
          <span class="hero-pill">Serve with us</span>
          <h1>Departments</h1>
          <p class="lead">Use your gifts in God's house. Pick a department, see how to join and send us a message in one tap.</p>
          <div class="btn-row">
            <a class="btn btn-red" href="#departments">Choose a department</a>
            <a class="btn btn-line" href="#wit">Workers in Training</a>
          </div>
        </div>
      </div>
    </section>

    <section class="sec" id="wit" aria-labelledby="wit-title">
      <div class="wrap">
        <div class="section-head"><h2 id="wit-title">Start with Workers in Training</h2><p>Every department starts here.</p></div>
{WIT_CARD}
      </div>
    </section>

    <section class="sec sec-tint" id="departments" aria-labelledby="dept-title">
      <div class="wrap">
        <div class="section-head"><h2 id="dept-title">Our departments</h2><p>Tap "How to join" on any department for the steps and a quick way to email us.</p></div>
        <div class="dept-list">
{chr(10).join(dept_card(d) for d in DEPTS)}
        </div>
      </div>
    </section>

    <section class="cta-band" aria-labelledby="cta-title">
      <div class="wrap">
        <div>
          <h2 id="cta-title">Not sure where you fit?</h2>
          <p>Talk to us. We will help you find the right place to serve.</p>
        </div>
        <div class="btn-row">
          <a class="btn btn-white" href="{mailto("Help me find a department")}">Email us</a>
          <a class="btn btn-line" href="tel:{TEL}">Call {PHONE}</a>
        </div>
      </div>
    </section>
  </main>'''
page("workers.html", "Serve | RCCG Fuller's Field",
     "Departments at RCCG Fuller's Field and how to join them, starting with Workers in Training.", workers_main)

# ---------------------------------------------------------------- events
p_events = prev("events")
RCCG_EV = between(p_events, '    <section class="rccg-events', '    <section class="cta-band"')
EV_CTA = between(p_events, '    <section class="cta-band"', '  </main>')
events_main = f'''  <main id="main">
    <section class="page-hero">
      <img src="images/web/members27.jpg" alt="">
      <div class="wrap">
        <div>
          <span class="hero-pill">What's on</span>
          <h1>Events</h1>
          <p class="lead">Weekly gatherings, monthly special services and the big moments of the year. Tap any event to see its flyer.</p>
        </div>
      </div>
    </section>

{COUNTDOWN}

{events_section("Coming up at Fuller's Field", "Dates update automatically. Tap an event to see the flyer and details.")}

{SERVICES}

{RCCG_EV.rstrip()}

{EV_CTA.rstrip()}
  </main>'''
page("events.html", "Events | RCCG Fuller's Field",
     "Monthly special services, yearly events and weekly service times at RCCG Fuller's Field, Lekki–Epe Expressway, Lagos.",
     events_main, extra=EV_DIALOG)

# ---------------------------------------------------------------- about
p_about = prev("about")
about_main = p_about[p_about.index('  <main id="main">'):p_about.index('  </main>') + 9]
old_purpose = between(about_main, "    <!-- Vision & mission -->", "    <!-- Values -->")
MV = ["To make heaven.",
      "To take as many people with us.",
      "To have a member of RCCG in every family of all nations.",
      "To accomplish No. 1 above, holiness will be our lifestyle.",
      "To accomplish No. 2 and 3 above, we will plant churches within five minutes walking distance in every city and town of developing countries and within five minutes driving distance in every city and town of developed countries.",
      "We will pursue these objectives until every Nation in the world is reached for the Lord Jesus Christ."]
mv_html = "\n".join(f"          <li><p>{t}</p></li>" for t in MV)
about_main = about_main.replace(old_purpose, f'''    <!-- Mission & Vision -->
    <section class="mv" id="mission" aria-labelledby="mv-title">
      <div class="wrap">
        <span class="kicker" style="color:var(--gold)">The RCCG mandate</span>
        <h2 id="mv-title">Mission &amp; Vision</h2>
        <ol class="mv-list">
{mv_html}
        </ol>
      </div>
    </section>

''')
page("about.html", "About | RCCG Fuller's Field",
     "Our story, the RCCG mission and vision, our beliefs and pastors at RCCG Fuller's Field, Sangotedo, Lagos.", about_main)

# ---------------------------------------------------------------- contact
p_contact = prev("contact")
contact_main = p_contact[p_contact.index('  <main id="main">'):p_contact.index('  </main>') + 9]
page("contact.html", "Contact | RCCG Fuller's Field",
     "Address, directions, phone, email and prayer requests for RCCG Fuller's Field, Km 47 Lekki–Epe Expressway, Lagos.", contact_main)

# ---------------------------------------------------------------- give
p_give = prev("give")
USSD_FAQ = between(p_give, "    <!-- USSD -->", "  </main>")
FUNDS = [
 ("Tabernacle Fund", "Building our church", "church", "bg-indigo", "0212009335"),
 ("Mission Fund", "Evangelism and RCCG missions", "globe", "bg-green", "3490010950"),
 ("CSR", "Projects that serve our community", "hands", "bg-gold", "0210002112"),
 ("Welfare", "Food, school fees and help for families", "heart", "bg-red", "0213000786"),
 ("Hope of Nations", "Our youth and young adults", "users", "bg-rose", "3490030961"),
 ("Special Funds", "Special seeds, vows and projects", "gift", "bg-ink", "0213061101"),
]
fund_html = "\n".join(f'''          <article class="fundc">
            <div class="band {bg}"></div>
            <div class="in">
              <span class="ic {bg}">{svg(ic)}</span>
              <h3>{n}</h3>
              <p>{u}</p>
              <div class="num-row"><span class="num">{num}</span>{copy_btn(num, aria="Copy " + n + " account number")}</div>
            </div>
          </article>''' for n, u, ic, bg, num in FUNDS)
give_main = f'''  <main id="main">
    <section class="page-hero">
      <img src="images/web/offeringhero.jpg" alt="">
      <div class="wrap" style="padding-bottom:110px">
        <div>
          <span class="hero-pill">Sow a seed</span>
          <h1>Give</h1>
          <p class="lead">Giving is worship. Your tithes, offerings and seeds fund ministry at Fuller's Field, care for families in need, send the gospel further and build God's house.</p>
          <div class="btn-row">
            <a class="btn btn-red" href="#funds">Choose a fund</a>
            <a class="btn btn-line" href="#ussd">Give with USSD</a>
          </div>
        </div>
        <blockquote class="verse">
          <p>Each of you should give what you have decided in your heart to give, not reluctantly or under compulsion, for God loves a cheerful giver.</p>
          <cite>2 Corinthians 9:7</cite>
        </blockquote>
      </div>
    </section>

    <div class="wrap give-top">
      <div class="acct-card">
        <p class="fund">Tithe, first fruit &amp; love offering</p>
        <p class="bank">Ecobank Nigeria. Account name: <strong>RCCG Fuller's Field</strong></p>
        <div class="acct-num-row">
          <span class="acct-num">0212009328</span>
          {copy_btn("0212009328", aria="Copy tithe and offering account number")}
        </div>
        <p class="acct-warn" style="margin-top:0"><strong>Before you send:</strong> check that your banking app shows the account name "RCCG Fuller's Field".</p>
      </div>
    </div>

    <section class="sec" id="funds" aria-labelledby="funds-title">
      <div class="wrap">
        <div class="section-head"><h2 id="funds-title">Choose where your seed goes</h2><p>All accounts are with Ecobank Nigeria in the name RCCG Fuller's Field.</p></div>
        <div class="fund-grid">
{fund_html}
        </div>
      </div>
    </section>

    <section class="sec sec-tint" aria-labelledby="seed-title">
      <div class="wrap">
        <div class="section-head"><h2 id="seed-title">Your seed at work</h2><p>What your giving makes possible at Fuller's Field and beyond.</p></div>
        <div class="seed-strip">
          <figure class="seed"><img src="images/web/community1.jpg" alt="Two women embracing after service" loading="lazy"><span><small>Welfare</small>Families cared for in hard times</span></figure>
          <figure class="seed"><img src="images/web/childrenministry.jpg" alt="Children gathered at a celebration" loading="lazy"><span><small>Ministry</small>Children growing in faith</span></figure>
          <figure class="seed"><img src="images/web/churchbuilding.jpg" alt="The church building" loading="lazy"><span><small>Tabernacle</small>A house of God for generations</span></figure>
          <figure class="seed"><img src="images/web/members17.jpg" alt="Young people worshipping" loading="lazy"><span><small>Hope of Nations</small>Young people growing in God</span></figure>
        </div>
      </div>
    </section>

{USSD_FAQ.rstrip()}

    <section class="thanks" aria-label="Thank you">
      <div class="wrap">
        <blockquote>
          <p>“Give, and it shall be given unto you; good measure, pressed down, and shaken together, and running over.”</p>
          <cite>Luke 6:38</cite>
        </blockquote>
        <p style="margin-top:22px; font-weight:700">Thank you for giving to the work of God at Fuller's Field.</p>
      </div>
    </section>
  </main>'''
page("give.html", "Give | RCCG Fuller's Field",
     "Give your tithes and offerings to RCCG Fuller's Field by bank transfer or USSD. All accounts are with Ecobank Nigeria.",
     give_main, fab=False)

print("built")
