from aiogram import types
from aiohttp import web
from fastapi import Request, FastAPI, HTTPException

from core.config import WEBHOOK_PATH, WEBHOOK_URI, BOT_TOKEN
from core.loader import bot, dp

import handlers
from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands

app = FastAPI()


async def set_webhook():
    await bot.set_webhook(WEBHOOK_URI)


async def handle_webhook(request: Request):
    url = str(request.url)
    index = url.rfind('/')
    token = url[index + 1:]

    if token == BOT_TOKEN:
        update = types.Update(**await request.json())
        await dp.feed_webhook_update(bot, update)
        return web.Response()
    else:
        raise HTTPException(status_code=403, detail="Forbidden")


async def on_startup():
    await set_webhook()
    await set_default_commands(bot)
    await on_startup_notify(bot)


async def on_shutdown():
    await on_shutdown_notify(bot)


if __name__ == "__main__":
    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)

    @app.post(WEBHOOK_PATH)
    async def webhook_endpoint(request: Request):
        return await handle_webhook(request)

    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
