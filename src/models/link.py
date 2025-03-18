from peewee import TextField, IntegerField, BooleanField

from entities import BOT_NAME
from .db import BaseModel, db
from .utils import str_uuid


class Link(BaseModel):
    code = TextField(default=str_uuid)
    count = IntegerField(null=False)
    used = BooleanField(default=False)

    def render(self):
        return f"https://t.me/{BOT_NAME}?start={self.code}"


def init_link():
    db.create_tables([Link])
