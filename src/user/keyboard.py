from ..factory.shemas import Session
from .keyboards import WelcomeKeyboard, DiceMenuKeyboard, NavigationKeyboards

class UserKeyboards:
    def __init__(self, s: Session):
        self.welcome = WelcomeKeyboard(s=s)

        self.dice = DiceMenuKeyboard(s=s)

        self.nav = NavigationKeyboards(s=s)