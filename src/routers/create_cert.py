from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from entities import States, TEXT, ADMINS, get_keyboard
from models import User, Cert

router = Router()


@router.message(StateFilter(None), Command("create_cert"))
@router.message(StateFilter(None), F.text == TEXT['create-cert'])
async def open_create_cert(message: Message, state: FSMContext):
    await state.set_state(States.TypingName)

    await message.answer(TEXT['input-name'],
                         reply_markup=ReplyKeyboardRemove())


@router.message(StateFilter(States.TypingName), Command("cancel"))
async def cancel(message: Message, state: FSMContext, user: User):
    await state.set_state(None)

    await message.answer(TEXT['create-cert-cancelled'],
                         reply_markup=get_keyboard(user))


@router.message(StateFilter(States.TypingName))
async def create_cert(message: Message, user: User, state: FSMContext):
    names = message.text.split("\n")

    if user.chat_id not in ADMINS and len(names) > user.count:
        await message.answer(TEXT['not-enough-count'])
        return

    await state.set_state(None)

    for name in names:
        cert = await Cert.aio_create(name=name)
        path = cert.generate_file()
        await message.answer_document(FSInputFile(path))

    if user.chat_id not in ADMINS:
        user.count -= len(names)
        await user.aio_save()

    await message.answer(TEXT['certs-ready'],
                         reply_markup=get_keyboard(user))
