import asyncio

from datetime import datetime
from typing import List

from aiogram.types import CallbackQuery
from aiogram.utils.media_group import MediaGroupBuilder

from ....database.tables import Gift, Inventory
from ....factory.session import Session
from ....factory.media import create_media
from ...keyboard import UserKeyboards

class DiceMenu:
    def __init__(self, s: Session, kb: UserKeyboards) -> None:
        self.s = s

        self.kb = kb

    def _date(self) -> float:
        return datetime.now().timestamp()

    async def _answer(
        self, 
        call: CallbackQuery, 
        **kargs
    ) -> None:

        await call.message.delete()

        await call.message.answer(
            text=kargs.get("text", ""),
            reply_markup=kargs.get("reply_markup", None)
        )

    async def _inventory(self, inventory: List[Inventory]):
        gifts: List[Gift] = []

        for item in inventory:
            gift = await self.s.db.fetch.gift(id_=item.giftId)

            gifts.append(gift[0])

        text = self.s.lang.text["inventory"].format(", ".join([gift.name for gift in gifts]))
        reply_markup=self.kb.nav.menu()

        return text, reply_markup
    
    async def _create_gifts_text(
        self
    ) -> str:
        gifts = await self.s.db.fetch.gifts()

        text = ""

        for gift in gifts:
            text += "\n{} - {}".format(
                self.s.lang.button[str(gift.dicePosition)],
                gift.name
            )

        return text

    async def dice_menu(self, call: CallbackQuery) -> None:
        gifts_caption = await self._create_gifts_text()
        
        text=self.s.lang.text["bonus_menu"].format(gifts_caption)
        reply_markup=self.kb.dice.spin_menu()

        inventory = await self.s.db.fetch.inventory(chatId=call.from_user.id)

        if inventory:
            text, reply_markup = await self._inventory(inventory=inventory)

        await self._answer(
            call=call, 
            delete=True if self.s.config.media.dice else False,
            text=text,
            reply_markup=reply_markup,
            static=self.s.config.media.dice
        )

    def _create_media_group(self, gifts: List[Gift], caption: str):
        media_group = MediaGroupBuilder()

        for gift in gifts:
            media_group.add_photo(
                media=gift.image,
                caption=caption if caption else None
            )

            caption = None

        return media_group

    async def send_dice(self, call: CallbackQuery) -> None:
        inventory = await self.s.db.fetch.inventory(chatId=call.from_user.id)

        conditions = await self.s.db.fetch.data(type_="conditions")

        if inventory:
            text, reply_markup = await self._inventory(inventory=inventory)
            if call.message.photo:
                await call.message.edit_caption(
                    reply_markup=reply_markup,
                    caption=text
                )
            else:
                await call.message.edit_text(
                    reply_markup=reply_markup,
                    caption=text
                )
            return
        
        dice_message = await call.message.bot.send_dice(chat_id=call.from_user.id)

        gifts = await self.s.db.fetch.gift(dice_value=dice_message.dice.value)

        for gift in gifts:
            await self.s.db.add.inventory(
                data=Inventory(
                    **{
                        "ownerId": call.from_user.id,
                        "giftId": gift.id,
                        "date": self._date()
                    }
                )
            )

        await asyncio.sleep(4)

        if len(gifts) == 1:
            desc = "\n\n {}".format(gifts[0].desc)
            await call.message.answer_photo(
                caption=self.s.lang.text["gift"].format(gifts[0].name, desc, conditions.value if conditions else "Условия"),
                photo=gifts[0].image,
                reply_markup=self.kb.nav.menu()
            )

            date = datetime.now()
            date = date.strftime("%d/%m/%Y, %H:%M:%S")

            await call.message.bot.send_photo(
                caption=self.s.lang.text["channel_msg"].format(gifts[0].name, call.from_user.username, call.from_user.first_name, call.from_user.id, date),
                photo=gifts[0].image,
                chat_id=self.s.config.adminChannelId
            )
        elif len(gifts) == 0:
            await call.message.answer(
                text=self.s.lang.text["gift"].format("Ничего :(", "", "")
            )
        else:
            desc = "\n\n".join([gift.desc for gift in gifts])
            caption = self.s.lang.text["gift"].format(", ".join([gift.name for gift in gifts]), desc, conditions.value if conditions else "Условия")
            await call.message.answer_media_group(
                media=self._create_media_group(gifts=gifts, caption=caption).build()
            )

            date = datetime.now()
            date = date.strftime("%d/%m/%Y, %H:%M:%S")

            caption = self.s.lang.text["channel_msg"].format(", ".join([gift.name for gift in gifts]), call.from_user.username, call.from_user.first_name, call.from_user.id, date)

            await call.message.bot.send_media_group(
                media=self._create_media_group(gifts=gifts, caption=caption).build(),
                chat_id=self.s.config.adminChannelId
            )