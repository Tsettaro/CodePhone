from time import time
import os, json

def existence():
    if not os.path.exists('data'):
        os.makedirs('data')
        
    if not os.path.exists('data/last_command_user.json') or os.path.getsize('data/last_command_user.json') == 0:
        with open('data/last_command_user.json', 'w') as file:
            json.dump({}, file)


def rate_limit(message):
    existence()
    with open('data/last_command_user.json', 'r') as file:
        user_id = message.from_user.id
        current_time = time()
        data = json.load(file)
        if str(user_id) not in data:
            # Добавить информацию о новом пользователе
            data[str(user_id)] = {
                "last_timestamp": current_time,
            }
        # Записать обновленные данные обратно в файл
        with open('data/last_command_user.json', 'w') as file:
            json.dump(data, file)

        if str(user_id) in data and (current_time != data[str(user_id)]["last_timestamp"]):
            last_call_time = data[str(user_id)]["last_timestamp"]
            # Чтобы в выводе не висело время ожидания в 0 секунд
            if current_time - last_call_time < 9:
                return (10 - (current_time - last_call_time))
        data[str(user_id)]["last_timestamp"] = current_time
        with open('data/last_command_user.json', 'w') as file:
            json.dump(data, file)
        return 0