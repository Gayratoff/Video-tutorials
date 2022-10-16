from aiogram import types
from aiogram.dispatcher import FSMContext
from states.murojaat import Murojaat
from keyboards.default.Menu import  tasdiq,Menu_button
from loader import dp,bot



@dp.message_handler(text="📩 Biz bilan bog'lanish")
async def bot_echo(message: types.Message):
    await message.answer(text="🙎🏻‍♂️ <b>Biz bilan bog'lanish uchun Ismingizni kiriting:</b>")
    await Murojaat.Ism_holati.set()

@dp.message_handler(state=Murojaat.Ism_holati)
async def bot_echo(message:types.Message,state:FSMContext):

    ism = message.text
    await state.update_data({"ism": ism})
    await message.answer(text="<b>🙍🏻‍♂️Familyangiz</b>")
    await Murojaat.Familya_holati.set()

@dp.message_handler(state=Murojaat.Familya_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    fam = message.text
    await state.update_data({"FAm": fam})
    await message.answer(text="<b>🕹Yoshingiz</b>")
    await Murojaat.Yoshi_holati.set()

@dp.message_handler(state=Murojaat.Yoshi_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data({"yosh": yosh})
    await message.answer(text="<b>☎️Raqamingiz\n\nMisol uchun :</b> +998935338025")
    await Murojaat.Raqami_holati.set()

@dp.message_handler(state=Murojaat.Raqami_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    nom = message.text
    await state.update_data({"num": nom})
    await message.answer(text="<b>💬Murojatingiz</b>")
    await Murojaat.Xabar_holati.set()

@dp.message_handler(state=Murojaat.Xabar_holati)
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    await state.update_data({"text": txt})

    malumot= await state.get_data()

    ismi = malumot.get("ism")
    familya = malumot.get("FAm")
    yoshi = malumot.get("yosh")
    nomeri = malumot.get("num")
    xabri = malumot.get("text")

    ekranga_chiqarish = f"🙍🏻‍♂️<b>Ism :</b> {ismi}\n" \
                        f"🙍🏻‍♂️<b>Familya :</b> {familya}\n"\
                        f"🕹<b>Yosh :</b> {yoshi}\n" \
                        f"☎️<b>Raqam :</b> {nomeri}\n" \
                        f"💬<b>Murojat :</b> {xabri}\n"

    await bot.send_message(chat_id=user_id,text=ekranga_chiqarish,reply_markup=tasdiq)
    await Murojaat.tasdiqlash_holati.set()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="✅ Tasdiqlash")
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    malumot = await state.get_data()

    ismi = malumot.get("ism")
    familya = malumot.get("FAm")
    yoshi = malumot.get("yosh")
    nomeri = malumot.get("num")
    xabri = malumot.get("text")

    ekranga_chiqarish = f"🙍🏻‍♂️{ismi} <b>Dan murojaat kelib tushdi</b>\n" \
                        f"🙍🏻‍♂️<b>Ism :</b> {ismi}\n" \
                        f"🙍🏻‍♂️<b>Familya :</b> {familya}\n"\
                        f"🕹<b>Yosh :</b> {yoshi}\n" \
                        f"☎️<b>Raqam :</b> {nomeri}\n" \
                        f"💬<b>Murojat :</b> {xabri}\n"
    await bot.send_message(chat_id="1625900856",text=ekranga_chiqarish)
    await bot.send_message(chat_id=user_id,text="Adminga Yuborildi ✅",reply_markup=Menu_button)
    await state.finish()

@dp.message_handler(state=Murojaat.tasdiqlash_holati,text="❌ Bekor qilish")
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=Menu_button)
    await state.finish()




