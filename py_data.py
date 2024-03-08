import telebot
with open('key.txt', 'r') as file:
    # Define your token here
    TELEGRAM_BOT_TOKEN = file.read()

# Create an instance of the bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)