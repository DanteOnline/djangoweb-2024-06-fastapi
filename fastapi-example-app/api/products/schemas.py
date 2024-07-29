from typing import Annotated

from annotated_types import Ge, Lt
from pydantic import BaseModel
from pydantic import Field
from pydantic import ConfigDict


class ProductBase(BaseModel):
    name: str
    price: int


class ProductCreate(ProductBase):
    price: Annotated[int, Ge(1), Lt(1_000_000)]


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(json_schema_extra={"example": 42})
    price: int = Field(json_schema_extra={"example": 100})


# class ProductReadResponse(BaseModel):
#     data: ProductRead
