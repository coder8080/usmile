from peewee import IntegerField, TextField
from .db import BaseModel, db


class User(BaseModel):
    chat_id = IntegerField()
    username = TextField()
    count = IntegerField(default=0)


def init_user():
    db.create_tables([User])
