from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp,bot
adobe = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Adobe After Effects 🇺🇿"),

        ],
        [
            KeyboardButton(text="Adobe Premiere Pro 🇺🇿")
        ],
        [
            KeyboardButton(text="🔙 Ortga"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]

    ],
    resize_keyboard=True
)
@dp.message_handler(text="Ortga   🔙")
async def bot_start(message:types.Message):
    await message.answer(f"<b>Mobil Dasturlash 🇺🇿</b>", reply_markup=adobe)
@dp.message_handler(text="Adobe Premiere Pro 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Adobe Premiere Pro 🇺🇿</b>" , reply_markup=Autocad)
Autocad = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="DARS   1-5"),KeyboardButton(text="DARS 6-11")],
        [
            KeyboardButton(text="Ortga   🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)