from random import randint

from peewee import TextField

from .db import db, BaseModel


def cert_code():
    return ''.join([str(randint(1, 9)) for _ in range(8)])


class Cert(BaseModel):
    name = TextField()
    code = TextField(default=cert_code)

    def generate_file(self):
        path = f"certs/{self.code}.txt"
        f = open(path, "w")
        print(self.name, file=f)
        f.close()
        return path


def init_cert():
    db.create_tables([Cert])
