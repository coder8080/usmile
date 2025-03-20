FROM pypy:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .

CMD ["pypy3", "-u", "src/main.py"]
