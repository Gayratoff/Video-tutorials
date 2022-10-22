from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

admin_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Foydalanuvchilarga xabar yuborish")

        ],
        [
            KeyboardButton(text="👤 Foydalanuvchiga xabar yuborish")
        ],
        [
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)