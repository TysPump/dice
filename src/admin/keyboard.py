from ..factory.session import Session
from .keyboards import PanelKeyboard
from .keyboards import GiftsMenuKeyboard, NavigationKeyboards

class AdminKeyboards:
    def __init__(self, s: Session) -> None:
        self.s = s

        self.panel = PanelKeyboard(s=s)
        self.gifts = GiftsMenuKeyboard(s=s)
        self.nav = NavigationKeyboards(s=s)