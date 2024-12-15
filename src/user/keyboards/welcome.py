from typing import Optional

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ...factory.shemas import Session
from .btn import btn

class WelcomeKeyboard:
    def __init__(self, s: Session):
        self.s = s

    def main_menu(self) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.row(
            btn(
                text=self.s.lang.button["gifts"], 
                callback="gifts"
            )
        )
        builder.row(
            btn(
                text=self.s.lang.button["info"],
                url=self.s.config.infoUrl
            )
        )
        builder.row(
            btn(
                text=self.s.lang.button["contacts"],
                callback="contacts"
            )
        )

        return builder.as_markup()