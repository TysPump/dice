from aiogram import Router, F
from aiogram.filters import CommandStart

from ..factory.routers import Session
from .handlers import Welcome
from .keyboard import UserKeyboards
from .callback import UserCallbackFactory

class UserRouter:
    def __init__(
        self, 
        s: Session
    ) -> None:
        self.r = Router()

        self.kb = UserKeyboards(s=s)

        self.w = Welcome(s=s, kb=self.kb)
        self.callback = UserCallbackFactory(s=s, kb=self.kb)

        self.r.message.register(self.w.start, CommandStart())

        self.r.callback_query.register(self.callback.dice.dice_menu, F.data=="gifts")
        self.r.callback_query.register(self.callback.dice.send_dice, F.data=="spin_dice")
        self.r.callback_query.register(self.callback.contacts.contacts, F.data=="contacts")

        self.r.callback_query.register(self.callback.menu.main_menu, F.data=="main_menu")



        

