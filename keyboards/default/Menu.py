from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

Menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="๐ง๐ปโ๐ป Dasturlash darslari"),
            KeyboardButton(text="๐ Dizayn darslari")
        ],
        [
            KeyboardButton(text="๐โโ๏ธ Frilanserlik darslari"),
            KeyboardButton(text="๐ฑSMM")
        ],
        [
            KeyboardButton(text="๐ฉ Biz bilan bog'lanish"),
            KeyboardButton(text="๐ Statistika")
        ],
        [
            KeyboardButton(text="๐จโ๐ฉโ๐งโ๐ฆ Biz haqimizda")
        ]
    ],
    resize_keyboard=True
)

tasdiq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="โ Tasdiqlash"),
            KeyboardButton(text="โ Bekor qilish")
        ]
    ],
    resize_keyboard=True
)