from ....factory.session import Session
from ...keyboard import AdminKeyboards
from ...states import NewGift

from aiogram.types import Message
from aiogram.fsm.context import FSMContext

class AdminStatesHandler:
    def __init__(
        self,
        s: Session,
        kb: AdminKeyboards
    ) -> None:
        self.s = s
        self.kb = kb

    async def gift_title(self, msg: Message, state: FSMContext) -> None:
        if not msg.text:
            return
        
        if len(msg.text) > 64:
            return
        
        await state.update_data({"name": msg.text})

        await state.set_state(NewGift.desc)

        await msg.answer(
            text=self.s.lang.text["desc_need"],
            reply_markup=self.kb.nav.cancle()
        )

    async def gift_desc(self, msg: Message, state: FSMContext) -> None:
        if not msg.text:
            return
        
        if len(msg.text) > 512:
            return
        
        await state.update_data({"desc": msg.text})

        await state.set_state(NewGift.image)

        await msg.answer(
            text=self.s.lang.text["image_need"],
            reply_markup=self.kb.nav.cancle()
        )

    async def gift_image(self, msg: Message, state: FSMContext) -> None:
        if not msg.photo:
            return

        await state.update_data({"image": msg.photo[-1].file_id})

        await msg.answer(
            text=self.s.lang.text["dice_value_need"],
            reply_markup=self.kb.gifts.dice_panel()
        )

    async def edit_gift_title(self, msg: Message, state: FSMContext) -> None:
        if not msg.text:
            return
        
        data = await state.get_data()

        await state.clear()

        await self.s.db.edit.gift_title(
            giftId=data.get("giftId", None),
            value=msg.text
        )

        await msg.answer(
            text=self.s.lang.text["done"],
            reply_markup=self.kb.nav.back(callback="edit_gifts")
        )

    async def edit_gift_desc(self, msg: Message, state: FSMContext) -> None:
        if not msg.text:
            return
        
        data = await state.get_data()

        await state.clear()

        await self.s.db.edit.gift_desc(
            giftId=data.get("giftId", None),
            value=msg.text
        )

        await msg.answer(
            text=self.s.lang.text["done"],
            reply_markup=self.kb.nav.back(callback="edit_gifts")
        )

    async def edit_gift_image(self, msg: Message, state: FSMContext) -> None:
        if not msg.photo:
            return
        
        data = await state.get_data()

        await state.clear()

        await self.s.db.edit.gift_image(
            giftId=data.get("giftId", None),
            value=msg.photo[-1].file_id
        )

        await msg.answer(
            text=self.s.lang.text["done"],
            reply_markup=self.kb.nav.back(callback="edit_gifts")
        )