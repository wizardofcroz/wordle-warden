# syntax = docker/dockerfile:1.2
FROM python:3
FROM gorialis/discord.py

RUN --mount=type=secret,id=discord,dst=/discord.key

RUN mkdir -p /usr/src/bot
WORKDIR /usr/src/bot

COPY . .

CMD [ "python3", "main.py" ]
