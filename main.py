import asyncio
import logging

from src.factory import create_session, create_routers

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    logger = logging.getLogger(__name__)

    s = await create_session(logger=logger)

    await s.db._create_tables()

    routers = await create_routers(s)

    bot = Bot(
        token=s.config.token,
        default=DefaultBotProperties(
            parse_mode="HTML"
        ) 
    )

    dp = Dispatcher()

    dp.include_routers(
        *routers
    )

    await dp.start_polling(
        bot
    )

if __name__ == "__main__":
    asyncio.run(main())