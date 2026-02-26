import os
from passlib.context import CryptContext
from datetime import timedelta, datetime, timezone
from dotenv import load_dotenv
from jose import jwt

pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto"

)

def hash_password(password: str):
    hashed_password = pwd_context.hash(password)
    return hashed_password

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict, expires_delta:timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


