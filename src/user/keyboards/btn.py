from aiogram.types import InlineKeyboardButton

def btn(
        text: str, 
        **kargs
    ) -> InlineKeyboardButton:
        return InlineKeyboardButton(
            text=text,
            callback_data=kargs.get("callback", None),
            url=kargs.get("url", None)
        )