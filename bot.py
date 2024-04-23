import os
import asyncio
from aiogram import Bot, Dispatcher
from handlers import start, comix_utils, comix
from dotenv import load_dotenv


async def main():
    load_dotenv()
    bot_token = os.getenv("TG_BOT_TOKEN")

    if not bot_token or not chat_id:
        raise ValueError("Необходимо заполнить переменные окружения TG_BOT_TOKEN и CHAT_ID")

    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_routers(start.router, comix.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
