from aiogram import types, Bot


# Set bot commands
def get_commands_uz():
    commands = [
        types.BotCommand(command="/start", description="Bot-ni ishga tushurish"),
        types.BotCommand(command="/help", description="Yordam"),
    ]
    return commands


def get_commands_ru():
    commands = [
        types.BotCommand(command="/start", description="Запустить бота"),
        types.BotCommand(command="/help", description="Помощь"),
    ]
    return commands


def get_commands_en():
    commands = [
        types.BotCommand(command="/start", description="Start the bot"),
        types.BotCommand(command="/help", description="Help"),
    ]
    return commands


async def set_default_commands(bot: Bot):
    await bot.set_my_commands(get_commands_uz(), scope=types.BotCommandScopeAllPrivateChats(), language_code="uz")
    await bot.set_my_commands(get_commands_ru(), scope=types.BotCommandScopeAllPrivateChats(), language_code="ru")
    await bot.set_my_commands(get_commands_en(), scope=types.BotCommandScopeAllPrivateChats(), language_code="en")