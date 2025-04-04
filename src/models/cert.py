import subprocess
from datetime import datetime, timedelta
from random import randint
from typing import cast

from peewee import BooleanField, TextField

from .db import BaseModel, db


def cert_code():
    return "".join([str(randint(1, 9)) for _ in range(8)])


async def replace_in_document(
    name: str, expires: str, result_filename: str, temp_filename: str, code:str
) -> None:
    with open("src/static/certificate.svg", "r", encoding="utf-8") as file:
        svg_content = file.read()
    svg_content = svg_content.replace("fioHandler", name)
    svg_content = svg_content.replace("dateHandler", expires)
    svg_content = svg_content.replace("codeHandler", code)

    with open(temp_filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    subprocess.run(
        [
            "inkscape",
            temp_filename,
            "--export-type=pdf",
            f"--export-filename={result_filename}",
        ],
        check=True,
    )


class Cert(BaseModel):
    name = TextField()
    code = TextField(default=cert_code)
    used = BooleanField(default=False)

    async def generate_file(self):
        path = f"certs/{self.code}.pdf"
        temp_path = f"certs/{self.code}.svg"

        expire = datetime.now() + timedelta(days=365)
        expire_str = f"{expire.year}/{expire.month}/{expire.day}"

        await replace_in_document(
            cast(str, self.name), expire_str, path, temp_path, cast(str, self.code)
        )
        return path


def init_cert():
    db.create_tables([Cert])
