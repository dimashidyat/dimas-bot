from telegram import Update
from config import DEFAULT_SCHEDULE

async def handle_schedule(update: Update, context):
    schedule = "\n".join([f"{key.capitalize()}: {value}" for key, value in DEFAULT_SCHEDULE.items()])
    await update.callback_query.edit_message_text(f"⏰ Jadwal Harian:\n\n{schedule}")
 
