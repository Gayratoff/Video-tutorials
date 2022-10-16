from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("<b>Buyruqlar:</b> ",
            "/start - Botni ishga tushirish",
            "/manba - manbalar bo'yicha malumotlar",
            "/admin - Loyiha asoschisi",
            "/help - Yordam",)
    
    await message.answer("\n".join(text))

