import os
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN
from core.menu import start_menu, handle_menu
from core.storage import ensure_storage
from core.filesystem import handle_text_reply

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start_menu(update, context)

def main():
    ensure_storage()
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_reply))

    app.run_polling()

if __name__ == "__main__":
    main()
