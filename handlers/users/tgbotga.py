from aiogram import types

from loader import dp,bot

@dp.message_handler(text="#1_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/195"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Kurs bilan tanishuv.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#2_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/196"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Kerakli dasturlar.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#3_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/197"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Metodologiya.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#4_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/198"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="BotFather.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#5_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/199"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="AIOgram.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#6_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/200"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Wikibot.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#7_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/201"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="API nima?\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#8_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/202"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Bot uchun qiziqarli API topamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#9_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/203"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Python'da API bilan ishlash.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#10_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/204"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="SpeakEnglish bot.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#11_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/205"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="ImloBot. 1-qism: So'zlarni tekshirish.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#12_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/206"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="ImloBot. 2-qism: Bot dasturi.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#13_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/207"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Botni serverga yuklash.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#14_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/208"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Diqqat, aksiya!\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Python'da Telegram Bot 🇺🇿")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"<b>Bu bolimda 2ta darslik mavjud👇🏻👇🏻👇🏻</b>")
    video_manzili ="https://t.me/Mobil_dasturchilar/209"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Bot yaratish\n\nDarsda Python dasturi yordamida Wikipediya bot'ni tayyorlashni ko'rib chiqamiz.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/210"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Botni serverga yuklash.\n\n👉 @ITSchoolUz_RoBot")