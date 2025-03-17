from entities import db, BaseModel
from peewee import TextField
from .utils import str_uuid


class Cert(BaseModel):
    name = TextField()
    code = TextField(default=str_uuid)


def init_cert():
    db.create_tables([Cert])
