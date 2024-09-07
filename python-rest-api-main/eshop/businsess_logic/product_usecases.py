from typing import Optional, List
from .product import Product
import uuid

products_db = []  # Простая база данных в памяти

def product_create(dto) -> Product:
    product = Product(
        id=str(uuid.uuid4()),
        name=dto['name'],
        price=dto['price']
    )
    products_db.append(product)
    return product

def product_get_many(page: int, limit: int) -> List[Product]:
    start = page * limit
    end = start + limit
    return products_db[start:end]

def product_get_by_id(id: str) -> Optional[Product]:
    for product in products_db:
        if product.id == id:
            return product
    return None
