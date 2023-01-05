import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5497514167:AAEKJC1u4ErVuBIzcwFzj5AlMNJrFLuun6w"
REMINDER = "{}, did you workout today?"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"hi, {user_full_name}")

@dp.message_handler(commands=['remind'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')

    for i in range(10):
        await bot.send_message(user_id, REMINDER.format(user_name))
        time.sleep(60*60*4)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
