from AdventureGame.game_files.actions.Move import Move
from AdventureGame.game_files.locations.Location import Location

class Alleyway(Location):
    def __init__(self):
        self.long_description = """You walk down the alleyway, taking each step slowly."""
        self.characters = []
        self.choices: dict[str, Action] = {}
        super().__init__(self.long_description, self.characters, self.choices)

    def set_as_active(self):
        from AdventureGame.game_files.locations.NewGameStart import NewGameStart
        back_to_start: Action = Move(new_location=NewGameStart())
        choices: dict[str, Action] = {
            "Return to roadway.": back_to_start
        }
        self.choices = choices
