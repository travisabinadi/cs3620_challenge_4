from AdventureGame.game_files.actions.Move import Move
from AdventureGame.game_files.locations.Location import Location
from AdventureGame.game_files.locations.Alleyway import Alleyway

class NewGameStart(Location):
    def __init__(self):
        self.long_description = """It is a cold, dark night. You have been working a long, hard day. 
        Each step you take, you can feel your legs ache and your head throb. Training to be a knight is 
        tough work.\n As you walk down the street you can hear loud voices echoing from an alleyway. You 
        pause and listen for a moment. Suddenly you feel a chill run down your spine. An ungodly sound arises, 
        followed by a bellowing roar."""
        self.choices: dict[str, Action] = {}
        super().__init__(self.long_description, self.choices)

    def set_as_active(self):
        down_alley: Action = Move(new_location=Alleyway())
        choices: dict[str, Action] = {
            "Follow the noises down the alleyway.": down_alley
        }
        self.choices = choices
