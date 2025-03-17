from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from entities import ADMINS, TEXT, States, get_keyboard
from models import Cert, User

router = Router()


@router.message(StateFilter(None), Command("check"), F.chat.id.in_(ADMINS))
@router.message(StateFilter(None), F.text == TEXT['check-cert'],
                F.chat.id.in_(ADMINS))
async def check_start(message: Message, state: FSMContext):
    await state.set_state(States.TypingCert)
    await message.answer(TEXT['input-cert'],
                         reply_markup=ReplyKeyboardRemove())


@router.message(StateFilter(States.TypingCert))
async def check_cert(message: Message, state: FSMContext, user: User):
    await state.set_state(None)

    markup = get_keyboard(user)
    query = Cert.select().where(Cert.code == message.text.strip())

    if not await query.aio_exists():
        await message.answer(TEXT['no-cert'], reply_markup=markup)
        return

    cert = await query.aio_first()

    if cert.used:
        await message.answer(TEXT['used-cert'], reply_markup=markup)
        return

    text = TEXT['ok-cert']
    text = text.replace("{%NAME%}", cert.name)

    await message.answer(text, reply_markup=markup)
