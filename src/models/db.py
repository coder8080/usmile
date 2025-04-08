import peewee_async

from entities import POSTGRES_PASSWORD, POSTGRES_USER
from entities.constants import POSTGRES_HOST, POSTGRES_PORT

db = peewee_async.PsycopgDatabase(
    "usmile",
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
)


class BaseModel(peewee_async.AioModel):
    class Meta:
        database = db


db.connect()
