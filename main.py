from fastapi import FastAPI, HTTPException
from typing import List
from app.schemas.character_schema import Character, CharacterCreate
from app.crud.character_crud import get_character, get_characters, create_character, update_character, delete_character

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Kung Fu Panda API!"}

@app.get("/characters/", response_model=List[Character])
def read_characters():
    return get_characters()

@app.get("/characters/{character_id}", response_model=Character)
def read_character(character_id: int):
    char = get_character(character_id)
    if char is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return char

@app.post("/characters/", response_model=Character)
def create_new_character(character: CharacterCreate):
    return create_character(character)

@app.put("/characters/{character_id}", response_model=Character)
def update_existing_character(character_id: int, character: CharacterCreate):
    char = update_character(character_id, character)
    if char is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return char

@app.delete("/characters/{character_id}", response_model=Character)
def delete_existing_character(character_id: int):
    char = delete_character(character_id)
    if char is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return char
