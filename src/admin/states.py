from aiogram.fsm.state import StatesGroup, State

class NewGift(StatesGroup):
    title = State()
    desc = State()
    image = State()

class EditGift(StatesGroup):
    title = State()
    desc = State()
    image = State()
    dice = State()