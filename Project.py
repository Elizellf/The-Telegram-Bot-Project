import telebot
import random

# Ввод токена бота
TOKEN = 'ТОКЕН'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, " + message.from_user.first_name)  # Фраза приветствия

# Обработчик сообщений с приветствием
@bot.message_handler(func=lambda message: message.text.lower() in ["привет!", "привет"])
def send_hello(message):
    bot.reply_to(message, "Привет-привет!")

# Обработчик сообщений с вопросом "Как дела?"
@bot.message_handler(func=lambda message: message.text.lower() in ["как дела?", "как дела"])
def send_status(message):
    responses = [
        "Все хорошо, новостей нет. Как твои дела?",
        "Дела идут прекрасно, активно работаю над своими проектами. А у тебя?",
        "Все отлично. А у тебя как дела, какие новости?"
    ]
    bot.reply_to(message, random.choice(responses))  # Выбор случайного варианта ответа

# Обработчик ответа 
@bot.message_handler(func=lambda message: True)
def reply_to_other_messages(message):
    bot.reply_to(message, "Cпасибо за сообщение.")

# Запуск бота
def start_bot():
    bot.polling()
