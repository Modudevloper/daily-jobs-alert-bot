from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = "8826668549:AAFYD0rdk4NcPHpz6CXQBknQSsI0VZDJ_B8"
YOUR_USERNAME = "@M_oo_d_off"

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

async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎨 Portfolio Design Resources:\nhttps://t.me/jobhuntez"
    )

async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📄 Resume Maker Website:\nhttps://t.me/jobhuntez"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Reply to user
    await update.message.reply_text("Use /jobs /internships /govjobs /portfolio /resume")

    # Send DM to you
    user = update.message.from_user
    username = f"@{user.username}" if user.username else user.first_name
    try:
        await context.bot.send_message(
            chat_id=YOUR_USERNAME,
            text=f"🆘 Help requested by: {username}"
        )
    except:
        pass

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "job" in text:
        await update.message.reply_text(
            "📢 Latest Jobs:\nhttps://t.me/jobhuntez"
        )
    else:
        await update.message.reply_text(
            "✅ Join Channel:\nhttps://t.me/jobhuntez"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("jobs", jobs))
app.add_handler(CommandHandler("internships", internships))
app.add_handler(CommandHandler("govjobs", govjobs))
app.add_handler(CommandHandler("portfolio", portfolio))
app.add_handler(CommandHandler("resume", resume))
app.add_handler(CommandHandler("help", help_cmd))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
)

print("Bot Running...")
app.run_polling()