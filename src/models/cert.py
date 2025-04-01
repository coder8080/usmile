from random import randint

from peewee import BooleanField, TextField

from .db import BaseModel, db


def cert_code():
    return ''.join([str(randint(1, 9)) for _ in range(8)])


class Cert(BaseModel):
    name = TextField()
    code = TextField(default=cert_code)
    used = BooleanField(default=False)

    def generate_file(self):
        path = f"certs/{self.code}.txt"
        f = open(path, "w")
        print(self.name, self.code, file=f)
        f.close()
        return path


def init_cert():
    db.create_tables([Cert])
