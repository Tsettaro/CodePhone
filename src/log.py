import json, os
from datetime import datetime
from time import time
k = 1
def from_timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

def log_user(user_id, username, timestamp):
    date_of_start = from_timestamp_to_date(timestamp)
    
    if not os.path.exists('data/user.json') or os.path.getsize('data/user.json') == 0:
        with open('data/user.json', 'w') as file:
            json.dump({}, file)
    
    with open('data/user.json', 'r') as file:
        data = json.load(file)
        if str(user_id) not in data:
            # Добавить информацию о новом пользователе
            data[str(user_id)] = {
                "user": username,
                "date_of_start": date_of_start,
                "count_of_voice_message": 0,
            }
        # Записать обновленные данные обратно в файл
        with open('data/user.json', 'w') as file:
            json.dump(data, file)

def log_tts_text(user_id, message_text):
    if not os.path.exists('data/tts_text.json') or os.path.getsize('data/tts_text.json') == 0:
        with open('data/tts_text.json', 'w') as file:
            json.dump({}, file)
    global k
    print(message_text)
    
    with open('data/tts_text.json', 'r') as file:
        data = json.load(file)
        data[k] = {
            "user_id": user_id,
            "date_of_start": from_timestamp_to_date(time()),
            "text": message_text,
        }
        k += 1
        # Записать обновленные данные обратно в файл
        with open('data/tts_text.json', 'w') as file:
            json.dump(data, file)