import os
import json
import feedparser
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@jobhuntez"

RSS_FEEDS = [
    "https://weworkremotely.com/categories/remote-programming-jobs.rss"
]

POSTED_FILE = "posted_jobs.json"

if os.path.exists(POSTED_FILE):
    with open(POSTED_FILE, "r", encoding="utf-8") as f:
        posted_links = set(json.load(f))
else:
    posted_links = set()

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(
        url,
        data={
            "chat_id": CHANNEL,
            "text": text
        },
        timeout=20
    )

for feed_url in RSS_FEEDS:
    feed = feedparser.parse(feed_url)

    for job in feed.entries[:5]:
        title = job.title
        link = job.link

        if link in posted_links:
            continue

        message = f"""🚀 New Job Alert

💼 {title}

🔗 Apply:
{link}

📢 Join @jobhuntez
"""
        send_message(message)
        posted_links.add(link)

with open(POSTED_FILE, "w", encoding="utf-8") as f:
    json.dump(list(posted_links), f, indent=2)

print("Done")