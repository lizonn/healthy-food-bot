from unittest.mock import AsyncMock

import pytest

from bot.handlers.users.start import start_bot
from bot.handlers import texts

@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    await start_bot(message)

    message.answer.assert_called_with(texts.GREETING_TEXT)


