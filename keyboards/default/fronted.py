from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp
Fronted_dars=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Frontend (Saud Abdulwahed) πΊπΏ")
        ],
        [
            KeyboardButton(text="HTML I CSS I SASS Bootstrap & web-site πΊπΏ")
        ],
        [
            KeyboardButton(text="HTML va CSS πΊπΏ")
        ],
        [
            KeyboardButton(text="SASS (Javohir Group) πΊπΏ")
        ],
        [
            KeyboardButton(text="JavaScript (Samar Badriddinov) πΊπΏ")
        ],
        [
            KeyboardButton(text="JavaScript (Saidbek Arislonov) πΊπΏ")
        ],
        [
            KeyboardButton(text="Vue.js (Samar Badriddinov) πΊπΏ")
        ],
        [
            KeyboardButton(text="Next JS (Javohir Group) πΊπΏ")
        ],
        [
            KeyboardButton(text="Angular darslari I Toβliq kurs πΊπΏ")
        ],
        [
            KeyboardButton(text="TypeScript to'liq kurs πΊπΏ")
        ],
        [
            KeyboardButton(text="React JS amaliyot πΊπΏ")
        ],
        [
            KeyboardButton(text="π Orqaga"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="Orqaga π")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Frontend πΊπΏ</b>" , reply_markup=Fronted_dars)

@dp.message_handler(text="Frontend (Saud Abdulwahed) πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Frontend (Saud Abdulwahed) πΊπΏ</b>" , reply_markup=Saud)

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
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="HTML I CSS I SASS Bootstrap & web-site πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>HTML I CSS I SASS Bootstrap & web-site πΊπΏ</b>" , reply_markup=HTML)

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
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="HTML va CSS πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>HTML va CSS πΊπΏ</b>" , reply_markup=CSS)

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
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="SASS (Javohir Group) πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>SASS (Javohir Group) πΊπΏ</b>" , reply_markup=SASS)

SASS = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1_Dars"),
            KeyboardButton(text="2_Dars")
        ],
        [
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="JavaScript (Samar Badriddinov) πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>JavaScript (Samar Badriddinov) πΊπΏ</b>" , reply_markup=JAVA)

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
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)


@dp.message_handler(text="JavaScript (Saidbek Arislonov) πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>JavaScript (Saidbek Arislonov) πΊπΏ</b>" , reply_markup=JAva)

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
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Vue.js (Samar Badriddinov) πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Vue.js (Samar Badriddinov) πΊπΏ</b>" , reply_markup=JUe)

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
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Next JS (Javohir Group) πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Next JS (Javohir Group) πΊπΏ</b>" , reply_markup=Next)

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
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Angular darslari I Toβliq kurs πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Angular darslari I Toβliq kurs πΊπΏ</b>" , reply_markup=Angu)

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
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="TypeScript to'liq kurs πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>TypeScript to'liq kurs πΊπΏ</b>" , reply_markup=typew)

typew = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#1 Dars"),
            KeyboardButton(text="#2 Dars"),
            KeyboardButton(text="#3 Dars")
        ],


        [
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="React JS amaliyot πΊπΏ")
async def bot_start(message: types.Message):
    await message.answer(f"<b>React JS amaliyot πΊπΏ</b>" , reply_markup=React)

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
            KeyboardButton(text="Orqaga π"),
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)