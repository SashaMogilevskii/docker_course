FROM python:3.10.7

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt


WORKDIR /app

COPY tg_bot.py tg_bot.py
COPY .env .env

ENTRYPOINT ["python", "tg_bot.py"]

