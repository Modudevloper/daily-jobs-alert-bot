from telegram import Update
from telegram.ext import (
Application,
CommandHandler,
MessageHandler,
filters,
ContextTypes,
)

TOKEN = "YOUR_NEW_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"👋 Welcome to Daily Jobs Alert\n\nJoin: https://t.me/jobhuntez"
)

async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"📢 Latest Jobs\nhttps://t.me/jobhuntez"
)

async def internships(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"🎓 Latest Internships\nhttps://t.me/jobhuntez"
)

async def govjobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"🏛 Government Jobs\nhttps://t.me/jobhuntez"
)

async def results(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"📄 Exam Results\nhttps://t.me/jobhuntez"
)

async def admitcard(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"🪪 Admit Cards\nhttps://t.me/jobhuntez"
)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"Use /jobs /internships /govjobs /results /admitcard"
)

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
text = update.message.text.lower()

```
if "job" in text:
    await update.message.reply_text(
        "📢 Latest Jobs:\nhttps://t.me/jobhuntez"
    )
else:
    await update.message.reply_text(
        "✅ Join Channel:\nhttps://t.me/jobhuntez"
    )
```

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("jobs", jobs))
app.add_handler(CommandHandler("internships", internships))
app.add_handler(CommandHandler("govjobs", govjobs))
app.add_handler(CommandHandler("results", results))
app.add_handler(CommandHandler("admitcard", admitcard))
app.add_handler(CommandHandler("help", help_cmd))

app.add_handler(
MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
)

print("Bot Running...")
app.run_polling()
