from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from entities import TEXT, States, admin_markup
from models import Link

router = Router()


@router.message(Command("create_link"), StateFilter(None))
@router.message(F.text == TEXT['create-link'], StateFilter(None))
async def create_link(message: Message, state: FSMContext):
    await state.set_state(States.TypingNumber)

    await message.answer(TEXT['input-count'],
                         reply_markup=ReplyKeyboardRemove())


@router.message(StateFilter(States.TypingNumber))
async def get_number(message: Message, state: FSMContext):
    if not message.text.isnumeric():
        await message.answer(TEXT['input-count'])
        return
    await state.set_state(None)
    link = await Link.aio_create(count=int(message.text))

    text = TEXT['link-created']
    text = text.replace("{%LINK%}", link.render())

    await message.answer(text, reply_markup=admin_markup(), parse_mode="html")
