import asyncio

from entities.bot import bot
from entities.dispatcher import dp


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
