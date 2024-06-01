from typing import List

class Character:
    def __init__(self, id: int, name: str, style: str):
        self.id = id
        self.name = name
        self.style = style

characters = [
    Character(id=1, name="Po", style="Panda Style"),
    Character(id=2, name="Shifu", style="Kung Fu"),
    Character(id=3, name="Tigress", style="Tiger Style"),
    Character(id=4, name="Master Oogway", style="Tai Chi"),
    Character(id=5, name="Monkey", style="Monkey Style"),
    Character(id=6, name="Crane", style="Crane Style"),
    Character(id=7, name="Viper", style="Viper Style"),
    Character(id=8, name="Mantis", style="Mantis Style"),
    Character(id=9, name="Tai Lung", style="Leopard Style"),
]
