import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@jobhuntez"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHANNEL,
            "text": text
        }
    )

    print(response.text)

if __name__ == "__main__":
    send_message(
        "🚀 Daily Jobs Alert\n\n"
        "GitHub Action Working Successfully ✅"
    )