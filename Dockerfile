FROM python:3.11

RUN mkdir /telegrambot

WORKDIR /telegrambot

COPY . /telegrambot

RUN pip install pyparsing

RUN pip install --upgrade pip setuptools

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "bot.py" ]
