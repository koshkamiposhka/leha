FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code


COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /code/


CMD ["python", "bot/bot.py"]