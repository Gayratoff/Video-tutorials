from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from data.tekshirish import tekshir
from data.config import kanal
from loader import bot


class Asosiy(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = "Botimizdan foydalanish uchun rasmiy kanalimizga <b>obuna bo'ling</b> va <b>Tekshirish</b> tugmasini bosing."
        royxat = []
        dastlabki = True
        for k in kanal :
            holat = await tekshir(user_id=user_id,kanal_id=k)
            dastlabki *= holat

            kanals = await bot.get_chat(k)

            if not holat:
                link = await kanals.export_invite_link()
                button = [InlineKeyboardButton(text=f"{kanals.title}",url=f"{link}")]
                royxat.append(button)
            royxat.append([InlineKeyboardButton(text="✅ Tekshirish",callback_data="start")])
            if not dastlabki:
                await bot.send_message(chat_id=user_id,text=matn,disable_web_page_preview=True,
                                       reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
                raise CancelHandler()
