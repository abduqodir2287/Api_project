import logging
import requests
from PIL import Image, ImageDraw, ImageFont
from aiogram import *
from aiogram.types import InputFile
from textwrap import wrap
from api_key import exampe_bot_token
import os

bot = Bot(token=exampe_bot_token)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)
font = ImageFont.truetype("arial.ttf", size=30)

def justify(line, width):
    gap_width, max_replace = divmod(width - len(line) + line.count(' '), line.count(' '))
    return line.replace(' ', ' ' * gap_width).replace(' ' * gap_width, ' ' * (gap_width + 1), max_replace)

def lines_formatter(a, width):
    lines = wrap(a, width, break_long_words=False)
    for j, line in enumerate(lines[:-1]):
        if len(line) <= width and line.count(' '):
            lines[j] = justify(line, width).rstrip()
    n = '\n'.join(lines)
    return n

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(f"Assalomu Aleykum {message.from_user.username} botga xush kelibsiz")
    await message.answer("Siz bu yerda Qur'on suralarini oqishingiz mumkin\n"
                         "Sura raqamini yozing👇👇\n"
                         "(1 dan 114 gacha:)")

@dp.message_handler()
async def text(message: types.Message):
    info = ""

    try:
        if int(message.text) >= 1 and int(message.text) <= 114:
            url = f"https://al-quran1.p.rapidapi.com/{int(message.text)}"
            headers = {
                "X-RapidAPI-Key": "48ec87fe45mshecb35adf6cb2136p11cf43jsn838685d94fd2",
                "X-RapidAPI-Host": "al-quran1.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers)
            data = response.json()
            name = data["surah_name"]
            for i in data["verses"]:
                info += data['verses'][i]["content"]
            l = lines_formatter(info, 40)
            img = Image.new("RGB", (1000, 1000), "black")
            draw = ImageDraw.Draw(img)
            draw.text((250, 250), f"{l[::-1]}", fill="white", font=font)
            img.save(f"{data['surah_name']}.jpg")
            silka = f"C:\\Users\\user\PycharmProjects\pythonProject5\pythonProject\Api_project\\{name}.jpg"
            photo = InputFile(silka)
            await message.answer(f"{message.text}-chi sura 👇👇👇")
            await message.bot.send_photo(chat_id=message.from_user.id, photo=photo)

            try:
                os.remove(silka)
            except FileNotFoundError:
                pass
        else:
            await message.reply("Xatolik yuzaga keldi🫢\n"
                                "Sura raqami tog'ri ekanligini tekshirib ko'ring")
    except:
        await message.reply("Iltimos Suraning raqamini sonda kiriting\n"
                            "(1 dan 114 gacha:)")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)



