from peewee import BigIntegerField, IntegerField, TextField

from .db import BaseModel, db


class User(BaseModel):
    chat_id = BigIntegerField()
    username = TextField()
    count = IntegerField(default=0)

    def info(self):
        return f"{self.username}:{self.chat_id}"


def init_user():
    db.create_tables([User])
