from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.servicebase.schemas import BrandCreate, BrandUpdate, BrandUpdatePartial
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


"""
Обновляем (вносим изменение в текущую запись в БД
"""
#
#
# async def update_brand(
#     session: AsyncSession,
#     brand: Brand,
#     brand_update: BrandUpdate,
# ) -> Brand:
#     for name, value in brand_update.model_dump().items():
#         setattr(brand, name, value)
#     await session.commit()
#     return brand


"""
Вносим частичные изменения в запись. В случае таблицы brands
данная функция будет полностью копировать предыдущую т.к. имеем только одно поле.
"""


async def update_brand(
    session: AsyncSession,
    brand: Brand,
    brand_update: BrandUpdate | BrandUpdatePartial,
    partial: bool = False,
) -> Brand:
    for name, value in brand_update.model_dump(exclude_unset=partial).items():
        setattr(brand, name, value)
    await session.commit()
    return brand


async def delete_brand(
    session: AsyncSession,
    brand: Brand,
) -> None:
    await session.delete(brand)
    await session.commit()
