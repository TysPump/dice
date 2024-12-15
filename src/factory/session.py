from typing import Dict, List
from .shemas import (
    Config,
    Session,
    Lang
)

from ..database import DatabaseApi
from ..utils import config, lang

def _get_config() -> Dict:
    return config(path="config.json")

def _get_lang() -> Dict[str, Dict[str, str]]:
    return lang()

async def create_session(**kargs) -> Session:
    """Метод возвращает модель сессии."""
    return Session(
        db=DatabaseApi(), 
        lang=Lang(
            button=_get_lang().get("button", {}),
            text=_get_lang().get("text", {})
        ),
        logger=kargs.get("logger", None),
        config=Config(**_get_config())
    )