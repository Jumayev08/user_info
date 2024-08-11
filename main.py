from aiogram import Dispatcher, Bot, types
from asyncio import run
from funksiyalar import get_user_info
dp=Dispatcher()
async def startup_answer(bot: Bot):
    await bot.send_message(chat_id=6124235622, text="Bot ishga tushdi ✅")

async def shutdown_answer(bot: Bot):
    await bot.send_message(chat_id=6124235622, text="Bot ishdan to'xtadi ❌")


async def start():
    dp.message.register(get_user_info)
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    bot = Bot(token="6563336446:AAGbsgymHNM1OuptD-AzLZC3f9nO8iNn8dE")
    await dp.start_polling(bot, polling_timeout=1)

run(start())