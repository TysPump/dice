from aiogram import Router, F
from aiogram.filters import Command

from ..factory.routers import Session
from .keyboard import AdminKeyboards
from .handlers.messages import Panel
from .handlers.states import AdminStatesHandler
from .callback import AdminCallbacks
from .states import NewGift, EditGift, StateEdit

class AdminRouter:
    def __init__(
        self, 
        s: Session
    ) -> None:
        self.r = Router()

        self.kb = AdminKeyboards(s=s)

        self.panel = Panel(s=s, kb=self.kb)
        self.callback = AdminCallbacks(s=s, kb=self.kb)
        self.states = AdminStatesHandler(s=s, kb=self.kb)

        self.r.message.register(self.panel.panel_menu, Command(commands=["admin"]))

        self.r.callback_query.register(self.callback.gifts.gifts_menu, F.data=="edit_gifts")
        self.r.callback_query.register(self.callback.gifts.new_gift, F.data=="new_gift")
        self.r.callback_query.register(self.callback.gifts.write_new_gift, F.data.startswith("add_value_to_gift:"))
        self.r.callback_query.register(self.callback.gifts.gift_menu, F.data.startswith("gift:"))
        self.r.callback_query.register(self.callback.gifts.delete, F.data.startswith("gift_delete:"))
        self.r.callback_query.register(self.callback.gifts.edit, F.data.startswith("gift_edit:"))

        self.r.callback_query.register(self.callback.gifts.edit_title, F.data.startswith("gift_title_edit:"))
        self.r.callback_query.register(self.callback.gifts.edit_desc, F.data.startswith("gift_desc_edit:"))
        self.r.callback_query.register(self.callback.gifts.edit_image, F.data.startswith("gift_image_edit:"))
        self.r.callback_query.register(self.callback.gifts.edit_dice, F.data.startswith("gift_dice_edit:"))

        self.r.callback_query.register(self.callback.edit.contacts, F.data=="edit_contacts")
        self.r.callback_query.register(self.callback.edit.conditions, F.data=="edit_conditions")

        self.r.callback_query.register(self.callback.panel.close, F.data=="close")
        self.r.callback_query.register(self.callback.panel.admin_panel, F.data=="admin_panel")

        self.r.message.register(self.states.gift_title, NewGift.title)
        self.r.message.register(self.states.gift_desc, NewGift.desc)
        self.r.message.register(self.states.gift_image, NewGift.image)

        self.r.message.register(self.states.edit_gift_title, EditGift.title)
        self.r.message.register(self.states.edit_gift_desc, EditGift.desc)
        self.r.message.register(self.states.edit_gift_image, EditGift.image)
        # self.r.message.register(self.states.edit_gift_dice, EditGift.dice)

        self.r.message.register(self.states.edit_data_value, StateEdit.value)