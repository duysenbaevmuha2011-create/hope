import asyncio
from email import message
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


@dp.message(Command('baxa'))
async def baxa(message: Message):
    await message.answer('atim baxa')

@dp.message(Command('a'))
async def a(message: Message):
    await message.answer('atim a')

@dp.message(Command('b'))
async def b(message: Message):
    await message.answer('atim b')

@dp.message(Command('c'))
async def c(message: Message):
    await message.answer('atim c')


@dp.message(Command('d'))
async def d(message: Message):
    await message.answer('atim d')    


@dp.message(Command('w'))
async def w(message: Message):
    await message.answer('atim w')


@dp.message(Command('r'))
async def r(message: Message):
    await message.answer('atim r')


@dp.message(Command('q'))
async def q(message: Message):
    await message.answer('atim q')


@dp.message(Command('t'))
async def t(message: Message):
    await message.answer('atim t')


@dp.message(Command('y'))
async def y(message: Message):
    await message.answer('atim y')


@dp.message(Command('u'))
async def u(message: Message):
    await message.answer('atim u')


@dp.message(Command('i'))
async def i(message: Message):
    await message.answer('atim i')


@dp.message(Command('o'))
async def o(message: Message):
    await message.answer('atim o')


@dp.message(Command('p'))
async def p(message: Message):
    await message.answer('atim p') 


@dp.message(Command('m'))
async def m(message: Message):
    await message.answer('atim m')


@dp.message(Command('n'))
async def n(message: Message):
    await message.answer('atim n')


@dp.message(Command('b'))
async def b(message: Message):
    await message.answer('atim b')


@dp.message(Command('v'))
async def v(message: Message):
    await message.answer('atim v')


@dp.message(Command('x'))
async def x(message: Message):
    await message.answer('atim x')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())