from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp,bot
adobe = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Adobe After Effects πΊπΏ"),

        ],
        [
            KeyboardButton(text="Adobe Premiere Pro πΊπΏ")
        ],
        [
            KeyboardButton(text="π Ortga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]

    ],
    resize_keyboard=True
)
@dp.message_handler(text="Ortga   π")
async def bot_start(message:types.Message):
    await message.answer(f"<b>Mobil Dasturlash πΊπΏ</b>", reply_markup=adobe)
@dp.message_handler(text="Adobe Premiere Pro πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Adobe Premiere Pro πΊπΏ</b>" , reply_markup=Autocad)
Autocad = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="DARS   1-5"),KeyboardButton(text="DARS 6-11")],
        [
            KeyboardButton(text="Ortga   π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)