# Базовый образ
FROM python:3.10

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /tg_bot

COPY ./requirements.txt ./

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tg_bot/requirements.txt

# Устанавливаем ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

COPY ./ ./
# Команда для запуска бота
CMD ["python", "main.py"]