FROM python:3.11-slim

COPY ./srv_mtga_be_fa /home/app

WORKDIR /home/app

RUN pip3.11 install --upgrade pip
RUN pip3.11 install poetry
RUN poetry install --no-dev

ENTRYPOINT [ "poetry", "run", "python", "./main.py" ]