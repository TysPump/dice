from ..factory.session import Session
from .keyboard import AdminKeyboards
from .handlers.callbacks import GiftsPanel, AdminPanel

class AdminCallbacks:
    def __init__(self, s: Session, kb: AdminKeyboards):
        self.s = s
        self.kb = kb

        self.gifts = GiftsPanel(s=s, kb=kb)
        self.panel = AdminPanel(s=s, kb=self.kb)