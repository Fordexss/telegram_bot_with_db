from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустити бота'),
            types.BotCommand('add_me', 'додати користувача'),
            types.BotCommand('remove_me', 'видалити мене'),
            types.BotCommand('update_me', 'змінити ім\'я та прізвище'),
            types.BotCommand('get_user_by_id', 'переглянути користувача за id'),
            types.BotCommand('get_user_by_name', 'перелянути користувача за іменем'),


        ]
    )
