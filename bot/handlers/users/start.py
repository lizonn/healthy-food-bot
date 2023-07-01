from aiogram import types
from aiogram.filters import CommandStart

from bot.loader import dp
from bot.handlers import texts


@dp.message(CommandStart())
async def start_bot_with_state(message: types.Message, state):
    await state.clear()

    await message.answer(texts.GREETING_TEXT)
