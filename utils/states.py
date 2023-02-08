from aiogram.fsm.state import StatesGroup, State


class Moon(StatesGroup):
    day1 = State()
    day2 = State()
    cool = State()

