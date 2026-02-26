from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.books import router as books_router
from app.database import Base, engine

app = FastAPI(
        title="Book Store API",
        description="API for book store with registration, roles and JWT",
        version="1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(books_router)


