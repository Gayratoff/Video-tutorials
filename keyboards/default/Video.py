from aiogram import types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from loader import dp,bot
video_montaj= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="3D Garfika πΊπΏ"),
            KeyboardButton(text="Video Montaj πΊπΏ")
        ],
        [
            KeyboardButton(text="Grafik Dizayn πΊπΏ"),
            KeyboardButton(text="Ui/UX Dizayn πΊπΏ")
        ],
        [
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)
