import datetime
from babel import dates as babel_dates

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5874530586:AAFyxocoEyN7LanT-f8aAUlc-R9XZiJsj6Y'

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

amazing_str = ""


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Amazing Bot.\nYou may know what I can do typing /help")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply(
        """
        I may do a lot of amazing things such as:
        /help - information about my amazing opportunities
        /time - get amazing current time in Moscow
        /date - get amazing current date in Moscow(probably not only in Moscow)
        /save <Your message> - save new amazing message
        /print - print last amazing saved message
        /print_amazing_number - print amazing number
        """
    )


@dp.message_handler(commands=['time'])
async def send_time(message: types.Message):
    now = datetime.datetime.now()
    await message.reply(f"Current time is {babel_dates.format_datetime(now, format='HH:mm')}")


@dp.message_handler(commands=['date'])
async def send_welcome(message: types.Message):
    now = datetime.datetime.now()
    await message.reply(f"Current date is {babel_dates.format_datetime(now, format='dd:MM')}")


@dp.message_handler(commands=['print'])
async def send_welcome(message: types.Message):
    await message.reply(f"Last amazing string is {amazing_str}")


@dp.message_handler(commands=['save'])
async def send_welcome(message: types.Message):
    global amazing_str
    amazing_str = message['text'][6:]
    await message.reply(f"Saved '{amazing_str}'")


@dp.message_handler(commands=['print_amazing_number'])
async def send_welcome(message: types.Message):
    await message.reply(f"Amazing number is 42")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
