from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔹 B1/B2 Visa Updates", callback_data='b1b2')],
        [InlineKeyboardButton("🎓 F1/F2 Visa Updates", callback_data='f1')],
        [InlineKeyboardButton("🎓 F1/F2 Refused Slots", callback_data='f1refused')],
        [InlineKeyboardButton("👨‍💼 H1B/H4 Visa Updates", callback_data='h1b')],
        [InlineKeyboardButton("📭 Dropbox Appointments", callback_data='dropbox')],
        [InlineKeyboardButton("🇨🇦 Canada to US Slots", callback_data='canada')],
        [InlineKeyboardButton("⛔ B1/B2 Refused Slots", callback_data='b1refused')],
        [InlineKeyboardButton("🧾 DS-160 / Consultation Help", callback_data='consult')],
        [InlineKeyboardButton("🏢 Corporate Visa Services", callback_data='corporate')],
        [InlineKeyboardButton("✈️ Partner with Us (Travel Agencies)", callback_data='travel')],
        [InlineKeyboardButton("📞 Talk to Our Team", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Welcome to QuickVisaBot — Powered by VisaSlotIndiaHub\n\n"
        "We help you get US Visa slots faster, smarter, and with expert support.\n\n"
        "📌 What We Offer:\n"
        "• Real-time visa slot alerts for all categories:\n"
        "   - B1/B2 (Tourist/Business)\n"
        "   - F1/F2 (Students & Dependents)\n"
        "   - Refused Slots (B1/B2 & F1/F2)\n"
        "   - H1B/H4 (Work & Family)\n"
        "   - Dropbox Appointments\n"
        "   - Canada to US cross-bookings\n"
        "• DS-160 form help & Mock Interviews\n"
        "• Corporate & Travel Agency Solutions\n\n"
        "🌐 www.visaslotindiahub.com\n"
        "📞 +91 91105 91822\n"
        "📩 contact@visaslotindiahub.com\n\n"
        "👇 Choose your category or service:",
        reply_markup=reply_markup
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    responses = {
        "b1b2": "📍 B1/B2 Visa Slot Group:\n👉 https://t.me/+29iDwvXZzbszN2M1",
        "f1": "🎓 F1/F2 Visa Slot Group:\n👉 https://t.me/+fOady0ZejI8wNzVl",
        "f1refused": "⛔ F1/F2 Refused Slots:\n👉 https://t.me/+fOady0ZejI8wNzVl",
        "h1b": "👨‍💼 H1B/H4 Updates:\n👉 https://t.me/+29iDwvXZzbszN2M1",
        "dropbox": "📭 Dropbox Appointments:\n👉 https://t.me/+29iDwvXZzbszN2M1",
        "canada": "🇨🇦 Canada to US Visa Slots:\n👉 https://t.me/+29iDwvXZzbszN2M1",
        "b1refused": "⛔ B1/B2 Refused Slots:\n👉 https://t.me/+29iDwvXZzbszN2M1",
        "consult": "🧾 DS-160 & Visa Help:\n🌐 www.visaslotindiahub.com\n📞 WhatsApp: +91 91105 91822\n📩 contact@visaslotindiahub.com",
        "corporate": "🏢 Corporate Visa Services\n\nWe assist companies with bulk US visa slots, documentation & real-time updates.\n\n✅ Trusted by Kohler, upGrad, and others.\n📞 +91 91105 91822\n🌐 www.visaslotindiahub.com\n📩 contact@visaslotindiahub.com",
        "travel": "✈️ Partner with Us (Travel Agencies)\n\n✅ Priority slot access for your clients\n✅ Commission-based collaboration\n✅ Dedicated team support\n📞 +91 91105 91822\n🌐 www.visaslotindiahub.com\n📩 contact@visaslotindiahub.com",
        "support": "📞 Talk to Our Team:\n💬 WhatsApp: https://wa.me/919110591822\n🌐 www.visaslotindiahub.com"
    }
    await query.edit_message_text(responses.get(query.data, "❌ Unknown option. Please try again."))

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))
    app.run_polling()