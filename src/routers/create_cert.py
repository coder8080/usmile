from typing import cast

from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message, ReplyKeyboardRemove

from entities import ADMINS, TEXT, States, get_keyboard
from models import Cert, User

router = Router()


@router.message(StateFilter(None), Command("create_cert"))
@router.message(StateFilter(None), F.text == TEXT["create-cert"])
async def open_create_cert(message: Message, state: FSMContext):
    await state.set_state(States.TypingName)

    await message.answer(TEXT["input-name"], reply_markup=ReplyKeyboardRemove())


@router.message(StateFilter(States.TypingName), Command("cancel"))
async def cancel(message: Message, state: FSMContext, user: User):
    await state.set_state(None)

    await message.answer(
        TEXT["create-cert-cancelled"], reply_markup=get_keyboard(user)
    )


@router.message(StateFilter(States.TypingName))
async def create_cert(message: Message, user: User, state: FSMContext):
    if not message.text:
        raise Exception(f"Message without text {user.info()}")

    names = message.text.split("\n")

    if user.chat_id not in ADMINS and len(names) > cast(int, user.count):
        await message.answer(TEXT["not-enough-count"])
        return

    await state.set_state(None)

    await message.answer(TEXT["start-create-cert"])

    for name in names:
        cert = await Cert.aio_create(name=name)
        path = await cert.generate_file()
        await message.answer_document(FSInputFile(path))

    if user.chat_id not in ADMINS:
        user.count -= len(names)
        await user.aio_save()

    await message.answer(TEXT["certs-ready"], reply_markup=get_keyboard(user))
