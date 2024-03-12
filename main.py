from py_data import bot
import user_func as js, os
from guard import rate_limit
from VTT import recognize_vosk, recognize_whisper
# Define the start command handler function
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello! I am your bot.")
    js.check_and_add_user(message.from_user.id, str(message.from_user.first_name), message.date)

# Define the echo function to repeat messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    wait = rate_limit(message)
    if wait == 0:
        bot.reply_to(message, message.text)
        bot.send_message(message.chat.id, str(message.from_user.first_name))
    else:
        bot.reply_to(message, f'Извините, но нужно подождать {round(wait)} секунд после использования предыдущей команды.')
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    wait = rate_limit(message)
    if wait == 0:
        bot.reply_to(message, "Вы прислали голосовое сообщение. Да начнётся этап дешифрования!")
        js.check_and_add_user(message.from_user.id, str(message.from_user.first_name), message.date)
        wav = js.save_audio(message.from_user.id, bot.get_file(message.voice.file_id), message.date)
        #bot.reply_to(message, f"Расшифровка голосового сообщения: \n{recognize_vosk(wav)}")
        bot.reply_to(message, f"Расшифровка голосового сообщения:\n{recognize_whisper(wav)}")
    else:
        bot.reply_to(message, f'Извините, но нужно подождать {round(wait)} секунд после использования предыдущей команды.')

# Main function to start the bot
def main():
    bot.polling()

if __name__ == '__main__':
    main()