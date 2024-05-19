from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db_helper, Brand
from . import crud


async def brand_by_id(
    brand_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Brand:
    brand = await crud.get_brand(brand_id=brand_id, session=session)
    if brand is not None:
        return brand

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Brand {brand_id} not found!",
    )
