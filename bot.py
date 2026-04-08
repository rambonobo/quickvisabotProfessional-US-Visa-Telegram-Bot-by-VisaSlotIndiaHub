import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔹 B1/B2 Visa Updates", callback_data='b1b2')],
        [InlineKeyboardButton("🎓 F1/F2 Visa Updates", callback_data='f1')],
        [InlineKeyboardButton("👨‍💼 H1B/H4 Visa Updates", callback_data='h1b')],
        [InlineKeyboardButton("🇨🇦 Canada Visa", callback_data='canada')],
        [InlineKeyboardButton("🇩🇪 Germany Visa", callback_data='germany')],
        [InlineKeyboardButton("📞 Talk to Our Team", callback_data='support')],
    ]

    await update.message.reply_text(
        "👋 Welcome to QuickVisaBot — VisaSlotIndiaHub\n\n"
        "🚀 Real-time visa slot alerts + expert booking support\n\n"
        "📌 B1/B2 | F1/F2 | H1B/H4 | Dropbox | Canada\n\n"
        "🌐 www.visaslotindiahub.com\n"
        "📞 +91 91105 91822\n\n"
        "👇 Choose your category:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    asyncio.create_task(follow_up(update, context))

async def follow_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await asyncio.sleep(45)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="⚡ Need fast visa booking help?\n👉 https://wa.me/919110591822"
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        "b1b2": "👉 https://t.me/+29iDwvXZzbszN2M1\n\n📞 Need help? https://wa.me/919110591822",
        "f1": "👉 https://t.me/+fOady0ZejI8wNzVl\n\n📞 Need help? https://wa.me/919110591822",
        "h1b": "👉 https://t.me/+kFVzGM4QmEc4NTE1\n\n📞 Need help? https://wa.me/919110591822",
        "canada": "👉 https://t.me/+zAyjmLnc8EszNjE1\n\n📞 Need help? https://wa.me/919110591822",
        "germany": "👉 https://t.me/+x5tV-kiMAag1MGU1\n\n📞 Need help? https://wa.me/919110591822",
        "support": "📞 Talk to our team:\n👉 https://wa.me/919110591822"
    }

    await query.edit_message_text(responses.get(query.data, "Error"))

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))

    app.run_polling(drop_pending_updates=True)
