FROM python:3.6

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./ .

COPY ./.env .

CMD python3 src/MusicBot/main.py
