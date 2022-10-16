from aiogram import types

from loader import dp, bot


# Echo bot
@dp.message_handler(text="Dars #1")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/4"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="<b>Frontend #1\n\n🧑🏻‍💻 Dars muallifi Saud Abdulwahed\n\nYouTube:</b> https://bit.ly/3KXj1hx\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars #2")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/5"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="<b>Frontend #2\n\n🧑🏻‍💻 Dars muallifi Saud Abdulwahed\n\nYouTube:</b> https://bit.ly/3KXj1hx\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="Dars #3")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/6"
    await bot.send_video(chat_id=user_id, video=video_manzili,
                         caption="<b>Frontend #3\n\n🧑🏻‍💻 Dars muallifi Saud Abdulwahed\n\nYouTube:</b> https://bit.ly/3KXj1hx\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="Dars #4")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/7"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="<b>Frontend #4\n\n🧑🏻‍💻 Dars muallifi Saud Abdulwahed\n\nYouTube:</b> https://bit.ly/3KXj1hx\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="1-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/8"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="1 soatda HTML'ni professional darajada o’rganamiz\n\nRasm olishingiz uchun saytlar:\n\nhttps://unsplash.com/\n\nhttps://gratisography.com/\n\nhttps://www.pexels.com/ru-ru/\n\nHTML teglar: https://bit.ly/3ETFsko\n\nHTML maxsus simvollar: https://bit.ly/3EH2qLr\n\nHTML inputlar: https://bit.ly/32HWgh4\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="2-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/9"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="45 daqiqada CSS’ni o’rganamiz I 1-qism \n\nShriftlar o'zgartirish uchun: https://bit.ly/3mQ4nz0\n\nShrift stillari: https://bit.ly/31gYkMb\n\nTransition stillari: https://bit.ly/3FS3JZe/n/nBorder stillari: https://bit.ly/3sMDC2h\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="3-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/10"
    await bot.send_video(chat_id=user_id, video=video_manzili,
                         caption="40 daqiqada CSS’ni o’rganamiz I 2-qism\n\nDisplay-block haqida batafsil: https://bit.ly/3zw7uRX\n\nDisplay-inline-block haqida batafsil: https://bit.ly/3FS4Ckw\n\nDisplay-flex haqida batafsil: https://bit.ly/3ERJjOx\n\nDisplay-grid haqida batafsil: https://bit.ly/3ziaYao\n\nTransform haqida batafsil: https://bit.ly/32L6MUF\n\nPosition (relative, absolute, fixed & enc.) haqida batafsil: https://bit.ly/3FSLuCX\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="4-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/11"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="HTML va CSS yordamida qanday qilib web-site yaratish | To'liq qo'llanma\n\nWeb-site kodi: https://bit.ly/32WABRO\n\nFont-size haqida batafsil: https://bit.ly/34f0OvQ\n\nLinear-gradient haqida batafsil: https://bit.ly/3FRo94K\n\nRoot haqida batafsil: https://mzl.la/3JA8f0z\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="5-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/12"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="<b>HTML va CSS yordamida Responsive (Adaptiv) web-site yaratish\n\nWeb-site kodi: https://bit.ly/32WdrLG\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="6-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/13"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Bootstrap'ga kirish I 1-qism\n\nBootstrap ulash uchun: https://bit.ly/3sR5D8D\n\nRedaktorlar qo'llanmasi: https://bit.ly/3qKkBLd\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="7-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/14"
    await bot.send_video(chat_id=user_id, video=video_manzili,
                         caption="Bootstrap Grid Sistemasi\n\nBootstrap ulash uchun: https://getbootstrap.com/\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="8-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/15"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Bootstrap 5 Responsive Portfolio web-site'ga qo'llanma\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="9-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/16"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="15 daqiqada SASS’ni proffesional darajada o'rganamiz \n\n👉 @ITSchoolUz_Bot")

@dp.message_handler(text="10-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/17"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Portfolio Responsive web-site HTML, CSS, JavaScript yordamida\n\nWeb-site yuklab olish uchun: https://bit.ly/3qEg6Ss\n\n👉 @ITSchoolUz_Bot")

@dp.message_handler(text="11-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/18"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="SASS mini loyiha\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="1 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/19"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="1 soatda HTML'ni o'rganamiz\n\nBu videoda sizlarga HTML haqida eng kerakli bilimlarni o'rgatamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="2 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/20"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="CSS'ni o'rganamiz 1-qism\n\nBu videoda sizlar bilan CSS ya'ni web site'ni skileti haqida dars olib boramiz.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="3 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/21"
    await bot.send_video(chat_id=user_id, video=video_manzili,
                         caption="CSS'ni o'rganamiz 2-dars\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="4 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/22"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="CSS'ni o'rganamiz 2-dars\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="5 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/23"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="CSS Cheatsheet\n\nUshbu darsimizda CSS'dagi bilimlarimizni bir marta qaytarib olish orqali mustahkamlab olamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="6 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/24"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="CSS media query & Bootstrap'ga kirish\n\nUshbu live video darsimizda CSS'dagi media query'lar bilan ishlash hamda Bootstrap'dan boshlang`ich bilimlarni berishga harakat qilamiz.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="7 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/25"
    await bot.send_video(chat_id=user_id, video=video_manzili,
                         caption="3 sahifali web site yaratamiz\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="8 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/26"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="3 sahifali web site yaratamiz, 2-qism\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="1_Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/27"
    await bot.send_video(chat_id=user_id, video=video_manzili,
                         caption="25 daqiqada SASS'ni o'rganamiz\n\nRuby dasturini yuklab olish: https://bit.ly/3FC1ath\n\nSASS'ning rasmiy veb-sayti: https://sass-lang.com/\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="2_Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/28"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="SASS bo'yicha amaliyot\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="1-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/29"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript'da o'zgaruvchilar: Var, Const.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="2-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/30"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Ma'lumot turlari: String, Number, Boolean.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="3-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/31"
    await bot.send_video(chat_id=user_id, video=video_manzili,
                         caption="JavaScript'da For loop.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="4-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/32"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="If - else & Switch - case shartli operatori.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="5-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/33"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript'da funksiya va return.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="6-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/34"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript'da Dom manipulyatsiyasi.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="7-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/35"
    await bot.send_video(chat_id=user_id, video=video_manzili, caption="JavaScript This, Bind, Call & Apply.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="8-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/36"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript Closure.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="9-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/37"
    await bot.send_video(chat_id=user_id, video=video_manzili,
                         caption="JavaScript LocalStorage.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="10-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/38"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript Class, Getters & Setters.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="11-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/39"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript ProtoType.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="12-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/40"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Chuqurlashtirilgan JavaScript Oddiy so'zlar bilan.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="13-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/41"
    await bot.send_video(chat_id=user_id, video=video_manzili,caption="JavaScript amaliyot: Korzina yasash.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="14-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/42"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript amaliyot, chuqurlashtirilgan JS | Dom bilan ishlash.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="15-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/43"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript'da Loader yasaymiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="16-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/44"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript'da o'yin yaratish.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="17-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/45"
    await bot.send_video(chat_id=user_id, video=video_manzili,caption="JavaScript'da To Do List yasash.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="18-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/46"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript amaliyot: Class yordamida dinamic content.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="19-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/47"
    await bot.send_video(chat_id=user_id, video=video_manzili,caption="JavaScript'da Slider yaratamiz.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="20-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/48"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript'da Slider yaratamiz: Owl Carousel.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="21-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/49"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Vanilla JS.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="22-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/50"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="API, JSON & Promise.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="23-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/51"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript amaliyot: Weather App.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="1_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/52"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JS haqida ma`lumot, 'var' kalit so`zi.\n\nUshbu videoda JavaScriptdagi boshlang`ich ko`nikmalari berilgan.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="2_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/53"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="String, Number, Boolean. Matematik hisoblash\n\nUshbu Videoda Javascriptda var kalit so`zi va ma`lumot turlari bo`lgan String, Number, Booleanlar tushuntirilgan.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="3_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili = "https://t.me/Mobil_dasturchilar/54"
    await bot.send_video(chat_id=user_id, video=video_manzili,
                         caption="JavaScript yordamida BMI (body mass index) hisoblash\n\nUshbu videoda JavaScript yordamida BMI (body mass index) ni hisoblashni o`rganamiz.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="4_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/55"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="If Else tushunchasi\n\nUshbu videoda JavaScriptda 'if else' haqida batafsil tushuntiriladi.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="5_dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/56"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JavaScript va ES6 1 soatda - Boshlang`ich ko`nikmalar\n\nUshbu videodan JavaScriptga oid boshlang`ich ko`nikmalar, xususan: \n\n- var, const, let\n\n- string, number, array, object\n\n- array functions: push, map, filter, forEach\n\n- ES6 xususiyatlari\n\n- for loop\n\n- if else statements\n\n- switch function\n\n- functions\n\n- es6 features\n\nhaqida bilimga ega bo`lasiz.\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="1 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/57"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Kirish\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="2 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/58"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Terminalda ishlash. CLI\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="3 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/59"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Metod bilan ishlash. Interpolatsiya\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="4 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/60"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Formalar bilan ishlash. Hodisalar\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="5 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/61"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Props va $emit nima? Ular bilan ishlash\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="6 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/62"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="UI Kutubxona yasaymiz\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="7 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/63"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Modal oynasi\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="8 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/64"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Server bilan ishlash. Lifescyle method\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="9 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/65"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Filterlash category bo'yicha\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="10 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/66"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Kontent category bo'yicha o'zgartirish\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="11 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/67"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Pagination va Animatsiya\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="12 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/68"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Navigatsiya bilan ishlash\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="13 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/69"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Amaliyot\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="14 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/70"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Amaliyot\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="15 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/71"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Amaliyot: Weather App\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="16 dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/72"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Amaliyot: Progress Bar\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars_#1")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/73"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Kirish\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="Dars_#2")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/74"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Dastur ochish, Fayllar strukturasi\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="Dars_#3")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/75"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Pages, Routing\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="Dars_#4")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/76"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Layout component\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="Dars_#5")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/77"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Style turlari\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="Dars_#6")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/78"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Link, Image Component\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="Dars_#7")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/79"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Dynamic Routing\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="Dars_#8")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/80"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Maxsus Error 404 sahifa\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="Dars_#9")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/81"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="API bilan ishlash (CSR va SSR)\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="Dars_#10")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/82"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="API bilan ishlash (SSG)\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="Dars_#11")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/83"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Lokal JSON Data ishlatish\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#1-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/84"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Angular darslari kirish\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#2-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/85"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Fayllar strukturasi \n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#3-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/86"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Material UI\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#4-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/87"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Komponentlar bilan ishlash \n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#5-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/88"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Dialog komponent\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#6-Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/89"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Formalar bilan ishlash\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#1 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/90"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="TypeScript kirish\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#2 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/91"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="TypeScript nima? \n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#3 Dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/92"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="TypeScript kurs haqida\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="#1-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/93"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="React yordamida Ob-havo dasturi\n\nBu darsda OpenWeather API orqali React'da Ob-havo dasturini qanday qilib yasalishini o'rganamiz! \n\nOpenWeather API'dan foydalanish: https://openweathermap.org/\n\nDarsimizning kodlari: https://goo.su/aXL\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#2-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/94"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Crypto Price Tracker dasturini yasaymiz (Crash kurs) | React JS, CoinGecko API\n\nBugungi React bo'yicha amaliyot darsimizda Kripto valyutalarni ko'rsatib turuvchi ajoyib App'ni qanday yasalishini o'rganamiz.\n\nBugungi darsimiz kodlari: https://goo.su/SLX\n\nDasturning demo versiyasi: https://goo.su/oZO\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#3-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/95"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="TikTok’ning clone versiyasini yasaymiz | React JS, Firebase\n\nBugungi amaliyot darsimiz ancha qiziqarli bo'ladi. \n\nSababi bugun sizlar bilan React JS, Firebase texnologiyalari yordami TikTok'ning clone dasturini yasab ko'ramiz.\n\nDasturning demo versiyasi: https://goo.su/coO\n\nDarsimizning kodlari: https://goo.su/9jwW\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#4-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/96"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="FAQ Reader Ovozli assistent dasturini yasaymiz | Alan AI, React JS\n\nBugungi amaliyot darsimiz ancha qiziqarli bo'ladi.\n\nSababi Alan AI, hamda React JS orqali FAQ Reader ovozli assistent dasturini yasashni o'rganamiz.\n\nFAQ Reader demo: https://faqreader.netlify.app/\n\nDarsimizning kodlari: https://goo.su/cac\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#5-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/97"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="React JS va Firebase bilan Avtorizatsiya\n\nUshbu darsda qanday qilib React JS, Firebase texnologiyalari yordamida Avtorizatsiya dasturini tuzishni o'rganamiz. \n\nDarsimizning kodlari: https://goo.su/Knr\n\nAvtorizatsiyaning demo versiyasi: https://goo.su/GkC\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#6-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/98"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Rasmlar Qidiruv dasturi | React JS, Unsplash API\n\nYana bir qiziqarli amaliyot darsimizda React hamda Unsplash API orqali \"Photo Search App\" qanday yasalishini o'rganamiz.\n\nDarsimizning kodlari: https://goo.su/vxf\n\nKerakli package'lar: https://goo.su/mfN I https://goo.su/nFy\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#7-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/99"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Google Autentifikatsiya bilan ishlash | React JS, Firebase\n\nGugungi amaliyotda React, Firebase bilan Google autentifikatsiyasini qanday yasalishini o'rganamiz.\n\nDarsimizning kodlari: https://goo.su/nrD\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#8-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/100"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="YouTube’ning clone versiyasini yasaymiz | React, YouTube Api\n\nUshbu amaliyotimizda qanday qilib YouTube'ning clone versiyasini React, YouTube API orqali yasalishini ko'rib, o'rganib chiqamiz. \n\nGoogle API Library: https://goo.su/ao5\n\nDarsimiz kodlari: https://goo.su/hKg\n\nDemo: https://ytclone1.netlify.app/\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#9-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/101"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="React'da QR Kod Generatori | React JS\n\nNavbatdagi amaliyotimizda esa React, hamda QR Server API orqali QR kod generatorini yasab ko'ramiz.\n\nReact JS bo'yicha to'liq darslarimiz: https://goo.su/9La7\n\nDarsimiz kodlari: https://goo.su/vqu\n\nDemo: https://qrcode1.netlify.app\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#10-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/102"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Web to'lovlar bilan ishlash | React JS, Stripe, Node JS\n\nBugungi darsimizda React, Stripe JS bilan Web to'lov yasab, u bilan ishlashni ko'ramiz.\n\nBundan tashqari dasturimizning Backend qismini Node JS orqali sozlaymiz.\n\nDarsimiz kodlari: https://goo.su/W5n\n\nKerakli packagelar ro'yhati: https://goo.su/9wGY\n\n👉 @ITSchoolUz_RoBot")
@dp.message_handler(text="#11-dars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/103"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Pokemon Dasturini yasaymiz! | React JS, Poke API\n\nUshbu amaliyot darsida nisbatan osonroq bo'lgan qiziqarli loyiha qilamiz, ya'ni Poke API orqali React'da \"Pokemon\" dasturini tuzishni o'rganamiz!\n\nDarsimiz kodlari: https://goo.su/9xIK\n\nPokemon API: https://pokeapi.co\n\n👉 @ITSchoolUz_RoBot")