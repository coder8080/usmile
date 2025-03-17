from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.redis import RedisStorage
import redis.asyncio as redis


class States(StatesGroup):
    TypingNumber = State()
    TypingName = State()
    TypingCert = State()


connection = redis.Redis(host="redis", port=6379)
storage = RedisStorage(connection)
