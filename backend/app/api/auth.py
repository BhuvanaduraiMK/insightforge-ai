from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.security import get_current_token
from app.core.security import get_current_user
from app.models.user import User
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
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Login user and return JWT access token.
    """
    try:
        return login_user(
            db=db,
            email=form_data.username,
            password=form_data.password,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )

@router.get("/token-test")
def token_test(
    token: str = Depends(get_current_token)
):
    return {
        "received_token": token
    }


@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(get_current_user)
):
    """
    Return the currently authenticated user.
    """
    return current_user