from aiogram.types import CallbackQuery

from ....factory.media import create_media
from ....factory.session import Session
from ...keyboard import UserKeyboards

class UserMainMenu:
    def __init__(self, s: Session, kb: UserKeyboards):
        self.s = s
        self.kb = kb

        self.logo_uri = None

    async def main_menu(self, call: CallbackQuery) -> None:
        await call.message.delete()
        
        if self.s.config.media.logo:
            animation = create_media(
                static=self.s.config.media.logo,
                filename="logo"
            ) if self.logo_uri is None else self.logo_uri

            try:
                msgg = await call.message.answer_animation(
                    caption=self.s.lang.text["welcome"],
                    animation=animation,
                    duration=3,
                    width=800,
                    height=800,
                    reply_markup=self.kb.welcome.main_menu()
                )
            
                self.logo_uri = msgg.animation.file_id
            except:
                msgg = await call.message.answer_animation(
                    caption=self.s.lang.text["welcome"],
                    animation=create_media(
                        static=self.s.config.media.logo,
                        filename="logo"
                    ),
                    duration=3,
                    width=800,
                    height=800,
                    reply_markup=self.kb.welcome.main_menu()
                )

                self.logo_uri = msgg.animation.file_id
            
            return
        
        await call.message.answer(
            text=self.s.lang.text["welcome"],
            reply_markup=self.kb.welcome.main_menu()
        )
    