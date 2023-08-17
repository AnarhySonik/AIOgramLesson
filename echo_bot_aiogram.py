from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
API_TOKEN: str = os.getenv('API_TOKEN')
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот (покачто)\nНапиши что-нибудь')


@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer('Напиши сюда чтонибудь, я пришлю тоже самое')


@dp.message(Command(commands=["calc"]))
async def process_calc_command(message: Message):
    result = 25+25
    await message.answer(str(result))


@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
