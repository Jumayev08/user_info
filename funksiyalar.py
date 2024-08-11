from aiogram import *
from aiogram.types import *

async def get_user_info(message: types.Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    user_photos = await message.from_user.get_profile_photos()
    
    text=""
    text+="Foydalanuvchi: "+str(message.from_user.mention_html(message.from_user.full_name))+"\n"
    text+="ID: "+str(message.from_user.id)+"\n"
    if user.username: text+="Username: @"+str(message.from_user.username)+"\n"
    if user.bio: text+="Bio: "+str(user.bio)+"\n"
    if user_photos.photos:
        await message.answer_photo(user_photos.photos[0][-1].file_id,caption=text, parse_mode="HTML")
    else:
        await message.answer(text, parse_mode="HTML")
