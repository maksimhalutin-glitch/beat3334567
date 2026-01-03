import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from aiogram.filters import Command

BOT_TOKEN = "8426681684:AAGPDeM0Lrddnb7dgBpEBbBYJRviV_RRpyo"
WEBAPP_URL = "https://maksimhalutin-glitch.github.io/beat3334567/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎧 Открыть BЁAT",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )

    await message.answer(
        "Добро пожаловать в BЁAT 🔥\n\n"
        "Нажми кнопку ниже, чтобы открыть приложение.",
        reply_markup=keyboard
    )


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
