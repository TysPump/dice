from aiogram.types import CallbackQuery

from ....factory.session import Session
from ...keyboard import AdminKeyboards

class AdminPanel:
    def __init__(self, s: Session, kb: AdminKeyboards) -> None:
        self.s = s
        self.kb = kb

    async def admin_panel(self, call: CallbackQuery) -> None:
        await call.message.edit_text(
            text=self.s.lang.text["admin_panel"],
            reply_markup=self.kb.panel.panel_menu()
        )

    async def close(self, call: CallbackQuery) -> None:
        await call.message.delete()

