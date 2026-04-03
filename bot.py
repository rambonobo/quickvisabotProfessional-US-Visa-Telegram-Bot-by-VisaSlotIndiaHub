import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

users_data = {}

async def ask_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = KeyboardButton("📱 Share Phone Number", request_contact=True)
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True, one_time_keyboard=True)

    await update.message.reply_text(
        "📞 Please share your WhatsApp number to continue:",
        reply_markup=keyboard
    )

async def save_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    user_id = update.effective_user.id

    users_data[user_id] = {
        "name": update.effective_user.first_name,
        "phone": contact.phone_number
    }

    print("NEW LEAD:", users_data[user_id])

    await update.message.reply_text(
        "✅ Thanks! Our team will contact you soon.\n\n👇 Choose your visa category:"
    )

async def follow_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await asyncio.sleep(60)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="👋 Need help with visa slots?\n\n👉 https://wa.me/919110591822"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await ask_phone(update, context)
    asyncio.create_task(follow_up(update, context))

    keyboard = [
        [InlineKeyboardButton("🔹 B1/B2 Visa Updates", callback_data='b1b2')],
        [InlineKeyboardButton("🎓 F1/F2 Visa Updates", callback_data='f1')],
        [InlineKeyboardButton("👨‍💼 H Visa Updates", callback_data='h1b')],
        [InlineKeyboardButton("🇨🇦 Canada Visa", callback_data='canada')],
        [InlineKeyboardButton("🇩🇪 Germany Visa", callback_data='germany')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to QuickVisaBot\n\n👇 Select your category:",
        reply_markup=reply_markup
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        "b1b2": "👉 https://t.me/+29iDwvXZzbszN2M1",
        "f1": "👉 https://t.me/+fOady0ZejI8wNzVl",
        "h1b": "👉 https://t.me/+kFVzGM4QmEc4NTE1",
        "canada": "👉 https://t.me/+zAyjmLnc8EszNjE1",
        "germany": "👉 https://t.me/+x5tV-kiMAag1MGU1",
    }

    await query.edit_message_text(responses.get(query.data, "Error"))

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))
    app.add_handler(MessageHandler(filters.CONTACT, save_contact))

    app.run_polling()
