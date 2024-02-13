from aiogram import *
from aiogram.types import InputFile
import logging
import requests
import json
import urllib.request
import os
from api_key import exampe_bot_token

bot = Bot(token=exampe_bot_token)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Assalomu Aleykum Botimizga xush kelibsiz\n"
                         "Siz bu yerda instagramdagi🌐 xoxlagan video ni yuklab olishingiz mumkin\n"
                         "Shunchaki video xavolasini bizga yuboring👇👇")

@dp.message_handler()
async def save_video(message: types.Message):
    if "https" in message.text:
        await message.reply("Iltimos biroz kuting⏰")
        url = "https://instagram-downloader.p.rapidapi.com/index"
        post = message.text
        querystring = {"url": post}

        headers = {"X-RapidAPI-Key": "TOKEN",
                   "X-RapidAPI-Host": "instagram-downloader.p.rapidapi.com"}
        response = requests.get(url, headers=headers, params=querystring)
        url_link = json.loads(response.text)
        video_link = url_link["result"]["video_url"]
        video_name = url_link["result"]["username"]
        video = urllib.request.urlretrieve(video_link, f"{video_name}.mp4")
        silka = f"C:/Users/user/PycharmProjects/Aiogram_bot/API_examples/{video_name}.mp4"
        await message.bot.send_video(chat_id=message.from_user.id, video=InputFile(silka))

        try:
            os.remove(silka)
        except FileNotFoundError:
            pass
    else:
        await message.reply("Bunday video topilmadi🫢\n"
                            "Xavolani to'g'ri ekanligini tekshirip ko'ring")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
