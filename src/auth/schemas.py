from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    username: str
    password: str
