from aiogram import types

from loader import dp,bot

@dp.message_handler(text="DARS 1-5")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/301"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Visual Studio qanday o'rnatiladi?\n\nBirinchi darsda Visual Studio'ni o'rnatishni ko'ramiz va birinchi darsturimizni tuzamiz.\n\nVisual Studio'ni yuklab olish linki: https://goo.su/zOA\n\nC# da yozish web platformasi: https://dotnetfiddle.net/\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/302"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Ma'lumot turlari\n\nBu darsimizda ma'lumot turlarini ko'rib o'tamiz.\n\nTurli xil ma'lumot turlarini e'lon qiling va ularni konsolga chiqarishni mashq qiling.\n\nKeyingi darsda shu ko'nikmalardan foydalangan holda yangi dastur yaratamiz.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/303"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Operatorlar\n\nUshbu darsda siz operatorlar nimaligini bilib olasiz va ular bilan ishlashni ko'rib o'tamiz.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/304"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Mantiqiy amallar\n\nUshbu darsda siz C# dasturlash tilidagi eng muhim hisoblanuvchi - mantiqiy amallarni o'rganasiz.\n\nVideodan olgan bilimingizni amaliyotda qo'llashni unutmang.\n\nZero, shu yo'sinda dasturlashni tez va oson o'rganasiz.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/305"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Satr (String) bilan ishlash\n\nUshbu dasrda siz string ma'lumot turi bilan ishlashni o'rganasiz.\n\nString'lar ustida turli amallar bajaramiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="DARS 6-10")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/306"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Metodlar\n\nUshbu darsda siz bilan C# dasturlash tilidagi metodlarni ko'rib o'tamiz.\n\nBular yordamida yozayotgan kodimizda takrorlanishni va mavhumlikni oldini olamiz.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/307"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Metodlar (davomi)\n\nUshbu darsda siz bilan C# dasturlash tilidagi qiymat qaytaruvchi metodlarni ko'rib o'tamiz.\n\nBular yordamida yozayotgan kodimizda takrorlanishni va mavhumlikni oldini olamiz.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/308"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Array\n\nUshbu darsda siz bilan C# dasturlash tilidagi \"Array\" mavzusini ko'rib o'tamiz.\n\nBular yordamida o'zgaruvchilarni guruhlarga jamlashimiz mumkin.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/309"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Loop\n\nBugungi darsda Loop yoki Tsikl qanday tushuncha ekangligini bilib olasiz.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/310"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="\"List\" bilan ishlashni o'rganamiz\n\nUshbu darsda List tushunchasi bilan tanishib o'tamiz.\n\n👉 @ITSchoolUz_RoBot")
