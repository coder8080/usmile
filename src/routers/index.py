from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from entities import TEXT, ADMINS
from models import Link, User

router = Router()


@router.message(CommandStart())
async def start(message: Message, user: User):
    if user.chat_id in ADMINS:
        await message.answer(text=TEXT['admin-start'])
        return

    arr = message.text.split()

    if len(arr) != 2:
        text = TEXT['simple-user-start']
        text = text.replace("{%ID%}", str(user.chat_id))
        await message.answer(text=text, parse_mode="html")
        return

    code = arr[1]
    query = Link.select().where(Link.code == code)

    if not await query.aio_exists():
        await message.answer(text=TEXT['wrong-link'])
        return

    link: Link = await query.aio_first()

    if link.used:
        await message.answer(text=TEXT['used-link'])
        return

    user.count += link.count
    await user.aio_save()

    link.used = True
    await link.aio_save()

    text = TEXT['ok-link']
    text = text.replace("{%COUNT%}", user.count)

    await message.answer(tex=text)
