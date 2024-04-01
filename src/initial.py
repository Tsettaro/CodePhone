import telebot, os
#Check the existence key
if not os.path.exists('secrets/key.txt'):
    print("ERROR! Key doesn't exist! Please, contact with @useless_acc for futher information")
    exit()
with open('secret/key.txt', 'r') as file:
    # Define your token here
    TELEGRAM_BOT_TOKEN = file.read()

# Create an instance of the bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)