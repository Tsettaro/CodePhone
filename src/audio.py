import json, os, subprocess
from pathlib import Path
from src.initial import bot
from src.my_sql_connect import from_timestamp_to_date

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
    return filename_path+'.wav'