from datetime import datetime

from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from ....factory.session import Session
from ...keyboard import AdminKeyboards
from ...states import NewGift, EditGift
from ....database.tables import Gift

class GiftsPanel:
    def __init__(self, s: Session, kb: AdminKeyboards):
        self.s = s
        self.kb = kb

    def _date(self) -> float:
        return datetime.now().timestamp()

    async def gifts_menu(self, call: CallbackQuery, state: FSMContext) -> None:
        await state.clear()

        gifts = await self.s.db.fetch.gifts()

        await call.message.edit_text(
            text=self.s.lang.text["gifts_menu"],
            reply_markup=self.kb.gifts.gifts_menu(gifts=gifts)
        )

    async def new_gift(self, call: CallbackQuery, state: FSMContext) -> None:
        await state.set_state(NewGift.title)

        await call.message.edit_text(
            text=self.s.lang.text["title_need"],
            reply_markup=self.kb.nav.cancle()
        )

    async def delete(self, call: CallbackQuery) -> None:
        gift_id = call.data.split(":")[-1]

        await self.s.db.remove.gift(id_=gift_id)

        await call.message.delete()

        await call.message.answer(
            text=self.s.lang.text["deleted_finish"],
            reply_markup=self.kb.nav.back(callback="edit_gifts")
        )

    async def edit(self, call: CallbackQuery) -> None:
        gift_id = call.data.split(":")[-1]

        await call.message.edit_reply_markup(
            reply_markup=self.kb.gifts.edit(gift_id)
        )

    async def write_new_gift(self, call: CallbackQuery, state: FSMContext) -> None:
        value = call.data.split(":")[-1]

        gift_data = await state.get_data()

        gift_data["dicePosition"] = int(value)
        gift_data["date"] = self._date()

        await state.clear()

        await self.s.db.add.gift(
            data=Gift(
                **gift_data
            )
        )

        await call.message.edit_text(
            text=self.s.lang.text["gift_added"],
            reply_markup=self.kb.nav.back(callback="admin_panel")
        )

    async def gift_menu(self, call: CallbackQuery) -> None:
        gift_id = call.data.split(":")[-1]

        gift_data = await self.s.db.fetch.gift(id_=int(gift_id))

        await call.message.answer_photo(
            photo=gift_data[0].image,
            caption=self.s.lang.text["gift_menu"].format(
                gift_data[0].name,
                gift_data[0].desc,
                self.s.lang.button[str(gift_data[0].dicePosition)]
            ),
            reply_markup=self.kb.gifts.gift_menu(gift_id=gift_data[0].id)
        )

    async def edit_title(self, call: CallbackQuery, state: FSMContext) -> None:
        await state.set_state(EditGift.title)

        i = call.data.split(":")[-1]

        await state.update_data({"giftId": int(i)})

        await call.message.answer(
            text=self.s.lang.text["title_need"],
            reply_markup=self.kb.nav.cancle()
        )

    async def edit_desc(self, call: CallbackQuery, state: FSMContext) -> None:
        await state.set_state(EditGift.desc)

        i = call.data.split(":")[-1]

        await state.update_data({"giftId": int(i)})

        await call.message.answer(
            text=self.s.lang.text["desc_need"],
            reply_markup=self.kb.nav.cancle()
        )

    async def edit_image(self, call: CallbackQuery, state: FSMContext) -> None:
        await state.set_state(EditGift.image)

        i = call.data.split(":")[-1]

        await state.update_data({"giftId": int(i)})

        await call.message.answer(
            text=self.s.lang.text["image_need"],
            reply_markup=self.kb.nav.cancle()
        )

    async def edit_dice(self, call: CallbackQuery, state: FSMContext) -> None:
        await state.set_state(EditGift.dice)

        i = call.data.split(":")[-1]

        await state.update_data({"giftId": int(i)})

        await call.message.answer(
            text=self.s.lang.text["dice_value_need"],
            reply_markup=self.kb.gifts.dice_panel(callback="edit_gift_dice:{}")
        )