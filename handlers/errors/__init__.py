import logging
from aiogram.types import ErrorEvent

from core.loader import dp, bot
from core.config import ADMINS


@dp.error()
async def error_handler(event: ErrorEvent):
    logging.error("Critical error caused by %s", event.exception,)
    for admin in ADMINS:
        await bot.send_message(
            chat_id=admin,
            text="Critical error caused by: {}".format(event.exception)
        )


