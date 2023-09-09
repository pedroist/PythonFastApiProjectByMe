from fastapi import APIRouter
from pydantic import BaseModel

from app.models import Users

router = APIRouter()


class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str


@router.post("/auth")
async def create_user(user: CreateUserRequest):
    create_user_model = Users(
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=user.password,
        role=user.role,
    )

    return create_user_model
