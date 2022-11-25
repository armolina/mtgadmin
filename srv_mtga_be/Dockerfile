FROM python:3.9-slim

COPY ./srv_mtga_be /home/app

WORKDIR /home/app

RUN pip3.9 install --upgrade pip
RUN pip3.9 install -r requirements.txt

CMD [ "python3.9", "-u", "main.py" ]