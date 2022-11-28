FROM python:3.10-slim

COPY ./ /home/app

WORKDIR /home/app

RUN pip3.10 install --upgrade pip
RUN pip3.10 install poetry
RUN poetry install --no-dev

ENTRYPOINT [ "poetry", "run", "python", "./mtg/main.py" ]