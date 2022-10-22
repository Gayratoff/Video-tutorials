from aiogram import types

from loader import dp,bot


@dp.message_handler(text="Dars 1")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/356"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Viewport'lar bilan tanishuv\n\nUshbu darsda 3Ds Max dasturining Viewport qismi bilan tanishasiz va ularning yordamchi klavishlarini ham bilib olasiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 2")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/357"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Interfeys qismini sozlash\n\nUshbu darsda 3Ds Max darsturining Interfeys qismi bilan tanishamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 3")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/358"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Primitive elementlarni hosil qilish\n\nBu darsda 3Ds Max dasturida Primitive elementlarni hosil qilishni o'rganasiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 4")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/359"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Select, Move, Rotate, Scale\n\nBu darsda Main Toolbar bo'limidagi Belgilash, Surish, Aylantirish, hamda O'lchamni O'zgartirish buyruqlari bilan tanishasiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 5")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/360"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Select, Move, Rotate, Scale I 2-qism\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 6")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/361"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Undo, Redo va Autoback (Orqaga, Oldinga va Autoback)\n\nUshbu darsda Undo, Redo va Autoback buyruqlarini o’rganasiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 7")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/362"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Save turlari.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 8")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/363"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Copy I Instance I Reference\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 9")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/364"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Snaps (Magnitlar)\n\nHozir siz bilan Primitive elementlar yordamida Snaps (magnitlar) bo'limi bilan tanishib, ularning qanday ishlashini ko'rib chiqamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 10")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/365"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Editable Poly va Editable Spline'ga konvert qilish\n\nBu darsda Primitive elementlarni \"Editable Poly va Editable Spline\" ga convert qilishni o'rganamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 11")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/366"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Editable Poly’ning Selection bo'limi\n\nBu darsda Editable Poly’ning Selection bo'limi (Belgilash bo'limi) bilan tanishamiz va belgilash turlarini o'rganamiz.\n\nBular: Vertex, Edge, Border, Polygon va Element.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 12")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/367"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Extrude\n\nUshbu darsda Editable Poly’dagi Extrude buyrug’i bilan ishlashni o’rganamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 13")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/368"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Connect, Cut, Quick Slice, Slice Plane\n\nBu darsda Connect, Cut, Quick Slice va Slice Plane buyruqlari bilan ishlashni o’rganamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 14")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/369"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Ortiqcha nuqta va segmentlarni to'g'ri olib tashlash\n\nBu darsda Remove Vertex and Remove Edge buyruqlari bilan ishlashni o’rganamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 15")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/370"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Nuqta va segmentlarni ulash va bir-biridan ajratish\n\nBu darsda Vertex, Edge, Weld va Break bilan ishlashni o'rganamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 16")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/371"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Insert, Outline va Bevel\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 17")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/372"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Bridge va Chamfer\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 18")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/373"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Attach va Detach\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 19")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/374"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Qo'shimcha dars\n\nBu darsda Editable Poly to’g’risida qo'shimcha ma’lumot beriladi.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 20")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/375"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Proboolean\n\nBugungi darsda Proboolean buyrug’ini o'rganamiz.\n\nBu buyruq asosan (Exterior va Interior) modelingda oyna va eshiklarning joyini asosiy devordan ajratib olish, ya'ni bo'shliq hosil qilish uchun ishlatiladi.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 21")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/376"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Pivot o'qlarining yo'nalishini o'zgartirish\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 22")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/377"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Import va Export\n\nBu darsda 3D modellarni 3Ds Max dasturiga Import va 3Ds Max dasturidan boshqa dasturlar uchun Export qilishni o'rganamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 23")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/378"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Obyektni boshqa bir yuzaga aniq va tez joylashtirish\n\nBu darsimizda Select and Place buyruqlarini o'rganamiz.\n\nBu buyruqlar Interior’ga aksessuar joylashtirishda juda ham asqotadi.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 24")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/379"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Mirror\n\nBu darsda Copy yoki Instance buyruqlariga o'xshash Mirror bilan tanishamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 25")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/380"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Array\n\nDarslikda ishlatilgan Stol va Stulning modelini quyidagi link orqali ko'chirib olishingiz mumkin:\n\nLink: https://yadi.sk/d/lZaL-8vJeUJwxQ\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 26")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/381"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Use pivot point center\n\nDarsda ishlatilgan Stol va Stulning modelini quyidagi link orqali ko'chirib olishingiz mumkin:\n\nLink: https://yadi.sk/d/lZaL-8vJeUJwxQ\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 27")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/382"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Align, Quick Align va Normal Align\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 28")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/383"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Spline hosil qilish.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 29")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/384"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Outline\n\nHozir siz bilan Outline buyrug'ini o'rganamiz.\n\nOutline Editable Spline'da joylashgan.\n\nBu buyruq bizga istagan line'ni ichki yoki tashqi tarafiga qo'shimcha line hosil qilishda yordam beradi.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 30")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/385"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Spline'dagi nuqtalarning turlari.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 31")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/386"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Line'ga qo'shimcha nuqtalar qo'shish.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 32")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/387"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Spline'dagi Chamfer va Filled\n\nHozir siz bilan Editable Spline'dagi \"Chamfer va Fillet\" buyruqlarini o'rganamiz.\n\nBu ikki buyruq bir biriga juda o'xshash vazifani bajaradi.\n\nBu buyruqni o'tkir va o'tmas burchaklarni yumshatish yoki kesib tashlash uchun ishlatamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 33")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/388"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Modifikatorlar nima?\n\nBu darsda Modifikatorlar to'g'risida umumiy ma'lumot beriladi.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 34")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/389"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Edit Poly Modifikatori\n\nHozirgi darsda Edit Poly modifikatorini o'rganamiz.\n\nYodingizda bo'lsa Editable Poly buyrug'ini o'rgangan edik.\n\nBu modifikator ham huddi shu vazifani bajaradi.\n\nLekin undan ozgina ustun taraflari mavjud.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 35")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/390"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Extrude\n\nHozir siz bilan Extrude modifikatorini o'rganamiz.\n\nBu modifikatorni biz Line yoki Spline'larga bir tomonlama hajm berishda ishlatamiz.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 36")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/391"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Shell modifikatori\n\nHozir siz bilan \"Shell\" modifikatorini o'rganamiz.\n\nBu modifikator huddi Extrude'ga o'xshaydi, ammo bu modifikatorni ham Line'ga ham Poly'ga ishlatsak bo'ladi.\n\nBu modifikator obyektimizga 2 tomonlama hajm beradi.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 37")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/392"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Sweep\n\nBugun siz bilan Sweep modifikatorini o'rganamiz.\n\nBu modifikatorni Line va Editable Spline'larga qo'llash mumkin.\n\nBu modifikator orqali biz profil, plintus va karnizlar yasashimiz mumkin.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 38")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/393"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Sweep'dagi xatoliklar.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 39")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/394"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Bevel Profile\n\nBugungi darsimizda siz bilan Bevel Profile modifikatorini o'rganamiz.\n\nBu modifikatorni ishlashi huddi Sweep modifikatoriga o'xshaydi. \n\nDeyarli bir xil natija olinadi. \n\nBazi vaziyatlarda Sweep yoki Bevel yaxshi ishlamay qolish vaqtlari ham bo'lishi mumkin. \n\nAna o'sha vaziyatda yoki Sweep yoki Bevel Profile modifikatorini ishlatishimizga to'g'ri keladi.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 40")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/395"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Bevel Profile I 2-qism.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 41")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/396"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Lathe modifikatori.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 42")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/397"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="FFD modifikatori\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 43")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/398"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Symmetry\n\n3D Modelni yuklab olish:\n\nhttps://yadi.sk/d/Jbboyf-oDpR-Bw\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 44")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/399"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="AutoCad yordamida PDF'dan DWG'ga import qilish\n\nPDF chizmani yuklab olish:\n\nhttps://yadi.sk/d/lV0kwJHFzr8stg\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 45")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/400"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="DWG plan yordamida devor ko'tarish.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 46")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/401"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="JPEG chizma yordamida devor ko'tarish\n\nJPEG faylni yuklab olish:\n\nhttps://yadi.sk/i/B4ZJK4Mxl4hLIA\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 47")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/402"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Interfeysni sozlash I 2-qism\n\nHozir siz bilan 3Ds Max'ga qo'shimcha Plugin va Script'lar o'rnatamiz.\n\nMuhim eslatma!\n\nBa'zi Plugin va Script'lar 3Ds Max darsturining versiyasiga qarab o'rnatiladi.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 48")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/403"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Floor Generator\n\nBugungi darsda siz bilan Floor Generator modifikatorini o'rganamiz.\n\nBu modifikatordan biz asosan tarket, parket, kafel, plitka va turli xil dekorativ panellar yasayotganda foydalanamiz.\n\nMuxim eslatma!!!\n\nVideo darsni oxirigacha ko'rishingizni tavsiya qilaman.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 49")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/404"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Relink Bitmap, Sweep Profile, Copy&Paste\n\nBugun siz bilan oldingi darslarimizda o'rnatgan Script'larimiz bilan tanishamiz.\n\nKitoblar modelini ushbu link orqali ko'chirib olishingiz mumkin:\n\nhttps://yadi.sk/d/J-gYixD5FeAx2Q\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 50")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/405"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Interior Modeling\n\nBu darsda siz \"Perspective Match\" orqali Reference'dan nusxa olishni o'rganasiz.\n\n3D Modellar:\n\nhttps://yadi.sk/d/0B4vZl3gldyBvg?w=1\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 51")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/406"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="3Ds Max'da 0 dan Interyer Vizualizatsiya qilish\n\nDarsda ishlatilgan 3D modellar, teksturalarni link orqali ko'chirib olishingiz mumkin:\n\nhttps://yadi.sk/d/QLZZH4UZK5-otg\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Dars 52")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/407"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Oshxona mebelini yasash (Kitchen Modeling)\n\n3D Modellar:\n\nhttps://yadi.sk/d/EtfuEazX-PccBg?w=1\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="Modeling")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"<b>Bu bolimda 3ta darslik mavjud👇🏻👇🏻👇🏻</b>")
    video_manzili ="https://t.me/Mobil_dasturchilar/408"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="(Spot) Chiroq modelini yasashni o'rganamiz\n\nBu darsda Spot ya'ni chiroq modelini yasash, material berish, render qilish va post qilishni o'rganasiz.\n\nInfo va 3Ds Max faylni shu yerdan ko'chirib olishingiz mumkin:\n\nhttps://yadi.sk/d/tSnvujkUvZKtvg\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/409"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Pufik modelini yasash\n\nBu darsda Pufik modelini yasash, material berish, render qilish va post qilishni o'rganasiz.\n\nInfo va 3Ds Max faylni shu yerdan ko'chirib olishingiz mumkin:\n\nhttps://yadi.sk/d/RVyS2MQ7bwwEqQ\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/410"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Deko svetilnik modelini yasash.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="DARS 1-3")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/411"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Blender'da Interfeys va Navigatsiya\n\nBu darsda Blender'dagi Interfeys va Navigatsiya to'g'risida gaplashamiz.\n\nBlender'ning rasmiy sayti: https://www.blender.org/\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/412"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Modellash asoslari\n\nUshbu darsda siz chuqurlashtirilgan tarzda modellashtirish prinsiplarini o'rganasiz.\n\nDars so'ngidagi stol va stul modellari faqatgina amaliy mashg'ulot sifatida qo`yilgan.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/413"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Modifikatorlar\n\nBugungi darsda Modelling'ga kerak bo'ladigan modifikatorlar haqida so'z boradi. \n\nUlar yordamida biz ishimizni ancha osonlashtirishimiz mumkin.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="DARS 4-6")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/414"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Barrel modelini yasash I Bonus\n\nUshbu bonus darsimizda barrel modelini yasaymiz.\n\nVideoda ishlatilgan teksturalar: https://t.me/RDGroup3D\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/415"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Tekstura\n\nUshbu darsda siz obyektga qanday qilib rang berish va realistik tekstura qo'yish haqida tushuncha olasiz.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/416"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Barrel - Tekstura&Render I Bonus\n\nUshbu darsda oldin yasagan Barrel modelimizni ranglash va render qilishni o'rganamiz. \n\nAgar siz ranglashdan xabaringiz bo'lmasa bundan oldingi darsimizni ko'rishni tafsiya etamiz.\n\nVideoda ishlatilgan teksturalar: https://t.me/RDGroup3D\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="DARS 1-4")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/417"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Autodesk Maya dasturiga kirish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/418"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Interfeys\n\nBu darsda Maya'ning interfeysi bilan tanishasiz.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/419"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="3D modeling.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/420"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Sodda 3D modellarni yasash.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="DARS 5-7")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/421"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Sodda 3D modellarni yasash.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/422"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Mebel naqshlarini yasash.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/423"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Mebel naqshlarini yasash.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="DARS  1-5")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/424"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="ZBrush'ga kirish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/425"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Robotni modellash.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/426"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Maskadan to'g'ri foydalanish va teksturalash.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/427"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Turntable video va render qilish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/428"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="LightBox instrumentlari.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="DARS 6-9")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/429"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Export qilish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/430"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Teksturalash va Alpha'lar bilan ishlash.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/431"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Fiber - soch va soqol hosil qilish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/432"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Fiber bilan ishlovchi brushlar.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="DARS 1-6")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/433"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="AutoCAD nima va qanday loyihlar qilsa bo'ladi?\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/434"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Line, Polyline, Circle buyruqlari.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/435"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Devor chizish, Mirror, Trim.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/436"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Zina va ustun qilish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/437"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Ustun va eshik o'rni chizish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/438"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Rom o'rni va rom chizish.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="DARS 7-11")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/439"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Eshik chizish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/440"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="1-qavat chizmasi va do’kon o'rnini chizish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/441"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Yerto’la qavatini chizish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/442"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Do’kon eshigi va lift eshigini chizish.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/443"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Yakuniy dars.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="Adobe After Effects 🇺🇿")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"<b>Bu bolimda 5ta darslik mavjud👇🏻👇🏻👇🏻</b>")
    video_manzili ="https://t.me/Mobil_dasturchilar/444"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Kirish\n\nAdobe After Effects to'g'risida tushuncha.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/445"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Interfeys\n\nUshbu darsda After Effects interfeysi va shakllarnig tuzilishi bilan tanishamiz va birinchi animatsiyani yaratamiz!\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/446"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Orqa fon elementlari\n\nUshbu darsimizda Adobe Illustrator fayllarini After Effects'da qanday ishlashini ko'rib chiqamiz va kelajakdagi animatsiyalarda foydalanishingiz mumkin bo'lgan animatsiya aylanish jarayonining bir nechta effektlari va sirlarini bilib olamiz.\n\nIshlatilgan fayllar: https://goo.su/uJF\n\nMotion Tools scripti: https://goo.su/bHt\n\nIshlatilgan kodlar: https://goo.su/E2F\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/447"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="sosiy obyektlar\n\nBu darsda biz sahnaning asosiy obyektlarini jonlantiramiz: ya'ni olov va xarakterlarni.\n\nBuning uchun biz bundan oldingi darsda bergan olov_rig faylidan foydalanamiz.\n\nAgar uni yuklab olmagan bo'lsangiz pastdagi havolalar orqali yuklab olishingiz mumkin.\n\nIshlatilgan kodlar: https://goo.su/bRA\n\nIshtatilgan fayllar: https://goo.su/lB9\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/448"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Yorug'lik effektlari\n\nUshbu darsda siz soyalar va yorug'lik effektlarini, animatsiya maslahatlari, yangi effektlarni va fokuslarni o'rganasiz.\n\nIshlatilgan fayllar: https://goo.su/fLC\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="DARS   1-5")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/449"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Adobe Premiere Pro dasturining interfeysi bilan tanishuv.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/450"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Adobe Premiere Pro dasturida montaj ishlari.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/451"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Adobe Premier Pro'da ranglar bilan ishlash.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/452"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Yashil fon bilan ishlash.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/453"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Musiqalar bilan ishlash.\n\n👉 @ITSchoolUz_RoBot")

@dp.message_handler(text="DARS 6-11")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/454"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Maskalar bilan ishlash.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/455"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Maskalar bilan ishlash, 2-qism\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/456"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Maskalar bilan ishlash, 3-qism\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/457"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Slideshow.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/458"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Effect control, motion.\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/459"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Export.\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="Adobe Illustrator 🇺🇿")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/506"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Dars 1\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/507"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Dars 2\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/508"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Dars 3\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/509"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Dars 4\n\n👉 @ITSchoolUz_RoBot")


@dp.message_handler(text="Mockup dizayn kursi 🇺🇿")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    video_manzili ="https://t.me/Mobil_dasturchilar/510"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Mockup Design kursiga kirish\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/511"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Maxsus saytlardan foydalanish\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/512"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Mobil ilova uchun Mockup\n\nVideodars resurslari: https://bit.ly/36pzV6G\n\n👉 @ITSchoolUz_RoBot")
    video_manzili ="https://t.me/Mobil_dasturchilar/513"
    await bot.send_video(chat_id=user_id,video=video_manzili,caption="Video interactive Mockup\n\nVideodars resurslari: https://bit.ly/3kQEaxP\n\n👉 @ITSchoolUz_RoBot")


