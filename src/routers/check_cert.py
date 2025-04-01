from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder

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


@router.message(StateFilter(States.TypingCert), Command("cancel"))
async def cancel(message: Message, state: FSMContext, user: User):
    await state.set_state(None)
    await message.answer(TEXT['check-cert-cancelled'],
                         reply_markup=get_keyboard(user))


@router.message(StateFilter(States.TypingCert), F.chat.id.in_(ADMINS))
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

    builder = InlineKeyboardBuilder()
    builder.button(text="Да", callback_data=f"used|{cert.code}")
    builder.button(text="Нет", callback_data="unused")
    builder.adjust(2)

    await message.answer(TEXT['input-used'], reply_markup=builder.as_markup())


@router.callback_query(F.data.regexp("used\\|\\d+"),
                       F.from_user.id.in_(ADMINS))
async def cert_used(query: CallbackQuery):
    await query.answer()
    await query.message.edit_reply_markup(reply_markup=None)

    _, code = query.data.split("|")
    cert: Cert = await Cert.aio_get(Cert.code == code)
    cert.used = True
    await cert.aio_save()

    await query.message.edit_text(TEXT['ok-used'])


@router.callback_query(F.data == "unused", F.from_user.id.in_(ADMINS))
async def cert_unused(query: CallbackQuery):
    await query.answer()
    await query.message.edit_reply_markup(reply_markup=None)

    await query.message.edit_text(TEXT['ok-unused'])
