from aiogram.types import CallbackQuery

from ....factory.session import Session
from ...keyboard import UserKeyboards

class ContactsMenu:
    def __init__(self, s: Session, kb: UserKeyboards):
        self.s = s
        self.kb = kb

    async def contacts(self, call: CallbackQuery) -> None:
        await call.message.delete()

        contacts = await self.s.db.fetch.data(
            type_="contacts"
        )
        
        await call.message.answer(
            text=contacts.value if contacts else "Контакты",
            reply_markup=self.kb.nav.back(callback="main_menu")
        )