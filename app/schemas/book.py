from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    year: int
    price: Decimal

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    price: Optional[Decimal] = None

class BookResponse(BookBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class BookInDB(BookResponse):
    pass
