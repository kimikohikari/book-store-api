from app.database import engine, Base
from app.models.user import User
from app.models.book import Book

Base.metadata.create_all(bind=engine)
