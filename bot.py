import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

users_data = {}

# STEP 1: START → ASK NAME
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to QuickVisaBot — Powered by VisaSlotIndiaHub\n\n"
        "We help you get US Visa slots faster with expert support.\n\n"
        "👉 First, please enter your *Name:*",
        parse_mode="Markdown"
    )

# STEP 2: SAVE NAME → ASK PHONE
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    name = update.message.text

    users_data[user_id] = {"name": name}

    button = KeyboardButton("📱 Share Phone Number", request_contact=True)
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True, one_time_keyboard=True)

    await update.message.reply_text(
        "📞 Please share your WhatsApp number:",
        reply_markup=keyboard
    )

# STEP 3: SAVE PHONE → ASK CATEGORY
async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    phone = update.message.contact.phone_number

    users_data[user_id]["phone"] = phone

    keyboard = [
        [InlineKeyboardButton("🔹 B1/B2", callback_data='b1b2')],
        [InlineKeyboardButton("🎓 F1/F2", callback_data='f1')],
        [InlineKeyboardButton("👨‍💼 H Visa", callback_data='h1b')],
        [InlineKeyboardButton("🇨🇦 Canada", callback_data='canada')],
        [InlineKeyboardButton("🇩🇪 Germany", callback_data='germany')],
    ]

    await update.message.reply_text(
        "🎯 Select your visa category:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# STEP 4: SAVE CATEGORY + RESPOND
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    category = query.data

    users_data[user_id]["category"] = category

    print("🔥 FULL LEAD:", users_data[user_id])

    responses = {
        "b1b2": "👉 https://t.me/+29iDwvXZzbszN2M1",
        "f1": "👉 https://t.me/+fOady0ZejI8wNzVl",
        "h1b": "👉 https://t.me/+kFVzGM4QmEc4NTE1",
        "canada": "👉 https://t.me/+zAyjmLnc8EszNjE1",
        "germany": "👉 https://t.me/+x5tV-kiMAag1MGU1",
    }

    await query.edit_message_text(
        f"✅ You're all set!\n\n{responses.get(category)}\n\n📞 Our team will contact you shortly!"
    )

# MAIN
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_name))
    app.add_handler(MessageHandler(filters.CONTACT, get_phone))
    app.add_handler(CallbackQueryHandler(handle_buttons))

    app.run_polling(drop_pending_updates=True)
