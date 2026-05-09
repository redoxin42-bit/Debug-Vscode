from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def start_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton("👤 Профиль", callback_data="profile")],
        [InlineKeyboardButton("📁 Основные папки", callback_data="main_folders")],
        [InlineKeyboardButton("➕ Добавить папку", callback_data="add_folder")],
        [InlineKeyboardButton("📦 Добавить проект", callback_data="add_project")],
        [InlineKeyboardButton("📛 Добавить пакет", callback_data="add_package")],
        [InlineKeyboardButton("🤖 /ai", callback_data="ai")],
        [InlineKeyboardButton("🔨 Build Apk", callback_data="build_apk")],
    ]
    text = "Добро пожаловать. Выберите действие:"
    if update.message:
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.callback_query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb))

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data

    if data == "profile":
        await q.message.edit_text("Профиль проекта. Здесь будут данные о папках, проектах и пакете.")
    elif data == "main_folders":
        await q.message.edit_text("Здесь будет список основных Android-папок.")
    elif data == "add_folder":
        await q.message.edit_text("Отправь путь к своей папке.")
        context.user_data["awaiting"] = "add_folder"
    elif data == "add_project":
        await q.message.edit_text("Отправь название проекта и путь к нему.")
        context.user_data["awaiting"] = "add_project"
    elif data == "add_package":
        await q.message.edit_text("Отправь пакет, например: com.example.app")
        context.user_data["awaiting"] = "add_package"
    elif data == "ai":
        await q.message.edit_text("Отправь команду /ai с папкой, файлом и задачей.")
    elif data == "build_apk":
        await q.message.edit_text("Запуск сборки APK будет добавлен здесь.")
