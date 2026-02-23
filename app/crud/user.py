from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password

def create_user(db:Session, user_data:UserCreate):
    hashed_password = hash_password(user_data.password)
    user = User(username=user_data.username, 
                email=user_data.email,
                password_hash=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_id(db:Session, user_id: int):
    return db.get(User, user_id)

def get_user_by_username(db:Session, username: str):
    return db.query(User).filter(User.username == username).first() 

def get_users(db:Session, skip: int = 0, limit: int = 100):
    return db.query(User).order_by(User.id).offset(skip).limit(limit).all()

def update_user(db:Session, user_id: int, update_data:UserUpdate):
    user = db.get(User, user_id)
    if not user:
        return None
    
    if update_data.username:
        user.username = update_data.username
    if update_data.email:
        user.email = update_data.email
    if update_data.password:
        user.password_hash = hash_password(update_data.password)

    db.commit()
    db.refresh(user)
    return user

def delete_user(db:Session, user_id: int):
    user = db.get(User, user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user
