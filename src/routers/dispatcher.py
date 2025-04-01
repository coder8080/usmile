from typing import Any, Awaitable, Callable, Dict

from aiogram import Dispatcher
from aiogram.types import Update

from entities import get_update_user_info, storage
from models import User

from .check_cert import router as check_cert_router
from .check_count import router as check_count_router
from .create_cert import router as create_cert_router
from .index import router as index_router
from .link import router as link_router
from .utility import router as utility_router

dp = Dispatcher(storage=storage)


@dp.update.middleware
async def get_user(handler: Callable[[Update, Dict[str, Any]],
                                     Awaitable[Any]],
                   update: Update,
                   data: Dict[str, Any]):
    chat_id, username = get_update_user_info(update)
    if chat_id == 0:
        return await handler(update, data)

    if not username:
        username = "unknown:" + str(chat_id)

    query = User.select().where(User.chat_id == chat_id)
    if not await query.aio_exists():
        user = await User.aio_create(chat_id=chat_id, username=username)
        data['user'] = user
    else:
        user = await query.aio_first()
        data['user'] = user

    return await handler(update, data)

dp.include_router(index_router)
dp.include_router(link_router)
dp.include_router(create_cert_router)
dp.include_router(check_cert_router)
dp.include_router(check_count_router)
dp.include_router(utility_router)
