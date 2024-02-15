from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode

from core.config import BOT_TOKEN

dp = Dispatcher()
bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
