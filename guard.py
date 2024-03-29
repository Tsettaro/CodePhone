from time import time
import os, json
def existence(name):
    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.exists(f'data/{name}.json') or os.path.getsize(f'data/{name}.json') == 0:
        with open(f'data/{name}.json', 'w') as file:
            json.dump({}, file)

def make_fcking_dumps(data, name):
    with open(f'data/{name}.json', 'w') as file:
        json.dump(data, file)

def rate_limit(message):
    existence("last_command_user")
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
        make_fcking_dumps(data, "last_command_user")

        if str(user_id) in data and (current_time != data[str(user_id)]["last_timestamp"]):
            last_call_time = data[str(user_id)]["last_timestamp"]
            # Чтобы в выводе не висело время ожидания в 0 секунд
            if current_time - last_call_time < 9:
                return (10 - (current_time - last_call_time))
        data[str(user_id)]["last_timestamp"] = current_time
        make_fcking_dumps(data, "last_command_user")
        return 0

def user_in_da_house(message, status):
    existence("anti-DDOS")
    with open('data/anti-DDOS.json', 'r') as file:
        user_id = message.from_user.id
        data = json.load(file)
        if str(user_id) not in data:
            # Добавить информацию о новом пользователе
            data[str(user_id)] = {
                "status": "execute",
            }
        # Записать обновленные данные обратно в файл
            make_fcking_dumps(data, "anti-DDOS")
            return True

        elif str(user_id) in data and data[str(user_id)]["status"] == "execute":
            data[str(user_id)]["status"] = "delete"
            make_fcking_dumps(data, "anti-DDOS")
            return True
        else:
            # Delete user from anit-DDOS
            del data[str(user_id)]
            make_fcking_dumps(data, "anti-DDOS")
            return False