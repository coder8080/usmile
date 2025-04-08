import asyncio
from os import getenv

from aiohttp import ClientSession

from entities import bot
from routers import dp
from server import start_site


async def main():
    LOCAL = bool(getenv("LOCAL"))

    if not LOCAL:
        await start_site()

        POD_NAME = getenv("POD_NAME")
        assert POD_NAME

        session = ClientSession()

        print("⏱️ Waiting to become main pod...")

        while True:
            try:
                response = await session.get("http://main-podname/podname")
                json = await response.json()
                assert json["podname"] == POD_NAME
                break
            except Exception as e:
                print(e)
                await asyncio.sleep(0.05)

        print("✅ Pod has become main. Starting polling")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
