import time
import logging

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

TOKEN = "5497514167:AAEKJC1u4ErVuBIzcwFzj5AlMNJrFLuun6w"

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserStates(StatesGroup):
    name = State()
    age = State()
    gender = State()

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_full_name = message.from_user.full_name
    await message.reply(f"hi, {user_full_name}! \nyou can ask me about available commands by writing /help")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = 'I can answer the following commands:\n/start \n/help \n/go \n/reminder'
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['go'])
async def process_go_command(message: types.Message):
    await UserStates.name.set()
    await message.reply("what's your name?")

@dp.message_handler(state='*', commands=['cancel'])
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('cancelled.', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=UserStates.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await UserStates.next()
    await message.reply("how old are you?")


@dp.message_handler(lambda message: not message.text.isdigit(), state=UserStates.age)
async def process_age_invalid(message: types.Message):
    return await message.reply("age gotta be a number.\nhow old are you?")


@dp.message_handler(lambda message: message.text.isdigit(), state=UserStates.age)
async def process_age(message: types.Message, state: FSMContext):
    await UserStates.next()
    await state.update_data(age=int(message.text))

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("male", "female")
    markup.add("other")

    await message.reply("what is your gender?", reply_markup=markup)


@dp.message_handler(state=UserStates.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

        # Remove keyboard
        markup = types.ReplyKeyboardRemove()

        # And send message
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('hi! nice to meet you,', data['name']),
                md.text('age:', data['age']),
                md.text('gender:', data['gender']),
                md.text('now you can record your reminder with the command /reminder'),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )
    await state.finish()

class ReminderStates(StatesGroup):
    reminder = State()

@dp.message_handler(commands=['reminder'])
async def reminder_writer(message: types.Message):
    await ReminderStates.reminder.set()
    await message.reply("what would you like to be reminded of? \nenter reminder text")

@dp.message_handler(state=ReminderStates.reminder)
async def process_reminder(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['reminder'] = message.text
        markup = types.ReplyKeyboardRemove()
        for i in range(10):
            await bot.send_message(
                message.chat.id,
                md.text(data['reminder']),
                reply_markup=markup,
                parse_mode=ParseMode.MARKDOWN,
            )
            time.sleep(60*60*4)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
