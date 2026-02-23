from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate

def create_book(db:Session, book_data:BookCreate):
    book = Book(title=book_data.title,
                author=book_data.author,
                year=book_data.year,
                price=book_data.price)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_book_by_id(db:Session, book_id: int):
    return db.get(Book, book_id)

def get_books(db:Session, skip: int = 0, limit:int = 100):
    return db.query(Book).order_by(Book.id).offset(skip).limit(limit).all()

def update_book(db:Session, book_id:int, update_data:BookUpdate):
    book = db.get(Book, book_id)
    if not book:
        return None
    if update_data.title:
        book.title = update_data.title
    if update_data.year:
        book.year = update_data.year
    if update_data.author:
        book.author = update_data.author
    if update_data.price is not None:
        book.price = update_data.price
    db.commit()
    db.refresh(book)
    return book

def delete_book(db:Session, book_id:int):
    book = db.get(Book, book_id)
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book
