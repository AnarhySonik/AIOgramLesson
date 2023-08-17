from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
API_TOKEN: str = os.getenv('API_TOKEN')
print(API_TOKEN)
