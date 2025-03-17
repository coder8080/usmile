from aiogram import Dispatcher
from aiogram.types import Update
from typing import Callable, Dict, Any, Awaitable

from models import User
from routers import index_router
from .fsm import storage

dp = Dispatcher(storage=storage)


@dp.update.middleware
async def get_user(handler: Callable[[Update, Dict[str, Any]],
                                     Awaitable[Any]],
                   update: Update,
                   data: Dict[str, Any]):
    chat_id = -1
    username = ""
    if update.event_type == "message":
        chat_id = update.message.chat.id
        username = update.message.from_user.username
    elif update.event_type == "callback_query":
        chat_id = update.callback_query.from_user.id
        username = update.callback_query.from_user.username
    elif update.event_type == "pre_checkout_query":
        chat_id = update.pre_checkout_query.from_user.id
        username = update.pre_checkout_query.from_user.username
    else:
        return await handler(update, data)

    if not username:
        username = "unknown:" + chat_id

    query = User.select().where(User.chat_id == chat_id)
    if not await query.aio_exists():
        user = await User.aio_create(chat_id=chat_id, username=username)
        data['user'] = user
    else:
        user = await query.aio_first()
        data['user'] = user

    return await handler(update, data)

dp.include_router(index_router)
