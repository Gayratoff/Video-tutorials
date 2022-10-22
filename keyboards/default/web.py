from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp
Web=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Django 🇺🇿"),
            KeyboardButton(text="WordPress 🇺🇿")
        ],
        [
            KeyboardButton(text="Web-site yaratish 🇺🇿")
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="🔙  Ortga")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Web Dasturlash 🇺🇿</b>" , reply_markup=Web)

@dp.message_handler(text="Django 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Django 🇺🇿</b>" , reply_markup=dj)
dj=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="dars 1-5"),
            KeyboardButton(text="dars 6-10")
        ],
        [
            KeyboardButton(text="🔙  Ortga"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="WordPress 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>WordPress 🇺🇿</b>" , reply_markup=word)
word=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dars 1-3"),
            KeyboardButton(text="Dars 4-7")
        ],
        [
            KeyboardButton(text="🔙  Ortga"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)


