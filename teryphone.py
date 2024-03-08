from py_data import bot
import check_user as js
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
    js.check_and_add_user(message.from_user.id, str(message.from_user.first_name + " " + message.from_user.last_name), str(message.date))
    with open('new_file.ogg', 'wb') as new_file:
        new_file.write(bot.download_file(voice.file_path))

# Main function to start the bot
def main():
    bot.polling()

if __name__ == '__main__':
    main()