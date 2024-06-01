from typing import List, Optional
from app.models.character_model import Character, characters
from app.schemas.character_schema import CharacterCreate

def get_character(character_id: int) -> Optional[Character]:
    return next((char for char in characters if char.id == character_id), None)

def get_characters() -> List[Character]:
    return characters

def create_character(character: CharacterCreate) -> Character:
    new_id = max(char.id for char in characters) + 1 if characters else 1
    new_character = Character(id=new_id, **character.dict())
    characters.append(new_character)
    return new_character

def update_character(character_id: int, character: CharacterCreate) -> Optional[Character]:
    char = get_character(character_id)
    if char:
        char.name = character.name
        char.style = character.style
    return char

def delete_character(character_id: int) -> Optional[Character]:
    char = get_character(character_id)
    if char:
        characters.remove(char)
    return char
