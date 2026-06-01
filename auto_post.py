import os
import sqlite3
import feedparser
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@jobhuntez"

RSS_FEEDS = [
    "https://weworkremotely.com/categories/remote-programming-jobs.rss"
]

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs(
    link TEXT PRIMARY KEY,
    title TEXT
)
""")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHANNEL,
            "text": text
        },
        timeout=30
    )

for feed_url in RSS_FEEDS:

    feed = feedparser.parse(feed_url)

    for job in feed.entries[:10]:

        title = job.title
        link = job.link

        cursor.execute(
            "SELECT link FROM jobs WHERE link=?",
            (link,)
        )

        if cursor.fetchone():
            continue

        cursor.execute(
            "INSERT INTO jobs(link,title) VALUES(?,?)",
            (link, title)
        )

        message = f"""
🚀 New Job Alert

💼 {title}

🔗 Apply:
{link}

📢 Join @jobhuntez
"""

        send_message(message)

conn.commit()
conn.close()