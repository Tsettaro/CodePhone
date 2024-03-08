import json, os

def check_and_add_user(user_id, username, date_of_start):
    if not os.path.exists('user_sectret_data'):
        os.makedirs('user_sectret_data')

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
                "count_of_voice_message": 1,
            }
        else:
            # Обновить информацию о существующем пользователе
            data[str(user_id)]["count_of_voice_message"] += 1
            # Записать обновленные данные обратно в файл
        with open('user_sectret_data/user.json', 'w') as file:
            json.dump(data, file)
        