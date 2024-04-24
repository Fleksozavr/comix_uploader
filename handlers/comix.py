import os
from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types.input_file import InputFile
from handlers.comix_utils import router, get_random_num, download_comix, get_author_comment
from dotenv import load_dotenv


@router.message(F.text == "/comix")
async def send_comix(message: Message):
    chat_id = os.environ("CHAT_ID")
    random_num = get_random_num()
    image_url, author_text = download_comix(random_num)
    if image_url:
        await message.bot.send_photo(chat_id=chat_id, photo=image_url, caption=author_text)
    else:
        await message.answer("Ошибка при загрузке комикса.")
