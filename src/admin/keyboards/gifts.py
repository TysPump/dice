from typing import List, Optional

from ...factory.session import Session
from .btn import btn
from ...database.tables import Gift

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

class GiftsMenuKeyboard:
    def __init__(self, s: Session):
        self.s = s

    def gift_menu(self, gift_id: int | str) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.row(
            btn(
                text=self.s.lang.button["edit"],
                callback="gift_edit:{}".format(gift_id)
            )
        )
        builder.row(
            btn(
                text=self.s.lang.button["delete"],
                callback="gift_delete:{}".format(gift_id)
            )
        )
        builder.row(
            btn(
                text=self.s.lang.button["close"],
                callback="close"
            )
        )

        return builder.as_markup()

    def gifts_menu(self, gifts: List[Gift]) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        for num, gift in enumerate(gifts):
            button = btn(
                text=gift.name,
                callback="gift:{}".format(gift.id)
            )
            if num == 0 or num%2 == 0:
                builder.row(button)
            else:
                builder.add(button)

        builder.row(
            btn(
                text=self.s.lang.button["add"],
                callback="new_gift"
            )
        )

        return builder.as_markup()
    
    def dice_panel(self, callback: Optional[str] = "add_value_to_gift:{}") -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        for i in range(1, 7):
            button = btn(
                text=self.s.lang.button[str(i)],
                callback=callback.format(i)
            )

            if i == 1 or i == 4:
                builder.row(button)
            else:
                builder.add(button)

        builder.row(
            btn(
                text=self.s.lang.button["cancle"],
                callback="edit_gifts"
            )
        )

        return builder.as_markup()
    
    def edit(self, gift_id: int | str) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.row(
            btn(
                text=self.s.lang.button["edit_title"],
                callback="gift_title_edit:{}".format(gift_id)
            )
        )
        builder.row(
            btn(
                text=self.s.lang.button["edit_desc"],
                callback="gift_desc_edit:{}".format(gift_id)
            )
        )
        builder.row(
            btn(
                text=self.s.lang.button["edit_image"],
                callback="gift_image_edit:{}".format(gift_id)
            )
        )
        # builder.row(
        #     btn(
        #         text=self.s.lang.button["edit_dice"],
        #         callback="gift_dice_edit:{}".format(gift_id)
        #     )
        # )

        builder.row(
            btn(
                text=self.s.lang.button["back"],
                callback="edit_gifts"
            )
        )

        return builder.as_markup()