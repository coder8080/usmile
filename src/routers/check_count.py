from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.types import Message

from entities import TEXT, ADMINS
from models import User

router = Router()


@router.message(StateFilter(None), Command("check_count"))
@router.message(StateFilter(None), F.text == TEXT['check-count'])
async def check_count(message: Message, user: User):
    if user.chat_id in ADMINS:
        await message.answer(TEXT['admin-count'])
        return
    text = TEXT['user-count']
    text = text.replace("{%COUNT%}", str(user.count))

    await message.answer(text)
