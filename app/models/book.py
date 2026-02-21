from app.database import Base
from sqlalchemy import Integer, Numeric, String, Column, func, DateTime

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, index=True)
    author = Column(String(100), nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    year = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False,server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
