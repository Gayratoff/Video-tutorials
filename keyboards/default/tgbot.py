from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp
TgBot=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telegram Bot yaratish πΊπΏ")
        ],
        [
            KeyboardButton(text="Python'da Telegram Bot πΊπΏ")
        ],
        [
            KeyboardButton(text="π Orqaga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="Ortga π")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Telegram Bot yaratish πΊπΏ</b>" , reply_markup=TgBot)


@dp.message_handler(text="Telegram Bot yaratish πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Telegram Bot yaratish πΊπΏ</b>", reply_markup=Pybt)
Pybt = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="#1_dars"), KeyboardButton(text="#2_dars")],
        [KeyboardButton(text="#3_dars"),KeyboardButton(text="#4_dars")],
        [KeyboardButton(text="#5_dars"),KeyboardButton(text="#6_dars")],
        [KeyboardButton(text="#7_dars"), KeyboardButton(text="#8_dars")],
        [KeyboardButton(text="#9_dars"), KeyboardButton(text="#10_dars")],
        [KeyboardButton(text="#11_dars"), KeyboardButton(text="#12_dars")],
        [KeyboardButton(text="#13_dars"), KeyboardButton(text="#14_dars")],
        [
            KeyboardButton(text="Ortga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
