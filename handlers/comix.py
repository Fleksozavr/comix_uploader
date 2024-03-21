import os
from dotenv import load_dotenv
from handlers import comix_utils
from .comix_utils import Image
from aiogram import Router, F, types, Bot
from aiogram.filters import Command
from aiogram.types import Message


load_dotenv()

router = Router()


@router.message(Command("comix"))
async def send_comix(message: types.Message):
    bot = Bot(os.getenv("BOT_TOKEN"))
    channel_id = str(os.getenv("CHAT_ID"))
    image = Image()
    image_url = image.download_comix()
    author_text = image.get_author_comment()

    if image_url:
        await bot.send_photo(chat_id=channel_id, photo=image_url, caption=author_text)
    else:
        await message.answer("Ошибка при загрузке комикса.")