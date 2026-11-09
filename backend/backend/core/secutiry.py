import hashlib
import secrets
import string
from datetime import datetime, timedelta
from uuid import UUID
from fastapi import HTTPException
from jose import jwt, JWTError
from argon2 import PasswordHasher
from password_validator import PasswordValidator
from starlette import status

password_schema = PasswordValidator(
)

password_schema.min(8).max(256).digits().uppercase().lowercase().symbols()

ph = PasswordHasher()

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return ph.verify(password, hashed_password)


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

def decode_access_token(token: str) -> UUID:
    try:
        payload = jwt.decode(token,
                             key="",
                             algorithms=['HS256']
                             )
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials",)
    user_id = payload.get('sub')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials")
    return UUID(user_id)


#Refresh
def hash_refresh_token(refresh_token: str) -> str:
    hashed_token = hashlib.sha256(refresh_token.encode('utf-8')).hexdigest()
    return hashed_token

def generate_refresh_token():
    token = secrets.token_urlsafe(32)
    hashed_token = hash_refresh_token(token)
    return token, hashed_token


def generate_strong_password(length=12):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов, чтобы вместить все категории.")

    # Определяем наборы символов
    lowercase = string.ascii_lowercase # a-z
    uppercase = string.ascii_uppercase # A-Z
    digits = string.digits
    punctuation = string.punctuation

    # Гарантируем наличие обязательных символов
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]

    # Заполняем оставшуюся длину случайными символами из всех доступных категорий
    all_characters = lowercase + uppercase + digits + punctuation
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_characters))

    # Перемешиваем символы, чтобы обязательные не всегда шли в начале
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)
