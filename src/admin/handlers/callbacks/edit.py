from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ....factory.session import Session
from ...keyboard import AdminKeyboards
from ...states import StateEdit
from ....database.tables import Data

class Edit:
    def __init__(self, s: Session, kb: AdminKeyboards):
        self.s = s
        self.kb = kb

    async def contacts(self, call: CallbackQuery, state: FSMContext) -> None:
        current_contacts = await self.s.db.fetch.data(type_="contacts")

        if current_contacts is None:
            await self.s.db.add.data(
                data=Data(
                    **{
                        "type_": "contacts",
                        "value": "Контакты"
                    }
                )
            )

        await state.set_state(StateEdit.value)

        await state.update_data({"type_": "contacts"})

        await call.message.edit_text(
            text=self.s.lang.text["admin_data_"].format(current_contacts.value if current_contacts else "Контакты"),
            reply_markup=self.kb.nav.cancle(callback="admin_panel")
        )

    async def conditions(self, call: CallbackQuery, state: FSMContext) -> None:
        current_data = await self.s.db.fetch.data(type_="conditions")

        if current_data is None:
            await self.s.db.add.data(
                data=Data(
                    **{
                        "type_": "conditions",
                        "value": "Условия"
                    }
                )
            )

        await state.set_state(StateEdit.value)

        await state.update_data({"type_": "conditions"})

        await call.message.edit_text(
            text=self.s.lang.text["admin_data_"].format(current_data.value if current_data else "Условия"),
            reply_markup=self.kb.nav.cancle(callback="admin_panel")
        )