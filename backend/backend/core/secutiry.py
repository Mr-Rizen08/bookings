import hashlib
import secrets
from datetime import datetime, timedelta
from uuid import UUID
from jose import jwt
from passlib.handlers.argon2 import argon2
from password_validator import PasswordValidator

password_schema = PasswordValidator(
)

password_schema.min(8).max(256).digits().uppercase().lowercase().symbols()

def hash_password(password: str) -> str:
    return argon2.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return argon2.verify(password, hashed_password)


#Access
def encode_access_token(user_id: UUID) -> str:
    now = datetime.now()
    payload = {
        'exp': now + timedelta(minutes=60),
        'iat': now,
        'sub': str(user_id)
    }

    return jwt.encode(
        payload,
        key="",
        algorithm='HS256'
    )

def decode_refresh_token(token: str) -> UUID:
    pass


#Refresh

def hash_refresh_token(refresh_token: str) -> str:
    hashed_token = hashlib.sha256(refresh_token.encode('utf-8')).hexdigest()
    return hashed_token

def generate_refresh_token():
    token = secrets.token_urlsafe(32)
    hashed_token = hash_refresh_token(token)
    return token