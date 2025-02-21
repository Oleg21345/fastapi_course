from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Annotated, Optional

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class TaskOrm(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str]
    disc: Mapped[Optional[str]]













