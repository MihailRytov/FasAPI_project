from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.servicebase.schemas import BrandCreate
from core.database import Brand
from sqlalchemy.engine import Result


async def get_brands(session: AsyncSession) -> list[Brand]:
    stmt = select(Brand).order_by(Brand.id)
    result: Result = await session.execute(stmt)
    brands = result.scalars().all()
    return list(brands)


async def get_brand(session: AsyncSession, brand_id: int) -> Brand | None:
    return await session.get(Brand, brand_id)


async def create_brand(session: AsyncSession, brand_in: BrandCreate) -> Brand:
    """
    Передаем параметры которые пришли в brand_id
    Через model_dump() превращаем в словарь
    Через ** разбираем на отдельные аргументы (**kwargs)
    """
    brand = Brand(**brand_in.model_dump())

    """
    Добавляем в сессию это объект для отслеживания
    """
    session.add(brand)
    """
    Сохраняем в БД.
    """
    await session.commit()
    """
    Иногда может понадобиться обновить объект перед
    тем как его возвращать.
    """
    # await session.refresh(brand)
    return brand
