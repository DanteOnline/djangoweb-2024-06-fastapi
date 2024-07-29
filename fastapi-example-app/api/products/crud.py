from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from .schemas import ProductCreate


async def product_list(session: AsyncSession) -> list[Product]:
    return []


async def new_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    return None
