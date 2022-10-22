from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

# --------------Dasturlash MENU--------------
from keyboards.default.Menu import Menu_button
from keyboards.default.Dastur_dars import dasturlash
from keyboards.default.Video import video_montaj
from keyboards.default.frilans import frilans_dars
from keyboards.default.SMM import Smm
from keyboards.default.fronted import  Fronted_dars,Saud
from keyboards.default.backend import Backend_dars
from keyboards.default.tgbot import TgBot
from keyboards.default.web import Web
from keyboards.default.mobil import Mobil
from keyboards.default.suniy import Suniy
from keyboards.default.oop import Oop
from keyboards.default.c1 import C1
from keyboards.default.admin import admin_panel
# --------------Dasturlash MENU--------------
# --------------Dizayn MENU--------------
from keyboards.default.Dizayn.grafika3d import Grafika
from keyboards.default.Dizayn.Adobe import adobe
from keyboards.default.Dizayn.garfik import Grf
from keyboards.default.Dizayn.Ui import UX
from keyboards.inline.inlne import rasmiy_kanal,admins
from keyboards.inline.inlinegrafik import asror, madina,figma,upw,zafar
from keyboards.inline.smmin import modu1,modu2

# --------------Dizayn MENU--------------
from loader import dp,bot,base

@dp.message_handler(commands="panel",chat_id="1625900856")
async def bot_start(message: types.Message):
    await message.answer("<b>✅ panel ishladi! @MistrUz</b>",reply_markup=admin_panel)

@dp.message_handler(commands="panel")
async def bot_start(message: types.Message):
    await message.answer("<b>Bu bo'lim faqat @MistrUz uchun</b>",reply_markup=Menu_button)


@dp.message_handler(commands="rek",chat_id="1625900856")
async def bot_start(message: types.Message):

    userlar= base.select_all_foidalanuvchilar()
    for user in userlar:
        user_id =user[3]
        video_manzili = "https://t.me/XUDOBERDI_GAYRATOV/18"
        await bot.send_photo(chat_id=user_id,photo=video_manzili,caption="👋 Assalomu alaykum \n\nQadli obunachilarimiz Sizlarni Telegramdagi IT, Biznes, Texnologiyalari Yangliklari kanaliga taklif qilamiz😇\n\n➞ IT Yangliklari\n➞ Biznes Yangliklari\n➞ Texnologiya Yangliklari\n➞ Valyuta Kurslari\n➞ O'zbek, Ingliz va Rus tillarida life-hacklar\n\n➞ Sahifamizni ochish: @IT_Subject")
    for users in userlar:
        users_id= users[0]
    await  message.answer(text=f"<b>{users_id} ta foidalanuvchilarga reklama yuborildi ✅</b>")

@dp.message_handler(text="📊 Statistika")
async def bot_start(message: types.Message):
    users= base.select_all_foidalanuvchilar()
    for user in users:
        user_id= user[0]
    await  message.answer(text=f"<a href='{'https://t.me/ITSchoolUz_Robot'}'>IT School bot</a> "
                               f"<b> statistikasi 📶\n\n👤 Foydalanuvchilar: {user_id}\n\n🟢 Bot holati: Online\n\nMurojaat uchun: </b>"
                               f"<a href='{'https://t.me/MrGayratov'}'>Xudoberdi G'ayratov</a> ",disable_web_page_preview=True,reply_markup=Menu_button)


@dp.callback_query_handler(text="start")
async def bot_echo(message: CallbackQuery):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Botdan foidalanishingiz mumkin",reply_markup=Menu_button)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    fam= message.from_user.last_name
    user_id = message.from_user.id
    video_manzili ="https://t.me/XUDOBERDI_GAYRATOV/15"
    try:
        base.user_qoshish(ism=ism,fam=fam,tg_id=user_id)
    except Exception as xatolik:
        print(xatolik)

    await bot.send_photo(chat_id=user_id, photo=video_manzili, caption=f"👋 Assalomu alaykum {message.from_user.full_name} !\n@IT_Subject Kanalining Video Darsliklar botiga Xush Kelibsiz😇✅",reply_markup=rasmiy_kanal)
    await message.answer("<b>Barcha savollar yuzasidan:</b> @MrGayratov",reply_markup=Menu_button)

