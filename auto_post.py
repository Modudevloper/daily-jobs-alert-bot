import os
import json
import feedparser
import requests
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@jobhuntez"

RSS_FEEDS = [
"https://weworkremotely.com/categories/remote-programming-jobs.rss",
"https://weworkremotely.com/categories/remote-design-jobs.rss",
]

POSTED_FILE = "posted_jobs.json"

BAD_WORDS = [
"registration fee",
"joining fee",
"pay to apply",
"investment required",
"crypto",
]

BAD_DOMAINS = [
"bit.ly",
"tinyurl.com",
]

if os.path.exists(POSTED_FILE):
with open(POSTED_FILE, "r", encoding="utf-8") as f:
posted_links = set(json.load(f))
else:
posted_links = set()

def send_message(text):
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

```
requests.post(
    url,
    data={
        "chat_id": CHANNEL,
        "text": text,
        "disable_web_page_preview": True
    },
    timeout=20
)
```

current_hour = datetime.utcnow().hour

if current_hour == 2:
category = "🌅 Morning Jobs"

elif current_hour == 5:
category = "🎓 Internship Jobs"

elif current_hour == 8:
category = "🌍 Remote Jobs"

elif current_hour == 11:
category = "💻 Developer Jobs"

elif current_hour == 15:
category = "📊 Daily Digest"

else:
category = "💼 Jobs"

new_posts = 0

for feed_url in RSS_FEEDS:

```
feed = feedparser.parse(feed_url)

for job in feed.entries[:10]:

    title = getattr(job, "title", "").strip()
    link = getattr(job, "link", "").strip()
    summary = getattr(job, "summary", "")

    if not link:
        continue

    if link in posted_links:
        continue

    text_to_check = f"{title} {summary}".lower()

    if any(word in text_to_check for word in BAD_WORDS):
        continue

    if any(domain in link.lower() for domain in BAD_DOMAINS):
        continue

    message = f"""
```

🚀 New Job Alert

{category}

💼 {title}

🔗 Apply:
{link}

📢 Join @jobhuntez
"""

```
    send_message(message)

    posted_links.add(link)
    new_posts += 1
```

with open(POSTED_FILE, "w", encoding="utf-8") as f:
json.dump(list(posted_links), f, indent=2)

print(f"Posted {new_posts} new jobs")
