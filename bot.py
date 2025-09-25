import os
from telegram.ext import ApplicationBuilder

# Берём токен из переменной окружения Render
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

# Создаём приложение
app = ApplicationBuilder().token(telegram_bot_token).build()


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import os
from dotenv import load_dotenv

load_dotenv()

telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context):
    await update.message.reply_text(
        "Привет! 👋\nЯ бот, который поможет тебе с ежедневным отчетом.\n"
        "📌 Если ты напишешь слово 'форма', я пришлю тебе форму.\n"
        "⏰ 21:00 я буду каждый день напоминать."
    )

async def handle_message(update: Update, context):
    text = update.message.text.lower()
    if "форма" in text:
        await update.message.reply_text(
            "Вот ссылка на форму: https://docs.google.com/forms/d/e/1FAIpQLScZEVk0ByvRxf7xB2VJlDZzkwhECkfauAVYWmxvnq3VTW3iUA/viewform?usp=dialog"
        )
    else:
        await update.message.reply_text("Я пока умею только отправлять форму. Напиши 'форма'.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(telegram_bot_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен...")
    app.run_polling()
