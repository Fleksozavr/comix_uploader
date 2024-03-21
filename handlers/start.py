from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который отправляет комиксы XKCD в канал. Просто напиши мне /comix.")