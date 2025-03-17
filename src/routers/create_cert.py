from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from entities import States, TEXT

router = Router()


@router.message(Command("create_cert"))
async def open_create_cert(message: Message, state: FSMContext):
    await message.answer(TEXT[''])
    await state.set_state(States.TypingName)
