from pydantic import BaseModel

class CharacterBase(BaseModel):
    name: str
    style: str

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    id: int

    class Config:
        orm_mode = True
