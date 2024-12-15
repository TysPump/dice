from ..factory.session import Session
from .keyboard import UserKeyboards
from .handlers.callbacks import DiceMenu
from .handlers.callbacks import ContactsMenu, UserMainMenu

class UserCallbackFactory:
    def __init__(self, s: Session, kb: UserKeyboards) -> None:
        self.dice = DiceMenu(s=s, kb=kb)
        self.contacts = ContactsMenu(s=s, kb=kb)
        self.menu = UserMainMenu(s=s, kb=kb)