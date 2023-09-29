from aiogram.dispatcher.filters.state import StatesGroup, State


class Updates(StatesGroup):
    Question_State = State()
    First_Name_State = State()

