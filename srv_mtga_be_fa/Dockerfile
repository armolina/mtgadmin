FROM python:3.9-slim

COPY ./srv_mtga_be_fa /home/app

WORKDIR /home/app

RUN pip3.9 install --upgrade pip
RUN pip3.9 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]