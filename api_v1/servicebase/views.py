from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Brand, BrandCreate, BrandUpdate
from core.database import db_helper
from .dependencies import brand_by_id

router = APIRouter(tags=["Brands"])


@router.get(path="/", response_model=list[Brand])
async def get_brands(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_brands(session=session)


@router.post(path="/", response_model=Brand)
async def create_brand(
    brand_in: BrandCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_brand(brand_in=brand_in, session=session)


@router.get(path="/{brand_id}/", response_model=Brand)
async def get_brand(
    brand: Brand = Depends(brand_by_id),
):
    return brand


@router.put(path="/{brand_id}/")
async def update_brand(
    brand_update: BrandUpdate,
    brand: Brand = Depends(brand_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_brand(
        session=session,
        brand=brand,
        brand_update=brand_update,
    )
