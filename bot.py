import asyncio
import json
import os
import feedparser
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = "8826668549:AAFYD0rdk4NcPHpz6CXQBknQSsI0VZDJ_B8"
CHANNEL = "@jobhuntez"
RSS_FEEDS = ["https://weworkremotely.com/categories/remote-programming-jobs.rss"]
POSTED_FILE = "posted_jobs.json"

# Load posted links
if os.path.exists(POSTED_FILE):
    with open(POSTED_FILE, "r", encoding="utf-8") as f:
        posted_links = set(json.load(f))
else:
    posted_links = set()

# --- Command Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Daily Jobs Alert\n\nJoin: https://t.me/jobhuntez")

async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📢 Latest Jobs\nhttps://t.me/jobhuntez")

async def internships(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎓 Latest Internships\nhttps://t.me/jobhuntez")

async def govjobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏛 Government Jobs\nhttps://t.me/jobhuntez")

async def results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📄 Exam Results\nhttps://t.me/jobhuntez")

async def admitcard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🪪 Admit Cards\nhttps://t.me/jobhuntez")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /jobs /internships /govjobs /results /admitcard")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "job" in text:
        await update.message.reply_text("📢 Latest Jobs:\nhttps://t.me/jobhuntez")
    else:
        await update.message.reply_text("✅ Join Channel:\nhttps://t.me/jobhuntez")

# --- RSS Auto-Poster ---
async def check_rss_feeds(context: ContextTypes.DEFAULT_TYPE):
    global posted_links
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for job in feed.entries[:5]:
            link = job.link
            if link in posted_links:
                continue
            message = f"""🚀 New Job Alert

💼 {job.title}

🔗 Apply:
{link}

📢 Join @jobhuntez
"""
            await context.bot.send_message(chat_id=CHANNEL, text=message)
            posted_links.add(link)

    with open(POSTED_FILE, "w", encoding="utf-8") as f:
        json.dump(list(posted_links), f, indent=2)

# --- Setup ---
async def main():
    app = Application.builder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jobs", jobs))
    app.add_handler(CommandHandler("internships", internships))
    app.add_handler(CommandHandler("govjobs", govjobs))
    app.add_handler(CommandHandler("results", results))
    app.add_handler(CommandHandler("admitcard", admitcard))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    # Schedule RSS check every 30 minutes
    app.job_queue.run_repeating(
        check_rss_feeds,
        interval=30*60,  # 30 minutes
        first=10  # First run after 10 seconds
    )

    print("Bot Running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())