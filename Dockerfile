FROM python:3.12-alpine

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .

CMD python -u src/main.py
