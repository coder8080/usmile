import asyncio

from entities import bot
from routers import dp


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
