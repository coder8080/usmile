from os import getenv

TOKEN = getenv("TOKEN")
POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
ADMINS = list(map(int, getenv("ADMINS").split(',')))
