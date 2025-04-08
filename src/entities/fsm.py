import redis.asyncio as redis
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage

from .constants import REDIS_HOST


class States(StatesGroup):
    TypingNumber = State()
    TypingName = State()
    TypingCert = State()


assert REDIS_HOST
connection = redis.Redis(host=REDIS_HOST, port=6379)
storage = RedisStorage(connection)
