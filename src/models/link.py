from entities.db import BaseModel, db
from peewee import TextField, IntegerField, BooleanField
from uuid import uuid4 as uuid


def generate_code():
    return str(uuid())


class Link(BaseModel):
    code = TextField(default=generate_code)
    count = IntegerField(null=False)
    used = BooleanField(default=False)

    def render(self):
        return f"https://t.me/usmile_cert_bot?start={self.code}"


def init_link():
    db.create_tables([Link])
