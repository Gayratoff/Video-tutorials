from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp
Web=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Django πΊπΏ"),
            KeyboardButton(text="WordPress πΊπΏ")
        ],
        [
            KeyboardButton(text="Web-site yaratish πΊπΏ")
        ],
        [
            KeyboardButton(text="π Orqaga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="π  Ortga")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Web Dasturlash πΊπΏ</b>" , reply_markup=Web)

@dp.message_handler(text="Django πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Django πΊπΏ</b>" , reply_markup=dj)
dj=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="dars 1-5"),
            KeyboardButton(text="dars 6-10")
        ],
        [
            KeyboardButton(text="π  Ortga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="WordPress πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>WordPress πΊπΏ</b>" , reply_markup=word)
word=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dars 1-3"),
            KeyboardButton(text="Dars 4-7")
        ],
        [
            KeyboardButton(text="π  Ortga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)


