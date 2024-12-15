from ...factory.session import Session
from .btn import btn

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

class DiceMenuKeyboard:
    def __init__(self, s: Session):
        self.s = s

    def spin_menu(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.row(
            btn(
                text=self.s.lang.button["spin_dice"],
                callback="spin_dice"
            )
        )

        return builder.as_markup()