from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.loader import dp
from bot.handlers import texts


# @dp.message_handler(CommandStart(),state='*')
# async def start_bot(message: types.Message,state):
#
#
#     await state.reset_state(with_data=False)
#
#     await message.answer(texts.GREETING_TEXT)


@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):


    await message.answer(texts.GREETING_TEXT)
