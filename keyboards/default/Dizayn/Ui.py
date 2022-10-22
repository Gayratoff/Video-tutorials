from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

UX = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Figma 🇺🇿"),
        ],
        [
            KeyboardButton(text="🔙 Ortga"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]

    ],
    resize_keyboard=True
)