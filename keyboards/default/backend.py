from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp
Backend_dars=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python ðºð¿"),
            KeyboardButton(text="C++ ðºð¿")
        ],
        [
            KeyboardButton(text="Java ðºð¿"),
            KeyboardButton(text="PHP ðºð¿")
        ],
        [
            KeyboardButton(text="ð Orqaga"),
            KeyboardButton(text="ð Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="ðOrqaga")
async def bot_start(message: types.Message):
    await message.answer(f"<b>ð Orqaga</b>" , reply_markup=Backend_dars)

@dp.message_handler(text="Python ðºð¿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Python ðºð¿</b>" , reply_markup=py)

py = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1,Dars"),
            KeyboardButton(text="2,Dars"),
            KeyboardButton(text="3,Dars")
        ],
        [
            KeyboardButton(text="4,Dars"),
            KeyboardButton(text="5,Dars"),
            KeyboardButton(text="6,Dars")
        ],
        [
            KeyboardButton(text="7,Dars"),
            KeyboardButton(text="8,Dars"),
            KeyboardButton(text="9,Dars")
        ],
        [
            KeyboardButton(text="10,Dars"),
            KeyboardButton(text="11,Dars"),
            KeyboardButton(text="12,Dars")
        ],
        [
            KeyboardButton(text="13,Dars"),
            KeyboardButton(text="14,Dars"),
            KeyboardButton(text="15,Dars")
        ],
        [
            KeyboardButton(text="ðOrqaga"),
            KeyboardButton(text="ð Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="C++ ðºð¿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>C++ ðºð¿</b>" , reply_markup=cp)

cp = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1,dars"),
            KeyboardButton(text="2,dars"),
            KeyboardButton(text="3,dars")
        ],
        [
            KeyboardButton(text="4,dars"),
            KeyboardButton(text="5,dars"),
            KeyboardButton(text="6,dars")
        ],
        [
            KeyboardButton(text="7,dars"),
            KeyboardButton(text="8,dars"),
            KeyboardButton(text="9,dars")
        ],
        [
            KeyboardButton(text="10,dars"),
            KeyboardButton(text="11,dars"),
            KeyboardButton(text="12,dars")
        ],
        [
            KeyboardButton(text="13,dars"),
            KeyboardButton(text="14,dars"),
            KeyboardButton(text="15,dars")
        ],
        [
            KeyboardButton(text="16,dars"),
            KeyboardButton(text="17,dars"),
            KeyboardButton(text="18,dars")
        ],
        [
            KeyboardButton(text="19,dars"),
            KeyboardButton(text="20,dars"),
            KeyboardButton(text="21,dars")
        ],
        [
            KeyboardButton(text="22,dars"),
            KeyboardButton(text="23,dars"),
            KeyboardButton(text="24,dars")
        ],
        [
            KeyboardButton(text="25,dars"),
            KeyboardButton(text="26,dars"),
            KeyboardButton(text="27,dars")
        ],
        [
            KeyboardButton(text="28,dars"),
        ],
        [
            KeyboardButton(text="ðOrqaga"),
            KeyboardButton(text="ð Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Java ðºð¿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Java ðºð¿</b>" , reply_markup=java)

java = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1.Dars"),
            KeyboardButton(text="2.Dars"),
            KeyboardButton(text="3.Dars")
        ],
        [
            KeyboardButton(text="4.Dars"),
            KeyboardButton(text="5.Dars"),
            KeyboardButton(text="6.Dars")
        ],
        [
            KeyboardButton(text="7.Dars"),
            KeyboardButton(text="8.Dars"),
            KeyboardButton(text="9.Dars")
        ],
        [
            KeyboardButton(text="10.Dars"),
            KeyboardButton(text="11.Dars"),
            KeyboardButton(text="12.Dars")
        ],

        [
            KeyboardButton(text="ðOrqaga"),
            KeyboardButton(text="ð Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="PHP ðºð¿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>PHP ðºð¿</b>" , reply_markup=Php)

Php = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1,Modul"),
            KeyboardButton(text="2,Modul")
        ],
        [
            KeyboardButton(text="ðOrqaga"),
            KeyboardButton(text="ð Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="1,Modul")
async def bot_start(message: types.Message):
    await message.answer(f"<b>PHP ðºð¿</b>" , reply_markup=modl)
modl = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dars 1-5"),
            KeyboardButton(text="Dars 6-10"),
            KeyboardButton(text="Dars 11-15")
        ],
        [
            KeyboardButton(text="Dars 16-20"),
            KeyboardButton(text="Dars 21-25"),
            KeyboardButton(text="Dars 26-30")
        ],
        [
            KeyboardButton(text="ðOrqaga"),
            KeyboardButton(text="ð Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

# @dp.message_handler(text="2,Modul")
# async def bot_start(message: types.Message):
#     await message.answer(f"<b>Bu Bolimda 6ta dars mavjudðð»ðð»ðð»</b>")