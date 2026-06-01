import requests
import schedule
import time

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@jobhuntez"

def post_job():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHANNEL,
            "text": "🚀 New Job Alert\n\nSoftware Developer Intern\nLocation: Remote\nApply Now!"
        }
    )

    print("Job Posted")

schedule.every(1).minutes.do(post_job)

print("Auto Poster Running...")

post_job()

while True:
    schedule.run_pending()
    time.sleep(1)