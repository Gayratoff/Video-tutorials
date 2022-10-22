from aiogram.types import ReplyKeyboardMarkup , KeyboardButton

Menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧑🏻‍💻 Dasturlash darslari"),
            KeyboardButton(text="🏞 Dizayn darslari")
        ],
        [
            KeyboardButton(text="🏄‍♂️ Frilanserlik darslari"),
            KeyboardButton(text="📱SMM")
        ],
        [
            KeyboardButton(text="📩 Biz bilan bog'lanish"),
            KeyboardButton(text="📊 Statistika")
        ],
        [
            KeyboardButton(text="👨‍👩‍👧‍👦 Biz haqimizda")
        ]
    ],
    resize_keyboard=True
)

tasdiq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Tasdiqlash"),
            KeyboardButton(text="❌ Bekor qilish")
        ]
    ],
    resize_keyboard=True
)