from aiogram.types import Message

from ....factory.session import Session
from ...keyboard import AdminKeyboards

class Panel:
    def __init__(
        self,
        s: Session,
        kb: AdminKeyboards
    ) -> None:
        self.s = s
        self.kb = kb

    async def panel_menu(self, msg: Message) -> None:
        if msg.from_user.id not in self.s.config.admins:
            return
        
        await msg.answer(
            text=self.s.lang.text["admin_panel"],
            reply_markup=self.kb.panel.panel_menu()
        )