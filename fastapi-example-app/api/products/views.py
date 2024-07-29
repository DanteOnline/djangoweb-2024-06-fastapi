from dataclasses import dataclass
from typing import Annotated

from fastapi import APIRouter
from fastapi import status
from fastapi import Body

from .schemas import ProductCreate, ProductRead

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@dataclass
class ProductDB:
    id: int
    name: str
    price: int


@router.get("/")
def get_products():
    return {
        "data": [
            {"id": 1, "name": "Foo"},
            {"id": 2, "name": "Bar"},
            {"id": 3, "name": "Spam"},
        ],
    }


@router.get("/{product_id}/", response_model=ProductRead)
def get_product_by_id(product_id: int):
    # return ProductRead(
    #     id=product_id,
    #     name="Foo",
    #     price=1233,
    # )
    # return ProductDB(
    #     id=product_id,
    #     name=f"abc-{product_id}",
    #     price=product_id % 10 * 100,
    # )
    return {
        "id": product_id,
        "name": f"abc-{product_id}",
        "price": product_id % 10 * 100,
        "internal-id": "qwerty",
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(product_in: ProductCreate):
    return {
        "data": {
            "id": 0,
            "name": product_in.name,
            "price": product_in.price,
        }
    }
