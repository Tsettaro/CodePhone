import mysql.connector, os
from datetime import datetime
SQL_KEY = []

def from_timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

def check_key():
    global SQL_KEY
    if not os.path.exists('secrets/sql.txt'):
        print("ERROR! Sql_key doesn't exist! Please, contact with @useless_acc for futher information")
        exit()
    with open('secrets/sql.txt', 'r') as file:
        # Define your token here
        SQL_KEY = file.read().split(":")
        if len(SQL_KEY) < 4:
            return False
    return True

def check_user(user_id):
    if check_key():
        with open('secrets/sql.txt', 'r') as file:
        # Define your token here
            SQL_KEY = file.read().split(":")
        connection = mysql.connector.connect(
        host=SQL_KEY[0],
        user=SQL_KEY[1],
        password=SQL_KEY[2],
        database=SQL_KEY[3]
        )

        cursor = connection.cursor()
        select_query = f"SELECT * FROM users WHERE ID = {user_id}"
        cursor.execute(select_query)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result == None:
            cursor.close()
            connection.close()
            return False
            
        else:
            cursor.close()
            connection.close()
            return True
    else:
        exit()

def add_user(user_id, username, timestamp):
    if check_key():
        with open('secrets/sql.txt', 'r') as file:
        # Define your token here
            SQL_KEY = file.read().split(":")
        connection = mysql.connector.connect(
        host=SQL_KEY[0],
        user=SQL_KEY[1],
        password=SQL_KEY[2],
        database=SQL_KEY[3]
        )

        cursor = connection.cursor()
        select_query = f"SELECT * FROM users WHERE ID = {user_id}"
        cursor.execute(select_query)
        result = cursor.fetchone()
        if result:
            pass
        else:
            print(user_id)
            sql = "INSERT INTO users (ID, name, reg_date, count_of_voice_messages, count_of_text_messages) VALUES (%s, %s, %s, %s, %s)"
            data = (user_id, username, from_timestamp_to_date(timestamp), 0, 0)
            cursor.execute(sql, data)
            connection.commit()
            cursor.close()
            connection.close( )
    else:
        exit()

def add_count(user_id, voice_messages_count, text_messages_count):
    with open('secrets/sql.txt', 'r') as file:
        # Define your token here
        SQL_KEY = file.read().split(":")
    connection = mysql.connector.connect(
      host=SQL_KEY[0],
      user=SQL_KEY[1],
      password=SQL_KEY[2],
      database=SQL_KEY[3]
    )

    cursor = connection.cursor()
    sql = "UPDATE users SET count_of_voice_messages = count_of_voice_messages + %s, count_of_text_messages = count_of_text_messages + %s WHERE ID = %s"
    cursor.execute(sql, (voice_messages_count, text_messages_count, user_id))
    connection.commit()
    cursor.close()
    connection.close( )