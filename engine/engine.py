"""Core classes for the TexAdvent engine."""

from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Location:
    name: str
    description: str
    exits: Dict[str, str] = field(default_factory=dict)
    items: List[str] = field(default_factory=list)

@dataclass
class Player:
    location: Location
    inventory: List[str] = field(default_factory=list)

class GameEngine:
    """Very small stub of the main game engine."""

    def __init__(self, starting_location: Location):
        self.player = Player(location=starting_location)

    def run(self):
        print(f"Starting game in {self.player.location.name}")
        print(self.player.location.description)
        # Stub loop
        print("Game engine stub running. Implement game logic here.")
