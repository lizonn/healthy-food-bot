from aiogram import Bot, Dispatcher, types,Router
from aiogram.fsm.storage.memory import MemoryStorage

from bot import config

router = Router()

bot = Bot(token=config.API_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(router)