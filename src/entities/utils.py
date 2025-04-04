import subprocess

from aiogram.types import ReplyKeyboardMarkup, Update
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from entities import ADMINS, TEXT
from models import User

from .create_bot import bot
from .logs import logger


def admin_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=TEXT["create-link"])
    builder.button(text=TEXT["create-cert"])
    builder.button(text=TEXT["check-cert"])
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def user_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=TEXT["create-cert"])
    builder.button(text=TEXT["check-count"])
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def get_keyboard(user: User):
    if user.chat_id in ADMINS:
        return admin_markup()
    return user_markup()


def get_update_user_info(update: Update):
    chat_id = 0
    username = ""
    if update.message and update.message.from_user:
        chat_id = update.message.chat.id
        username = update.message.from_user.username
    elif update.callback_query:
        chat_id = update.callback_query.from_user.id
        username = update.callback_query.from_user.username
    elif update.pre_checkout_query:
        chat_id = update.pre_checkout_query.from_user.id
        username = update.pre_checkout_query.from_user.username

    if username is None:
        username = f"unknown:${chat_id}"

    return chat_id, username


async def log_error(message: str):
    logger.error(message)
    for admin_chat_id in ADMINS:
        await bot.send_message(chat_id=admin_chat_id, text=message)


def replaceInDocument(FIO: str, dateTill: str, pdfFileName: str) -> None:
    with open("src/static/certificate.svg", "r", encoding="utf-8") as file:
        svg_content = file.read()
    svg_content = svg_content.replace("fioHandler", FIO)
    svg_content = svg_content.replace("dateHandler", dateTill)

    temp_svg_path = "temp_certificate.svg"
    with open(temp_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    subprocess.run(
        [
            "inkscape",
            temp_svg_path,
            "--export-type=pdf",
            f"--export-filename={pdfFileName}",
        ],
        check=True,
    )

    logger.info(f"PDF успешно создан: {pdfFileName}")
