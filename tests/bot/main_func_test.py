

API_TOKEN = "6212906570:AAHfDp8CDmtt3eELJ1P4SjnTr3lkc5bIKJk"




from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext

# Please, keep your bot tokens on environments, this code only example
bot = Bot(API_TOKEN)
dp = Dispatcher()


@dp.message()
async def echo(message: types.Message, state: FSMContext) -> None:
    await message.answer(message.text)


if __name__ == '__main__':
    dp.run_polling(bot)






import pytest


from aiogram_tests import MockedBot
from aiogram_tests.handler import MessageHandler
from aiogram_tests.types.dataset import MESSAGE


@pytest.mark.asyncio
async def test_echo():
    request = MockedBot(MessageHandler(echo))
    calls = await request.query(message=MESSAGE.as_object(text="Hello, Bot!"))
    answer_message = calls.send_messsage.fetchone()
    assert answer_message.text == "Hello, Bot!"



# @pytest.mark.asyncio
# async def test_echo():
#     request = MockedBot(MessageHandler(start_bot))
#     calls = await request.query(message=MESSAGE.as_object(text="Hello, Bot!"))
#     answer_message = calls.send_messsage.fetchone()
#     assert answer_message.text == "Hello, Bot!"
