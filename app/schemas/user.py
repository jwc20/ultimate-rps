from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    disabled: bool


class UserUpdate(BaseModel):
    disabled: bool | None = None
    password: str | None = None