FROM python:3

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY src/ /bot/

CMD ["python3", "/bot/bot.py"]