from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Brand, BrandCreate
from core.database import db_helper

router = APIRouter(tags=["Brands"])


@router.get(path="/", response_model=list[Brand])
async def get_brands(session: AsyncSession = Depends(db_helper.session_dependency())):
    return await crud.get_brands(session=session)


@router.post(path="/", response_model=Brand)
async def create_brand(
    brand_in: BrandCreate,
    session: AsyncSession = Depends(db_helper.session_dependency()),
):
    return await crud.create_brand(brand_in=brand_in, session=session)


@router.get(path="/{brand_id}/", response_model=Brand)
async def get_brand(
    brand_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency()),
):
    brand = await crud.get_brand(brand_id=brand_id, session=session)
    if brand is not None:
        return brand

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Brand {brand_id} not found!",
    )
