from aiogram import types


from loader import dp


@dp.message_handler(commands="admin")
async def bot_start(message: types.Message):
    await message.answer(f"<b>🙎🏻‍♂️ Administrator: </b> @MrGayratov")

