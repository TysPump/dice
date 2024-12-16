from aiogram.types import CallbackQuery

from ....factory.session import Session
from ...keyboard import UserKeyboards

class ContactsMenu:
    def __init__(self, s: Session, kb: UserKeyboards):
        self.s = s
        self.kb = kb

    async def contacts(self, call: CallbackQuery) -> None:
        await call.message.delete()
        
        await call.message.answer(
            text=self.s.lang.text["contacts"],
            reply_markup=self.kb.nav.back(callback="main_menu")
        )