from aiogram import types

from loader import dp,bot

@dp.message_handler(text="dars 1-5")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/211"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web dastur. Web sayt yozamiz\n\nUshbu dars boshlovchilar uchun ajoyib tajriba bo'lishi mumkin.\n\nBunda biz Semantic UI dan foydalanamiz:\n\nhttps://semantic-ui.com/\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/212"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web dastur. BackEnd qismi - Djangoni o'rnatish\n\nBu darsda Django Framework dan foydalanamiz:\n\nhttps://www.djangoproject.com/\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/213"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web server nima?\n\nWeb dasturchi bilishi kerak bo'lgan eng muhim tushunchalardan biri bu web server.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/214"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web dastur. BackEnd qismi - Djangoda birinchi sahifa\n\nBu darsda Django Framework dan foydalanamiz:\n\nhttps://www.djangoproject.com/\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/215"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web dastur. BackEnd qismi - Django Template \n\nUshbu darsda Django Framework dan foydalanamiz:\n\nhttps://www.djangoproject.com/\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="dars 6-10")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/216"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web dastur. BackEnd qismi - Django Static File\n\nBu darsda Django Framework dan foydalanamiz:\n\nhttps://www.djangoproject.com/\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/217"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web dastur. BackEnd qismi - Django Models\n\nBu darsda ham Django Framework dan foydalanamiz \n\nhttps://www.djangoproject.com/\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/218"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web dastur. BackEnd qismi - Django Request I Get\n\nBu darsda ham Django framework dan foydalanamiz:\n\nhttps://www.djangoproject.com/\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/219"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web dastur. BackEnd qismi - Making Query I SQL\n\nBu darsda Django Framework dan foydalanamiz:\n\nhttps://www.djangoproject.com/\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/220"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web dasturlash. BackEnd qismi - Making Query I Like\n\nBu darsda ham Django Frameworkdan foydalanamiz:\n\nhttps://www.djangoproject.com/\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Web-site yaratish 🇺🇿")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"<b>Bu bolimda 4ta darslik mavjud👇🏻👇🏻👇🏻</b>")
    video_manzili ="https://t.me/Mobil_dasturchilar/221"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="HTML va CSS yordamida 3 sahifali mehmonxona web site'ini yaratamiz\n\nUshbu 2 qismdan iborat video darsligimizda faqatgina HTML va CSS yordamida 3 sahifali mehmonxona web site'tini yaratamiz.\n\nSource Code: https://bit.ly/2lwA2Jf\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/222"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Mehmonxona web site'ini yaratamiz, 2-qism\n\nUshbu 2 qismdan iborat video darsligimizda faqatgina HTML va CSS yordamida 3 sahifali mehmonxona web site'ini yaratamiz.\n\nSource Code: https://bit.ly/2lwA2Jf\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/223"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Bootstrapda web site yasash\n\nLink: https://drive.google.com/drive/folders/1yrtztAul2Dibvx9aptJAbTeGnUtg3NjF\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/224"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Bootstrap 2 qism\n\nUshbu darsimizda Bootstrap orqali yasalgan web site'ni davom ettiramiz. \n\nBootstrap'da yasalgan web site 1-qism: https://www.youtube.com/watch?v=XH1aXNIpK4s\n\nStarter Folder: https://drive.google.com/drive/folders/1yrtztAul2Dibvx9aptJAbTeGnUtg3NjF\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 1-3")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/225"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="WordPress'ni o'rnatish\n\nWordPress bilan tanishish va uni lokal serverga o'rnatish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/226"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Admin va Shablon (Theme) bilan ishlash\n\nWordPress'ning admin paneli bilan tanishish va shablonni yangilash.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/227"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Maqola (Post), Bo'lim (Category), Kalit so'z (Tags) bilan ishlash\n\nQuyidagilarga javob olasiz:\n\n- WordPress'da qanday qilib maqola qo'shish\n- WordPressda maqola vaqtini oldindan belgilash\n- Maqolaga rasm o'rnatish (Featured image)\n- Bo'limlar bilan ishlash\n- Kalit so'zlar bilan ishlash\n- WordPress'da layout tushunchasi\n- WordPress'da maqolani himoya qilish (maqolaga parol berish)\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 4-7")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/228"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Fikrlar, izohlar (comments) bilan ishlash\n\nQuyidagilarga javob topasiz:\n\n- WordPress'da izoh bilan ishlash\n- WordPress'da qora ro'yxat\n- Fikrlarni boshqarish\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/229"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="WordPress'da sahifalar bilan ishlash\n\nQuyidagilarga javob olasiz:\n\n- WordPressda sahifalar bilan ishlash\n- Sahifa va maqola o'rtasidagi farq\n- Parent page nima?\n- Sahifada url\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/230"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="WordPress'ni yangilash\n\nWordPress, shablonlar, plugin'larni yangilash.\n\nWordPress'ning yangi versiyasiga o'tish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/231"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="WordPress'da yangi editor\n\nWordPress'ning yangilangan 5-versiyasida taqdim etilgan editor bilan tanishish.\n\n👉 @ITSchoolUz_RoBot")
