from AdventureGame.utils.UserInput import UserInput
from AdventureGame.game_files.characters.Character import Character
from AdventureGame.game_files.story.Choices import Choices

class Area:
    def __init__(self, description: str):
        self.visited = False
        self.short_description: str = description
        self.long_description: str = description