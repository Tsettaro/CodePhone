from src.initial import bot
from src.guard import rate_limit, user_in_da_house
from src.VTT import recognize_whisper
from src.TTS import tts
from src.log import log_user, log_tts_text
import src.audio as js, os
import src.my_sql_connect as sql

# Define the start command handler function
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello! I am your bot.")
    sql.add_user(message.from_user.id, str(message.from_user.first_name), message.date)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if sql.check_user(message.from_user.id):
        wait = rate_limit(message)
        if wait == 0:
            bot.reply_to(message, "Да грядёт послание человеческое в виде голоса машины ящерской!")
            try:
                tts(message.text)
                sql.add_count(message.from_user.id, 0, 1)
            except:
                bot.reply_to(message, f'Ах ты {message.from_user.first_name} окаянный! Пришли другое нам послание!')
            if os.path.exists("audio_text.ogg"):
                bot.send_voice(message.chat.id, open('audio_text.ogg', 'rb'))
                os.remove("audio_text.ogg")
        else:
            bot.reply_to(message, f'Извините, но нужно подождать {round(wait)} секунд после использования предыдущей команды.')
    else:
        bot.reply_to(message, "Please, restart bot with command /start")
@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    if sql.check_user(message.from_user.id):
        if user_in_da_house(message, 1):
            wait = rate_limit(message)
            if wait == 0:
                bot.reply_to(message, "Вы прислали голосовое сообщение. Да начнётся этап дешифрования!")
                wav = js.save_audio(message.from_user.id, bot.get_file(message.voice.file_id), message.date)
                bot.reply_to(message, f"Расшифровка голосового сообщения:\n{recognize_whisper(wav)}")
                sql.add_count(message.from_user.id, 1, 0)
            else:
                bot.reply_to(message, f'Извините, но нужно подождать {round(wait)} секунд после использования предыдущей команды.')
            user_in_da_house(message, 0)
        else:
            bot.reply_to(message, "Вы не можете использовать эту команду пока обрабатывается предыдущее голосовое сообщение!")
    else:
        bot.reply_to(message, "Please, restart bot with command /start")

# Main function to start the bot
def main():
    bot.polling()

if __name__ == '__main__':
    main()