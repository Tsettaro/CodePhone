from time import time

last_call = {}
def rate_limit(message):
    user_id = message.from_user.id
    current_time = time()
    if user_id in last_call:
        last_call_time = last_call[user_id]
        # Чтобы в выводе не висело время ожидания в 0 секунд
        if current_time - last_call_time < 9:
            return (10 - (current_time - last_call_time))
    last_call[user_id] = current_time
    return 0