from fastapi import APIRouter, HTTPException
from app.schemas.user_schemas import User
from app.services.user_services import create_user,login_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def add_user(user: User):

    new_user = create_user(user)

    if new_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "User created successfully",
        "user": new_user
    }

@router.post("/login")
def login(email: str, password: str):

    user = login_user(email, password)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful",
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        }
    }