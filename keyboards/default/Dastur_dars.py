from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

dasturlash =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Frontend πΊπΏ"),
            KeyboardButton(text="Backend πΊπΏ")
        ],
        [
            KeyboardButton(text="Telegram-Bot πΊπΏ"),
            KeyboardButton(text="Web Dasturlash πΊπΏ")
        ],
        [
            KeyboardButton(text="Mobil Dasturlash πΊπΏ"),
            KeyboardButton(text="Sun'iy intellekt πΊπΏ")
        ],
        [
            KeyboardButton(text="OOP dasturlash πΊπΏ"),
            KeyboardButton(text="1C dasturlash πΊπΏ")
        ],
        [
            KeyboardButton(text="π Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)