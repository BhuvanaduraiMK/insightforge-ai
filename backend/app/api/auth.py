from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
)
from app.services.auth_service import (
    register_user,
    login_user,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Register a new user.
    """
    try:
        return register_user(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    """
    Login user and return JWT access token.
    """
    try:
        return login_user(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )