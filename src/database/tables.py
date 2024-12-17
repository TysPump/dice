from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    chatId: Mapped[int] = mapped_column(index=True, unique=True)
    username: Mapped[str]
    firstName: Mapped[str]
    isPremium: Mapped[bool]
    date: Mapped[float]

class Gift(Base):
    __tablename__ = "Gifts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    desc: Mapped[str]
    date: Mapped[float]
    dicePosition: Mapped[int] = mapped_column(index=True)
    image: Mapped[str]

class Inventory(Base):
    __tablename__ = "Inventory"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ownerId: Mapped[int] = mapped_column(index=True)
    giftId: Mapped[int]
    date: Mapped[float]

class Data(Base):
    __tablename__ = "Data"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type_: Mapped[str]
    value: Mapped[str]