from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8826668549:AAFYD0rdk4NcPHpz6CXQBknQSsI0VZDJ_B8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Daily Jobs Alert\n\nJoin: https://t.me/jobhuntez"
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()

    if "job" in msg:
        await update.message.reply_text("📢 Latest jobs: https://t.me/jobhuntez")
    else:
        await update.message.reply_text("✅ Join channel: https://t.me/jobhuntez")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Bot Running...")
app.run_polling()