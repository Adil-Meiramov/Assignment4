# Импортируем нужные классы из библиотеки telegram
from telegram.ext import ApplicationBuilder, CommandHandler

# Импортируем функции-команды из файла handlers.py
from handlers import start, help_command, config, log, summary, notify_on, notify_off

# Токен твоего Telegram-бота (получен от @BotFather)
TOKEN = "7925467325:AAEmktmkS0iQidievaDMpJpXY6wcp0FSaws"

# Создаём приложение Telegram бота
app = ApplicationBuilder().token(TOKEN).build()

# Подключаем обработчики команд
app.add_handler(CommandHandler("start", start))           # Команда /start
app.add_handler(CommandHandler("help", help_command))     # Команда /help
app.add_handler(CommandHandler("config", config))         # Команда /config <категория> <бюджет>
app.add_handler(CommandHandler("log", log))               # Команда /log <категория> <+/-сумма>
app.add_handler(CommandHandler("summary", summary))       # Команда /summary
app.add_handler(CommandHandler("notifyon", notify_on))    # Команда /notifyon
app.add_handler(CommandHandler("notifyoff", notify_off))  # Команда /notifyoff

# Запуск бота в режиме "опроса" (постоянное ожидание новых сообщений)
if __name__ == "__main__":
    print("Бот запущен. Нажми Ctrl+C для остановки.")
    app.run_polling()

