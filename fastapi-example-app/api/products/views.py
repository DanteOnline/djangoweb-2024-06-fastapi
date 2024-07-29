from dataclasses import dataclass
from fastapi import APIRouter, Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from .schemas import ProductCreate, ProductRead
from .crud import product_list, new_product

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@dataclass
class ProductDB:
    id: int
    name: str
    price: int


@router.get("/", response_model=list[ProductRead])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await product_list(session)


@router.get("/{product_id}/", response_model=ProductRead)
def get_product_by_id(product_id: int):
    return {
        "id": product_id,
        "name": f"abc-{product_id}",
        "price": product_id % 10 * 100,
        "internal-id": "qwerty",
    }


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductRead)
async def create_product(
        product_in: ProductCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await new_product(session, product_in)
    data = product_in.model_dump()
    data['id'] = 1
    return ProductRead(**data)
