from entities.db import BaseModel, db
from peewee import TextField, IntegerField
from uuid import uuid4 as uuid


def generate_code():
    return str(uuid())


class Link(BaseModel):
    code = TextField(default=generate_code)
    count = IntegerField()


def init_link():
    db.create_tables([Link])
