import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart , Command 
from aiogram.types import Message
from dotenv import load_dotenv
import os
load_dotenv()


Token = os.getenv("API")
bot = Bot(token=Token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello')

@dp.message(Command('jardem'))
async def help(message: Message):
    await message.answer('Sizge qanday jardem kerek')

@dp.message(Command('tel'))
async def tel(message: Message):
    await message.answer('+998936022010')

@dp.message(Command('baxa'))
async def baxa(message: Message):
    await message.answer('atim baxa')
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())