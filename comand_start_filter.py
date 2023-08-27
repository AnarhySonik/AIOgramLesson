from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
API_TOKEN: str = os.getenv('API_TOKEN')
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


def my_start_filter(message: Message) -> bool:
    return message.text == '/start'


def custom_filter(some_list: list) -> bool:
    sum: int = 0
    for i in some_list:
        if type(i) == int and (i%7 == 0):
            sum += i
    return sum < 83




@dp.message(my_start_filter)
async def process_start_command(message: Message):
    await message.answer(text='Это команда /start')


if __name__ == '__main__':
    dp.run_polling(bot)
