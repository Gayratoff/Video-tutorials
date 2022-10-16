from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp
Fronted_dars=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Frontend (Saud Abdulwahed) 🇺🇿")
        ],
        [
            KeyboardButton(text="HTML I CSS I SASS Bootstrap & web-site 🇺🇿")
        ],
        [
            KeyboardButton(text="HTML va CSS 🇺🇿")
        ],
        [
            KeyboardButton(text="SASS (Javohir Group) 🇺🇿")
        ],
        [
            KeyboardButton(text="JavaScript (Samar Badriddinov) 🇺🇿")
        ],
        [
            KeyboardButton(text="JavaScript (Saidbek Arislonov) 🇺🇿")
        ],
        [
            KeyboardButton(text="Vue.js (Samar Badriddinov) 🇺🇿")
        ],
        [
            KeyboardButton(text="Next JS (Javohir Group) 🇺🇿")
        ],
        [
            KeyboardButton(text="Angular darslari I To’liq kurs 🇺🇿")
        ],
        [
            KeyboardButton(text="TypeScript to'liq kurs 🇺🇿")
        ],
        [
            KeyboardButton(text="React JS amaliyot 🇺🇿")
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="Orqaga 🔙")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Frontend 🇺🇿</b>" , reply_markup=Fronted_dars)

@dp.message_handler(text="Frontend (Saud Abdulwahed) 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Frontend (Saud Abdulwahed) 🇺🇿</b>" , reply_markup=Saud)

Saud = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dars #1"),
            KeyboardButton(text="Dars #2"),
        ],
        [
            KeyboardButton(text="Dars #3"),
            KeyboardButton(text="Dars #4"),
        ],
        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="HTML I CSS I SASS Bootstrap & web-site 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>HTML I CSS I SASS Bootstrap & web-site 🇺🇿</b>" , reply_markup=HTML)

HTML = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-Dars"),
            KeyboardButton(text="2-Dars"),
            KeyboardButton(text="3-Dars")
        ],
        [
            KeyboardButton(text="4-Dars"),
            KeyboardButton(text="5-Dars"),
            KeyboardButton(text="6-Dars")
        ],
        [
            KeyboardButton(text="7-Dars"),
            KeyboardButton(text="8-Dars"),
            KeyboardButton(text="9-Dars")
        ],
        [
            KeyboardButton(text="10-Dars"),
            KeyboardButton(text="11-Dars")
        ],
        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="HTML va CSS 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>HTML va CSS 🇺🇿</b>" , reply_markup=CSS)

CSS = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 Dars"),
            KeyboardButton(text="2 Dars"),
            KeyboardButton(text="3 Dars")
        ],
        [
            KeyboardButton(text="4 Dars"),
            KeyboardButton(text="5 Dars"),
            KeyboardButton(text="6 Dars")
        ],
        [
            KeyboardButton(text="7 Dars"),
            KeyboardButton(text="8 Dars")
        ],

        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="SASS (Javohir Group) 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>SASS (Javohir Group) 🇺🇿</b>" , reply_markup=SASS)

SASS = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1_Dars"),
            KeyboardButton(text="2_Dars")
        ],
        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="JavaScript (Samar Badriddinov) 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>JavaScript (Samar Badriddinov) 🇺🇿</b>" , reply_markup=JAVA)

JAVA = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-dars"),
            KeyboardButton(text="2-dars"),
            KeyboardButton(text="3-dars")
        ],
        [
            KeyboardButton(text="4-dars"),
            KeyboardButton(text="5-dars"),
            KeyboardButton(text="6-dars")
        ],
        [
            KeyboardButton(text="7-dars"),
            KeyboardButton(text="8-dars"),
            KeyboardButton(text="9-dars")
        ],
        [
            KeyboardButton(text="10-dars"),
            KeyboardButton(text="11-dars")
        ],
        [
            KeyboardButton(text="12-dars"),
            KeyboardButton(text="13-dars"),
            KeyboardButton(text="14-dars")
        ],
        [
            KeyboardButton(text="15-dars"),
            KeyboardButton(text="16-dars"),
            KeyboardButton(text="17-dars")
        ],
        [
            KeyboardButton(text="18-dars"),
            KeyboardButton(text="19-dars"),
            KeyboardButton(text="20-dars")
        ],
        [
            KeyboardButton(text="21-dars"),
            KeyboardButton(text="22-dars"),
            KeyboardButton(text="23-dars")
        ],
        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)


