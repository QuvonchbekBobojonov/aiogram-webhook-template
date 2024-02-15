from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

ADMINS = env.list("ADMINS")

WEBHOOK_HOST = env.str("WEBHOOK_HOST")
WEBHOOK_PATH = f"/{BOT_TOKEN}"
WEBHOOK_URI = WEBHOOK_HOST + WEBHOOK_PATH
