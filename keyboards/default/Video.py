from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp,bot
video_montaj= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="3D Garfika 🇺🇿"),
            KeyboardButton(text="Video Montaj 🇺🇿")
        ],
        [
            KeyboardButton(text="Grafik Dizayn 🇺🇿"),
            KeyboardButton(text="Ui/UX Dizayn 🇺🇿")
        ],
        [
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
