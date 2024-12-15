from ...factory.session import Session
from .btn import btn

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

class NavigationKeyboards:
    def __init__(self, s: Session) -> None:
        self.s = s

    def back(self, **kwargs) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.add(
            btn(
                text=self.s.lang.button["back"],
                callback=kwargs.get("callback", "")
            )
        )

        return builder.as_markup()
    
    def menu(self, **kwargs) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.add(
            btn(
                text=self.s.lang.button["menu"],
                callback="main_menu"
            )
        )

        return builder.as_markup()