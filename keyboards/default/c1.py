from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
C1=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-Modul"),
            KeyboardButton(text="2-Modul")
        ],
        [
            KeyboardButton(text="3-Modul"),
            KeyboardButton(text="4-Modul")
        ],
        [
            KeyboardButton(text="5-Modul"),
            KeyboardButton(text="6-Modul")
        ],
        [
            KeyboardButton(text="7-Modul")
        ],
        [
            KeyboardButton(text="🔙 Orqaga"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)