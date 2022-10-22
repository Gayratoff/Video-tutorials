from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
Oop=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="DARS 1-5"),
            KeyboardButton(text="DARS 6-10")
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)