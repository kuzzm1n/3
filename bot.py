import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# Ваш токен бота
TOKEN = '7207040124:AAHuWchouAISQq-tsIxlWQIDppBGGpdzceY'

# Создание экземпляра бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    # Создание кнопки с WebApp
    web_app_button = KeyboardButton(text="Веб приложение", web_app=WebAppInfo(url="https://kuzzm1n.github.io/1/"))

    # Создание клавиатуры и добавление кнопки
    keyboard = ReplyKeyboardMarkup(keyboard=[[web_app_button]], resize_keyboard=True)

    await message.answer("Вот ваш бот", reply_markup=keyboard)

# Основная функция запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
