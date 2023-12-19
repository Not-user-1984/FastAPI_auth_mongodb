import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase
from pydantic import EmailStr, Field

from src.config import settings

DATABASE_URL = settings.DATABASE_URL
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client["database_name"]


class User(BeanieBaseUser, Document):
    name: str = Field(...)
    phone: str = Field(...)
    email: EmailStr = Field(..., unique=True)
    site: str = Field(...)
    hashed_password: str = Field(..., description="Hashed password")

    class Meta:
        collection = "users"


async def get_user_db():
    yield BeanieUserDatabase(User)
