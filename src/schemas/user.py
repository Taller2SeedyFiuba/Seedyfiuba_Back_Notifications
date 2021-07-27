from pydantic import BaseModel

class UserBase(BaseModel):
    id: str


class UserOut(UserBase):
    class Config:
        orm_mode = True
    pass


class User(UserBase):
    token: str

    class Config:
        orm_mode = True
