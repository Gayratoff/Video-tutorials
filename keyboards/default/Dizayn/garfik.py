from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

Grf = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Adobe Photoshop (Asror Iskandarov) 🇺🇿"),
        ],
        [
            KeyboardButton(text="Adobe Illustrator (Madina Mavlonova) 🇺🇿"),

        ],
        [
            KeyboardButton(text="Adobe Illustrator 🇺🇿"),
            KeyboardButton(text="Mockup dizayn kursi 🇺🇿")
        ],
        [
            KeyboardButton(text="🔙 Ortga"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]

    ],
    resize_keyboard=True
)