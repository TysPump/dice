from aiogram.types import Message
from aiogram.filters import CommandObject

from ....factory.session import Session
from ....factory.media import create_media
from ....database.tables import User
from ...keyboard import UserKeyboards

from datetime import datetime

class Welcome:
    def __init__(self, s: Session, kb: UserKeyboards):
        self.s = s

        self.kb = kb

        self.logo_uri = None

    def _date(self) -> float:
        return datetime.now().timestamp()

    async def _write_user(self, msg: Message) -> None:
        exist = await self.s.db.fetch.user(chat_id=msg.from_user.id)
        if exist:
            return False
        
        await self.s.db.add.user(
            data=User(
                **{
                    "chatId": msg.from_user.id,
                    "username": msg.from_user.username if msg.from_user.username else "user",
                    "firstName": msg.from_user.first_name,
                    "isPremium": msg.from_user.is_premium,
                    "date":  self._date()
                }
            )
        )

        self.s.logger.info("New user [ %d ]", msg.from_user.id)

        return True
    
    async def _answer(self, msg: Message) -> None:
        if self.s.config.media.logo:
            animation = create_media(
                static=self.s.config.media.logo,
                filename="logo"
            ) if self.logo_uri is None else self.logo_uri

            msgg = await msg.answer_animation(
                caption=self.s.lang.text["welcome"],
                animation=animation,
                duration=3,
                width=800,
                height=800,
                reply_markup=self.kb.welcome.main_menu()
            )
            
            self.logo_uri = msgg.animation.file_id
            
            return
        
        await msg.answer(
            text=self.s.lang.text["welcome"],
            reply_markup=self.kb.welcome.main_menu()
        )

    async def start(
        self,
        msg: Message, 
        **kargs
    ) -> None:
        cmd: CommandObject = kargs.get("command", None)

        if cmd:
            if cmd.args:
                self.s.logger.info("DeepLink [ %d ] value: [ %s ]", msg.from_user.id, cmd.args)

        try:
            await self._write_user(msg=msg)
        finally:
            await self._answer(msg=msg)