@dp.message_handler(text="Adobe Photoshop (Asror Iskandarov) 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer("<b>Adobe Photoshop (Asror Iskandarov) Darslari 🇺🇿</b>",reply_markup=asror)

@dp.message_handler(text="Adobe Illustrator (Madina Mavlonova) 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer("<b>Adobe Illustrator (Madina Mavlonova) Darslari 🇺🇿</b>",reply_markup=madina)

@dp.message_handler(text="Figma 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer("<b>Figma Darslari 🇺🇿</b>",reply_markup=figma)

@dp.message_handler(text="UPWork'da karyera 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer("<b>UPWork'da karyera Darslari 🇺🇿</b>",reply_markup=upw)

@dp.message_handler(text="Zafarbek Ibrohimov 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer("<b>Zafarbek Ibrohimov Darslari 🇺🇿</b>",reply_markup=zafar)

@dp.message_handler(text="1 - Modul")
async def bot_start(message: types.Message):
    await message.answer("<b>SMM Darslari 🇺🇿</b>",reply_markup=modu1)

@dp.message_handler(text="2 - Modul")
async def bot_start(message: types.Message):
    await message.answer("<b>SMM Darslari 🇺🇿</b>",reply_markup=modu2)
# --------------Asosiy MENU--------------
@dp.message_handler(text="🧑🏻‍💻 Dasturlash darslari")
async def bot_start(message: types.Message):
    await message.answer(f"🧑🏻‍💻 <b>Dasturlash darslari</b>" , reply_markup=dasturlash)

@dp.message_handler(text="🏞 Dizayn darslari")
async def bot_start(message: types.Message):
    await message.answer(f"🏞 <b>Dizayn darslari</b>" , reply_markup=video_montaj)

@dp.message_handler(text="🏄‍♂️ Frilanserlik darslari")
async def bot_start(message: types.Message):
    await message.answer(f"🏄‍♂️ <b>Frilanserlik darslari</b>" , reply_markup=frilans_dars)

@dp.message_handler(text="📱SMM")
async def bot_start(message: types.Message):
    await message.answer(f"<b>📱SMM</b>" , reply_markup=Smm)

@dp.message_handler(text="👨‍👩‍👧‍👦 Biz haqimizda")
async def bot_start(message: types.Message):
    await message.answer(f"@ITSchoolUZ_RoBOT <b>loyihasi frilans bozorini shakllantirish va yetakchi IT - mutaxassislar tayyorlashga qaratilgan.\n\nMaqsadimiz insonlar ongida oz bo'lsa ham o'zi va yon atrofdigilarga manfaat keltiradigan bilimlarni shakllantirish.</b>",reply_markup=Menu_button)

# --------------Asosiy MENU--------------

# --------------Qaytish MENU--------------
@dp.message_handler(text="🔝 Asosiy Menyu")
async def bot_start(message: types.Message):
    await message.answer(f"🔝 <b>Asosiy Menyu</b>" , reply_markup=Menu_button)


@dp.message_handler(text="🔙 Orqaga")
async def bot_start(message: types.Message):
   await message.answer(f"🔝 <b>🧑🏻‍💻 Dasturlash darslari</b>", reply_markup=dasturlash)

@dp.message_handler(text="🔙 Ortga")
async def bot_start(message: types.Message):
   await message.answer(f"🔝 <b>🏞 Dizayn darslari</b>", reply_markup=video_montaj)
# --------------Qaytish MENU--------------

# --------------Dasturlash MENU--------------
@dp.message_handler(text="Frontend 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Frontend 🇺🇿</b>" , reply_markup=Fronted_dars)

@dp.message_handler(text="Backend 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Backend 🇺🇿</b>" , reply_markup=Backend_dars)

@dp.message_handler(text="Telegram-Bot 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Telegram-Bot 🇺🇿</b>" , reply_markup=TgBot)

@dp.message_handler(text="Web Dasturlash 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Web Dasturlash 🇺🇿</b>" , reply_markup=Web)

@dp.message_handler(text="Mobil Dasturlash 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Mobil Dasturlash 🇺🇿</b>" , reply_markup=Mobil)

@dp.message_handler(text="Sun'iy intellekt 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Sun'iy intellekt 🇺🇿</b>" , reply_markup=Suniy)

@dp.message_handler(text="OOP dasturlash 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>C# boshlang'ich darslari👇🏻👇🏻👇🏻 🇺🇿</b>" , reply_markup=Oop)

@dp.message_handler(text="1C dasturlash 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>1C dasturlash 🇺🇿</b>" , reply_markup=C1)
# --------------Dasturlash MENU--------------

# --------------Dizayn MENU--------------
@dp.message_handler(text="3D Garfika 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>3D Garfika 🇺🇿</b>" , reply_markup=Grafika)

@dp.message_handler(text="Video Montaj 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Video Montaj 🇺🇿</b>" , reply_markup=adobe)

@dp.message_handler(text="Grafik Dizayn 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Grafik Dizayn 🇺🇿</b>" , reply_markup=Grf)

@dp.message_handler(text="Ui/UX Dizayn 🇺🇿")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Ui/UX Dizayn 🇺🇿</b>" , reply_markup=UX)
# --------------Dizayn MENU--------------
