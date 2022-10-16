from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

Smm = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 - Modul"),
            KeyboardButton(text="2 - Modul")
        ],
        [
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)

