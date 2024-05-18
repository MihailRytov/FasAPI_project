from pydantic import BaseModel, ConfigDict


class BrandBase(BaseModel):
    title: str


class BrandCreate(BrandBase):
    pass


class Brand(BrandBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
