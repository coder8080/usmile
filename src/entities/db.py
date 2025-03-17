import peewee_async
from entities.constants import POSTGRES_USER, POSTGRES_PASSWORD

db = peewee_async.PooledPostgresqlDatabase('usmile',
                                           user=POSTGRES_USER,
                                           password=POSTGRES_PASSWORD,
                                           host="postgres",
                                           port=5432)


class BaseModel(peewee_async.AioModel):
    class Meta:
        database = db


db.connect()
