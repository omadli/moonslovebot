import sys
import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from utils.data import API_TOKEN


def include_all_routers(dp: Dispatcher):
    from handlers.moonslove import router as moonslove_router
    from handlers.advanced import router as advanced_router
    dp.include_router(moonslove_router)
    dp.include_router(advanced_router)
    
    
async def main():
    # Initialize bot, dispatcher and dispatcher storage
    bot = Bot(token=API_TOKEN, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # include routers
    include_all_routers(dp)
    
    # start polling
    await dp.start_polling(
        bot,
        skip_updates=True
    )

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    