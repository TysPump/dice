from typing import List, Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import select, update, delete

from .base import Base
from .tables import Gift, Inventory, User, Data

class DatabaseApi:
    def __init__(self):
        self.engine = create_async_engine(url="sqlite+aiosqlite:///db.db")

        self.session = async_sessionmaker(self.engine, expire_on_commit=False)

        self.add = Add(session=self.session)
        self.remove = Remove(session=self.session)
        self.fetch = Fetch(session=self.session)
        self.edit = Edit(session=self.session)

    async def _create_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

class Edit:
    def __init__(self, session: async_sessionmaker[AsyncSession]) -> None:
        self.session = session

    async def gift_title(
        self,
        giftId: int,
        value: str
    ) -> None:
        async with self.session() as s:
            query = update(Gift).where(Gift.id==giftId).values(name=value)

            await s.execute(query)
            await s.commit()

    async def gift_desc(
        self,
        giftId: int,
        value: str
    ) -> None:
        async with self.session() as s:
            query = update(Gift).where(Gift.id==giftId).values(desc=value)

            await s.execute(query)
            await s.commit()

    async def gift_image(
        self,
        giftId: int,
        value: str
    ) -> None:
        async with self.session() as s:
            query = update(Gift).where(Gift.id==giftId).values(image=value)

            await s.execute(query)
            await s.commit()

    async def gift_dice(
        self,
        giftId: int,
        value: int
    ) -> None:
        async with self.session() as s:
            query = update(Gift).where(Gift.id==giftId).values(dicePosition=value)

            await s.execute(query)
            await s.commit()

    async def data(
        self,
        type_: str,
        value: str
    ) -> None:
        async with self.session() as s:
            query = update(Data).where(Data.type_ == type_).values(value=value)

            await s.execute(query)
            await s.commit()

class Add:
    def __init__(self, session: async_sessionmaker[AsyncSession]) -> None:
        self.session = session

    async def user(
        self, 
        data: User
    ) -> None:
        async with self.session() as s:
            s.add(data)

            await s.flush()
            await s.commit()

    async def gift(
        self, 
        data: Gift
    ) -> None:
        async with self.session() as s:
            s.add(data)

            await s.flush()
            await s.commit()

    async def inventory(
        self,
        data: Inventory
    ) -> None:
        async with self.session() as s:
            s.add(data)

            await s.flush()
            await s.commit()

    async def data(
        self,
        data: Data
    ) -> None:
        async with self.session() as s:
            s.add(data)

            await s.flush()
            await s.commit()
    
class Fetch:
    def __init__(self, session: async_sessionmaker[AsyncSession]) -> None:
        self.session = session

    async def user(
        self, 
        chat_id: int
    ) -> User | None:
        async with self.session() as s:
            query = select(User).where(User.chatId == chat_id)

            try:
                result = await s.execute(query)
                return result.scalars().one()
            except:
                return None
        
    async def gift(
        self,
        id_: Optional[int] = None,
        dice_value: Optional[int] = None
    ) -> List[Gift]:
        async with self.session() as s:
            query = select(Gift)
            if id_:
                query = query.where(Gift.id == id_)
            else:
                query = query.where(Gift.dicePosition == dice_value)

            try:
                result = await s.execute(query)
                return result.scalars().all()
            except:
                return []
            
    async def gifts(
        self
    ) -> List[Gift]:
        async with self.session() as s:
            query = select(Gift)

            try:
                result = await s.execute(query)
                return result.scalars().all()
            except Exception as e:
                return []
        
    async def inventory(
        self,
        chatId: int
    ) -> List[Inventory]:
        async with self.session() as s:
            query = select(Inventory).where(Inventory.ownerId == chatId)

            try:
                result = await s.execute(query)
                return result.scalars().all()
            except:
                return None
            
    async def data(
        self,
        type_: str
    ) -> Data:
        async with self.session() as s:
            query = select(Data).where(Data.type_ == type_)

            try:
                result = await s.execute(query)
                return result.scalars().one()
            except:
                return None
            
class Remove:
    def __init__(self, session: async_sessionmaker[AsyncSession]):
        self.session = session

    async def gift(
        self,
        id_: int
    ) -> None:
        async with self.session() as s:
            query = delete(Gift).where(Gift.id == id_)

            await s.execute(query)
            await s.commit()