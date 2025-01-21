from telegram import Update

async def handle_study(update: Update, context):
    await update.callback_query.edit_message_text("📚 Study BULOG belum dibuat.")
