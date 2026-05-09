from telegram.ext import ContextTypes
from core.storage import load_data, save_data

async def handle_text_reply(update, context: ContextTypes.DEFAULT_TYPE):
    if "awaiting" not in context.user_data:
        return

    text = update.message.text.strip()
    awaiting = context.user_data["awaiting"]
    data = load_data()

    if awaiting == "add_folder":
        data["folders"].append(text)
        save_data(data)
        await update.message.reply_text(f"Папка добавлена: {text}")
    elif awaiting == "add_project":
        data["projects"].append({"name": text, "path": text})
        save_data(data)
        await update.message.reply_text(f"Проект добавлен: {text}")
    elif awaiting == "add_package":
        data["package"] = text
        save_data(data)
        await update.message.reply_text(f"Пакет сохранён: {text}")

    context.user_data.pop("awaiting", None)
