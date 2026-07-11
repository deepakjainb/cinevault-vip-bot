from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Join Free Channel", url="https://t.me/CineVault_Free")],
        [InlineKeyboardButton("💎 VIP Membership", url="https://t.me/CineVaultPremium")],
        [InlineKeyboardButton("📞 Contact Admin", url="https://t.me/Itz_Deepak_006]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎬 *Welcome to CineVault VIP*\n\nChoose an option below:",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
