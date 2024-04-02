from src.my_sql_connect import connect, from_timestamp_to_date
from time import time
def log_tts(user_id, message_text):
    connection = connect()
    cursor = connection.cursor()
    sql = "INSERT INTO tts_log (user_id, data, text) VALUES (%s, %s, %s)"
    data = (user_id, from_timestamp_to_date(time()), message_text)
    cursor.execute(sql, data)
    connection.commit()
    cursor.close()
    connection.close( )