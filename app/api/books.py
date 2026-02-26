from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session 
from app.database import get_db
from app.crud.book import create_book, get_book_by_id, get_books, update_book, delete_book
from app.schemas.book import BookCreate, BookUpdate, BookResponse
from app.api.deps import get_current_user, get_current_admin

router = APIRouter(
        prefix="/books",
        tags=["books"]
)

@router.get("/", response_model=list[BookResponse])
def read_books(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user),
):
    return get_books(db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=BookResponse)
def read_book(
        book_id: int,
        db: Session = Depends(get_db),
        current_user = Depends(get_current_user),
):
    book = get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found",
        )

    return book

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_new_book(
        book_data: BookCreate,
        db: Session = Depends(get_db),
        current_admin=Depends(get_current_admin),
):
    return create_book(db, book_data)

@router.put("/{book_id}", response_model=BookResponse)
def update_existing_book(
        book_id: int,
        update_data: BookUpdate,
        db: Session = Depends(get_db),
        current_admin=Depends(get_current_admin),
):
    book = update_book(db, book_id, update_data)

    if not book:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
        )

    return book

@router.delete("/{book_id}", response_model=BookResponse)
def delete_existing_book(
        book_id: int,
        db: Session = Depends(get_db),
        current_admin=Depends(get_current_admin),
):
    book = delete_book(db, book_id)

    if not book:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found"
        )

    return book














