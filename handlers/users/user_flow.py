from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db_bot
from states import Updates


@dp.message_handler(commands=['get_user_by_id'])
async def get_user_info(msg: types.Message):
    try:
        user_id = int(msg.text.split()[1])
        user_info = db_bot.get_user_by_id(user_id)
        await msg.reply(user_info)
    except (IndexError, ValueError):
        await msg.reply("Веддіть команду у такому форматі:\n/get_user_by_id user_id")


@dp.message_handler(commands=['get_user_by_name'])
async def get_user_info(msg: types.Message):
    user_name = msg.get_args()
    if user_name:
        user_info = db_bot.get_user_by_name(user_name)
        await msg.reply(user_info)
    else:
        await msg.reply("Веддіть команду у такому форматі:\n/get_user_by_name user_name")


@dp.message_handler(commands=['add_me'])
async def add_user(msg: types.Message):
    user_id = msg.from_user.id
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    user_name = msg.from_user.username

    if not db_bot.user_exists(user_id):
        db_bot.add_user_to_db(user_id, first_name, last_name, user_name)
        await msg.reply("Користувача було успішно додано")
    else:
        await msg.reply("Такий користувач вже існує")


@dp.message_handler(commands=['remove_me'])
async def remove_user(msg: types.Message):
    user_id = msg.from_user.id

    if db_bot.user_exists(user_id):
        db_bot.remove_user_from_db(user_id)
        await msg.reply("Користувача успішно видалено")
    else:
        await msg.reply("Такого користувача не існує")


@dp.message_handler(commands=["update_me"])
async def update_me(message: types.Message, state: FSMContext):
    await message.answer("Будь ласка, введіть ваше нове ім'я:")
    await Updates.Question_State.set()


@dp.message_handler(state=Updates.Question_State.state)
async def update_me_first_name(message: types.Message, state: FSMContext):
    new_first_name = message.text

    await message.answer("Тепер введіть ваше нове прізвище:")

    await state.update_data(new_first_name=new_first_name)

    await Updates.First_Name_State.set()


@dp.message_handler(state=Updates.First_Name_State)
async def update_me_last_name(message: types.Message, state: FSMContext):
    new_last_name = message.text

    user_id = message.from_user.id

    data = await state.get_data()
    new_first_name = data.get('new_first_name')

    result_message = db_bot.update_user_info(user_id, new_first_name, new_last_name)

    await message.answer(result_message)

    await state.finish()


@dp.message_handler(commands=['remove_me'])
async def remove_user(msg: types.Message):
    user_id = msg.from_user.id


@dp.message_handler(commands=['start'])
async def get_user_info(msg: types.Message):
    await msg.reply("Hello")
