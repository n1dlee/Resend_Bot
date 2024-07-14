import logging
import sqlite3
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Токен вашего бота
TOKEN = '7208868281:AAHvJlXSvSn82-N3u06hhzd4v2Ni7ynV_uA'

# Список идентификаторов пользователей
USERS = ['1574853222', '6721664987']

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS state
                      (id INTEGER PRIMARY KEY, current_receiver INTEGER)''')
    cursor.execute('''INSERT INTO state (id, current_receiver)
                      SELECT 1, 0 WHERE NOT EXISTS (SELECT 1 FROM state WHERE id=1)''')
    conn.commit()
    conn.close()
    logger.info("Database initialized")

# Получение текущего получателя
def get_current_receiver():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT current_receiver FROM state WHERE id=1')
    current_receiver = cursor.fetchone()[0]
    conn.close()
    logger.info(f"Current receiver: {current_receiver}")
    return current_receiver

# Обновление текущего получателя
def update_current_receiver(new_receiver):
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE state SET current_receiver=? WHERE id=1', (new_receiver,))
    conn.commit()
    conn.close()
    logger.info(f"Updated current receiver to: {new_receiver}")

# Обработчик сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_receiver = get_current_receiver()
    user_id = USERS[current_receiver]

    # Отправка сообщения текущему получателю
    await context.bot.send_message(chat_id=user_id, text=update.message.text)
    logger.info(f"Message sent to {user_id}: {update.message.text}")

    # Обновление получателя
    new_receiver = (current_receiver + 1) % len(USERS)
    update_current_receiver(new_receiver)

# Основная функция
def main() -> None:
    init_db()
    application = Application.builder().token(TOKEN).build()

    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUP, handle_message))

    logger.info("Bot started")

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
