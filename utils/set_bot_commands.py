from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("manba", "manbalar bo'yicha malumotlar"),
            types.BotCommand("admin","Administrator"),
            types.BotCommand("help", "Yordam"),
        ]
    )
