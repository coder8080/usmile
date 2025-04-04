from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.types.base import TelegramObject
from aiogram.types.callback_query import CallbackQuery
from aiogram.types.pre_checkout_query import PreCheckoutQuery
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


def get_update_user_info(update: TelegramObject):
    chat_id = 0
    username = ""
    if (
        isinstance(update, Message) or isinstance(update, PreCheckoutQuery)
    ) and update.from_user:
        chat_id = update.from_user.id
        username = update.from_user.username
    elif isinstance(update, CallbackQuery):
        chat_id = update.from_user.id
        username = update.from_user.username

    if username is None:
        username = f"unknown:${chat_id}"

    return chat_id, username


async def log_error(message: str):
    logger.error(message)
    for admin_chat_id in ADMINS:
        await bot.send_message(chat_id=admin_chat_id, text=message)
