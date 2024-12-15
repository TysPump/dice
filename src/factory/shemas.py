"""
Pydantic models for bot session.

Don't edit.
"""

from logging import Logger
from pydantic import BaseModel, ConfigDict

from typing import Dict, List, Optional
from ..database import DatabaseApi

class Media(BaseModel):
    logo: Optional[str] = None
    dice: Optional[str] = None

class Config(BaseModel):
    media: Media
    infoUrl: str
    admins: List[int]
    adminChannelId: int
    token: str

class Lang(BaseModel):
    """The simplest language model.
    
    Provides access to the localization file and access to text by json keys.
    """
    button: Dict[str, str]
    text: Dict[str, str]

class Session(BaseModel):
    """The bot session model, provides access to the necessary classes and links all bot modules."""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    db: DatabaseApi
    lang: Lang
    logger: Logger = None
    config: Config