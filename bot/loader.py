from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from bot import config

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


