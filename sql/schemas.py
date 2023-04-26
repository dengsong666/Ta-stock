from pydantic import BaseModel

from sql.models import Selected


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    enabled: bool
    selected: list[Selected] = []

    class Config:
        # arbitrary_types_allowed = True
        orm_mode = True


class SelectedBase(BaseModel):
    name: str
    source: str


class Selected(SelectedBase):
    id: int

    class Config:
        orm_mode = True
