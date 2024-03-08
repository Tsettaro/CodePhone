from py_data import bot
import user_func as js, os
# Define the start command handler function
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello! I am your bot.")

# Define the help command handler function
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, "Help! I need somebody.")

# Define the echo function to repeat messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, str(message.from_user.first_name + " " + message.from_user.last_name))

@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    bot.reply_to(message, "Вы прислали голосовое сообщение. Да начнётся дешифрование!")
    voice = bot.get_file(message.voice.file_id)
    js.check_and_add_user(message.from_user.id, str(message.from_user.first_name + " " + message.from_user.last_name), message.date)
    js.save_audio(message.from_user.id, voice, message.date)

# Main function to start the bot
def main():
    if not os.path.exists('key.txt'):
        print("ERROR! Key doesn't exist! Please, contact with @useless_acc fro futher information")
        exit()
    bot.polling()

if __name__ == '__main__':
    main()