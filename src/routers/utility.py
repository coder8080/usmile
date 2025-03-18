from aiogram import Router
from aiogram.types import Message, ErrorEvent

from entities import TEXT, ADMINS, get_update_user_info, bot, log_error

router = Router()


@router.message()
async def unknown_message(message: Message):
    await message.answer(TEXT['unknown-message'])


@router.error()
async def error_handler(error: ErrorEvent):
    update = error.update
    exception = error.exception

    chat_id, username = get_update_user_info(update)

    log = f"Необработанное исключение. \
Пользователь: {username}:{chat_id}. \
Исключение: {exception}"

    try:
        await bot.send_message(chat_id, TEXT['error'])
    except Exception:
        pass

    await log_error(log)
