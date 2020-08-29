FROM python:3.7.9-slim-buster

RUN apt-get update && \
	apt-get install -y gcc make apt-transport-https ca-certificates build-essential

RUN unlink /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Samara /etc/localtime

COPY . /app

WORKDIR  /app

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]