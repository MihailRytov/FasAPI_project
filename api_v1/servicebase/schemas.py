from pydantic import BaseModel, ConfigDict


class BrandBase(BaseModel):
    title: str


class Brand(BrandBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class BrandCreate(BrandBase):
    pass


class BrandUpdate(BrandCreate):
    pass


class BrandUpdatePartial(BrandCreate):
    title: str | None = None


# test:int = BrandCreate.
