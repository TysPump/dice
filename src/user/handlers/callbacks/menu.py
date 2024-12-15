from aiogram.types import CallbackQuery

from ....factory.session import Session
from ...keyboard import UserKeyboards

class UserMainMenu:
    def __init__(self, s: Session, kb: UserKeyboards):
        self.s = s
        self.kb = kb

    async def main_menu(self, call: CallbackQuery) -> None:
        await call.message.answer_animation(
            animation="CgACAgIAAxkDAAICjWddrqq0Pd2j7ZwlRrxY_zVQk3zJAAKkZwACgRbwSrRqNFqSJS-KNgQ",
            caption=self.s.lang.text["welcome"],
            reply_markup=self.kb.welcome.main_menu()
        )
    