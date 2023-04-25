from pydantic import BaseModel

from sql.models import Selected


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    enabled: bool
    selected: list[Selected] = []

    class Config:
        orm_mode = True
