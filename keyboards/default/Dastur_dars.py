from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

dasturlash =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Frontend 🇺🇿"),
            KeyboardButton(text="Backend 🇺🇿")
        ],
        [
            KeyboardButton(text="Telegram-Bot 🇺🇿"),
            KeyboardButton(text="Web Dasturlash 🇺🇿")
        ],
        [
            KeyboardButton(text="Mobil Dasturlash 🇺🇿"),
            KeyboardButton(text="Sun'iy intellekt 🇺🇿")
        ],
        [
            KeyboardButton(text="OOP dasturlash 🇺🇿"),
            KeyboardButton(text="1C dasturlash 🇺🇿")
        ],
        [
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)