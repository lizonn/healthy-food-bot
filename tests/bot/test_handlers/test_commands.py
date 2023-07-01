from unittest.mock import AsyncMock

import pytest
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from bot.handlers.users.start import start_bot_with_state
from bot.handlers import texts
from tests.bot.utils import TEST_USER, TEST_USER_CHAT
from tests.bot.conftest import bot, storage, event_loop


@pytest.mark.asyncio
async def test_start_handler_with_state(storage, bot):
    message = AsyncMock()

    state = FSMContext(
        bot=bot,
        storage=storage,
        key=StorageKey(bot_id=bot.id, user_id=TEST_USER.id, chat_id=TEST_USER_CHAT.id)
    )

    await start_bot_with_state(message=message, state=state)

    assert await state.get_state() is None  # проверяем сохранился ли стейт

    message.answer.assert_called_with(texts.GREETING_TEXT)
