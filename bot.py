import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

BOT_TOKEN = "8426681684:AAGPDeM0Lrddnb7dgBpEBbBYJRviV_RRpyo"
WEBAPP_URL = "https://maksimhalutin-glitch.github.io/beat3334567/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(
                text="🎧 Открыть BЁAT",
                web_app={"url": WEBAPP_URL}
            )
        ]],
        resize_keyboard=True
    )

    await message.answer(
        "Добро пожаловать в BЁAT 🔥",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
