from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from handlers.pempek import handle_pempek
from handlers.study import handle_study
from handlers.schedule import handle_schedule
from config import TOKEN

# Menu Utama
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("📝 Laporan Pempek", callback_data="pempek")],
        [InlineKeyboardButton("📚 Study BULOG", callback_data="study")],
        [InlineKeyboardButton("⏰ Jadwal Harian", callback_data="schedule")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Halo bro! Pilih menu di bawah ini:", reply_markup=reply_markup)

# Handle Callback
async def handle_callback(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "pempek":
        await handle_pempek(update, context)
    elif query.data == "study":
        await handle_study(update, context)
    elif query.data == "schedule":
        await handle_schedule(update, context)

# Main Function
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))

    print("🚀 Bot berjalan!")
    app.run_polling()
