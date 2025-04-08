from os import getenv

from aiohttp import web


async def podname(request: web.Request):
    POD_NAME = getenv("POD_NAME")
    assert POD_NAME
    return web.json_response({"podname": POD_NAME})


async def start_site():
    app = web.Application()
    app.router.add_get("/podname", podname)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=3000)
    await site.start()


__all__ = ["start_site"]
