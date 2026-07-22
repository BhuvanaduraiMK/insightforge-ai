from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin


def register_user(db: Session, user: UserCreate):
    """
    Register a new user after checking email uniqueness
    and hashing the password.
    """
    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        raise ValueError("Email already registered")

    hashed_password = hash_password(user.password)

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(
    db: Session,
    email: str,
    password: str,
):
    """
    Authenticate a user and return a JWT access token.
    """

    db_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not db_user:
        raise ValueError("Invalid email or password")

    if not verify_password(
        password,
        db_user.password
    ):
        raise ValueError("Invalid email or password")

    access_token = create_access_token(
        data={
            "sub": db_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }