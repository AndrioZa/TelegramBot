from dotenv import load_dotenv  # импортируем функцию для загрузки .env
import os  # импортируем модуль для работы с переменными окружения

# Загружаем все переменные из файла .env
load_dotenv()

# Получаем ключи из .env
openai_api_key = os.getenv("OPENAI_API_KEY")
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

# Проверим, что ключи читаются правильно
print("OpenAI API Key:", openai_api_key)
print("Telegram Bot Token:", bot_token)

