import os
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher
from handlers import start, comix_utils, comix


load_dotenv()


async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    dp.include_routers(start.router, comix.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())