@dp.message_handler(text="JavaScript (Saidbek Arislonov) 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>JavaScript (Saidbek Arislonov) 🇺🇿</b>" , reply_markup=JAva)

JAva = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1_dars"),
            KeyboardButton(text="2_dars"),
        ],
        [
            KeyboardButton(text="3_dars"),
            KeyboardButton(text="4_dars"),
            KeyboardButton(text="5_dars")
        ],
        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Vue.js (Samar Badriddinov) 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Vue.js (Samar Badriddinov) 🇺🇿</b>" , reply_markup=JUe)

JUe = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 dars"),
            KeyboardButton(text="2 dars"),
            KeyboardButton(text="3 dars")
        ],
        [
            KeyboardButton(text="4 dars"),
            KeyboardButton(text="5 dars"),
            KeyboardButton(text="6 dars")
        ],
        [
            KeyboardButton(text="7 dars"),
            KeyboardButton(text="8 dars"),
            KeyboardButton(text="9 dars")
        ],
        [
            KeyboardButton(text="10 dars"),
            KeyboardButton(text="11 dars"),
            KeyboardButton(text="12 dars")
        ],
        [
            KeyboardButton(text="13 dars"),
            KeyboardButton(text="14 dars")
        ],
        [
            KeyboardButton(text="15 dars"),
            KeyboardButton(text="16 dars")
        ],
        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Next JS (Javohir Group) 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Next JS (Javohir Group) 🇺🇿</b>" , reply_markup=Next)

Next = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dars_#1"),
            KeyboardButton(text="Dars_#2"),
            KeyboardButton(text="Dars_#3")
        ],
        [
            KeyboardButton(text="Dars_#4"),
            KeyboardButton(text="Dars_#5"),
            KeyboardButton(text="Dars_#6")
        ],
        [
            KeyboardButton(text="Dars_#7"),
            KeyboardButton(text="Dars_#8"),
            KeyboardButton(text="Dars_#9")
        ],
        [
            KeyboardButton(text="Dars_#10"),
            KeyboardButton(text="Dars_#11")
        ],
        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Angular darslari I To’liq kurs 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Angular darslari I To’liq kurs 🇺🇿</b>" , reply_markup=Angu)

Angu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#1-Dars"),
            KeyboardButton(text="#2-Dars"),
            KeyboardButton(text="#3-Dars")
        ],
        [
            KeyboardButton(text="#4-Dars"),
            KeyboardButton(text="#5-Dars"),
            KeyboardButton(text="#6-Dars")
        ],

        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="TypeScript to'liq kurs 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>TypeScript to'liq kurs 🇺🇿</b>" , reply_markup=typew)

typew = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#1 Dars"),
            KeyboardButton(text="#2 Dars"),
            KeyboardButton(text="#3 Dars")
        ],


        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="React JS amaliyot 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>React JS amaliyot 🇺🇿</b>" , reply_markup=React)

React = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#1-dars"),
            KeyboardButton(text="#2-dars"),
            KeyboardButton(text="#3-dars")
        ],
        [
            KeyboardButton(text="#4-dars"),
            KeyboardButton(text="#5-dars"),
            KeyboardButton(text="#6-dars")
        ],
        [
            KeyboardButton(text="#7-dars"),
            KeyboardButton(text="#8-dars"),
            KeyboardButton(text="#9-dars")
        ],
        [
            KeyboardButton(text="#10-dars"),
            KeyboardButton(text="#11-dars")
        ],
        [
            KeyboardButton(text="Orqaga 🔙"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)