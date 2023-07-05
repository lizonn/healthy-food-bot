from aiogram import types
from aiogram.filters import CommandStart

from bot.loader import dp
from bot.handlers import texts
from logic.alternative_food import AlternativeKeyFood


@dp.message()
async def echo_handler_for_alternative_food(message: types.Message) -> None:

    key = message.text

    alt_food = AlternativeKeyFood(dataset_filepath='data/food.txt',
                                  synonyms_key_words_path='data/synonyms_food.txt')

    alternative = alt_food.get_alternative(key)
    await message.answer(alternative)
