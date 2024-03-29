FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Установим директорию для работы

WORKDIR /tg_bot

COPY ./requirements.txt ./

# Устанавливаем зависимости и gunicorn
RUN apt-get update && \
    apt-get install -y ffmpeg
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt


# Копируем файлы и билд
COPY ./ ./

RUN chmod -R 777 ./