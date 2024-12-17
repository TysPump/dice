from ...factory.session import Session
from .btn import btn

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

class PanelKeyboard:
    def __init__(self, s: Session):
        self.s = s

    def panel_menu(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.row(
            btn(
                text=self.s.lang.button["panel_gifts"],
                callback="edit_gifts"
            )
        )
        builder.row(
            btn(
                text=self.s.lang.button["contacts"],
                callback="edit_contacts"
            )
        )
        builder.row(
            btn(
                text=self.s.lang.button["conditions"],
                callback="edit_conditions"
            )
        )

        return builder.as_markup()