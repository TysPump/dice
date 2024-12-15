from aiogram import Router

from ..factory.shemas import Session
from ..user import UserRouter
from ..admin import AdminRouter

async def create_routers(s: Session) -> tuple[Router, Router]:
    return (
        UserRouter(s).r,
        AdminRouter(s).r
    )