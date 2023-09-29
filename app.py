import logging

from aiogram import executor
from aiogram import types
import handlers
from utils.commands import set_default_commands
from loader import dp, db_bot


async def on_startup(dispatcher):
    db_bot.open()
    db_bot.create_default_table()
    logging.info("Db has opened connection")
    await set_default_commands(dispatcher)


async def on_shutdown(dispatcher):
    db_bot.close()
    logging.info("Db has closed connection")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
