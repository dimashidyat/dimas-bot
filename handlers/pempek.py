from telegram import Update

async def handle_pempek(update: Update, context):
    await update.callback_query.edit_message_text("📝 Laporan Pempek belum dibuat.")
 
