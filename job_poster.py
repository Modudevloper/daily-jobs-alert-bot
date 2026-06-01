import requests
import schedule
import time

BOT_TOKEN = "8826668549:AAFYD0rdk4NcPHpz6CXQBknQSsI0VZDJ_B8"
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