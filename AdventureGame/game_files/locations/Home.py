from AdventureGame.game_files.actions.Move import Move
from AdventureGame.game_files.locations.Location import Location
from AdventureGame.game_files.locations.Alleyway import Alleyway

class Home(Location):
    def __init__(self):
        self.long_description = """After an extremely quick walk, you arrive home out of breath 
        and covered in sweat. You're thrilled to be home."""
        self.short_description = """You are in your small, but comfy home. Not a care in the world. Too bad 
        it's the 15th century and you don't have a T.V. to sit back and watch. Maybe some ice cream too."""
        self.adjacent_locations = []
        self.characters = []
        super().__init__(self.long_description, self.adjacent_locations, self.characters, self.choices)


    def set_as_active(self):
        self.choices: dict[str, Action] = {
            "You think it might be wise to go train.": Move(Alleyway())
        }