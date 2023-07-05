import asyncio
import logging

from bot.handlers import dp
from bot.loader import bot

from aiogram.types import (BotCommand,
                           BotCommandScopeAllPrivateChats)



async def start_bot(dp):
    # user_commands = [
    #     BotCommand('help', 'инструкция')
    # ]

    async def startup(dp):
        # await bot.set_my_commands(
        #     commands=user_commands,
        #     scope=BotCommandScopeAllPrivateChats())
        pass

    # dp.start_polling(dp, on_startup=startup)
    await dp.start_polling(bot, on_startup=startup)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # await start_bot(dp)
    asyncio.run(start_bot(dp))