import json, os
from pathlib import Path
from datetime import datetime
from py_data import bot
import subprocess

def from_timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
  
def check_and_add_user(user_id, username, timestamp):
    date_of_start = from_timestamp_to_date(timestamp)
    
    if not os.path.exists('user_sectret_data/user.json') or os.path.getsize('user_sectret_data/user.json') == 0:
        with open('user_sectret_data/user.json', 'w') as file:
            json.dump({}, file)
    
    with open('user_sectret_data/user.json', 'r') as file:
        data = json.load(file)
        if str(user_id) not in data:
            # Добавить информацию о новом пользователе
            data[str(user_id)] = {
                "user": username,
                "date_of_start": date_of_start,
                "count_of_voice_message": 0,
            }
        # Записать обновленные данные обратно в файл
        with open('user_sectret_data/user.json', 'w') as file:
            json.dump(data, file)

def save_audio(user_id, audio, timestamp):
    date_of_start = from_timestamp_to_date(timestamp)
    
    if not os.path.exists('user_voice_messages'):
        os.makedirs('user_voice_messages')
    
    if not os.path.exists('user_voice_messages/' + str(user_id)):
        os.makedirs('user_voice_messages/' + str(user_id))
    
    # Define the directory path
    directory_path = str(Path('user_voice_messages/' + str(user_id))).replace('\\', '/')
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    # Define a list of audio file extensions
    voice = bot.get_file(audio.file_id)
    
    filename_path = directory_path + '/' +(str(date_of_start).replace(':','_').replace('-','_'))
    
    with open(filename_path+'.oga', 'wb') as file:
        file.write(bot.download_file(voice.file_path))
    subprocess.run(['ffmpeg', '-i', filename_path+'.oga', filename_path+'.wav'])
    os.remove(filename_path+'.oga')
    with open('user_sectret_data/user.json', 'r') as file:
        data = json.load(file)
        data[str(user_id)]["count_of_voice_message"] += 1
        with open('user_sectret_data/user.json', 'w') as file:
            json.dump(data, file)
    return filename_path+'.wav'