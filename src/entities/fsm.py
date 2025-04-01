import redis.asyncio as redis
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage


class States(StatesGroup):
    TypingNumber = State()
    TypingName = State()
    TypingCert = State()


connection = redis.Redis(host="redis", port=6379)
storage = RedisStorage(connection)
