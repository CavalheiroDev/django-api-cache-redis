FROM python:3.10.1-slim

WORKDIR /code

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update \
    && apt install python3-dev default-libmysqlclient-dev build-essential libaio1 -y \
    && apt clean -y \
    && apt autoclean -y \
    && apt autoremove -y  

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . . 