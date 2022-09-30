from AdventureGame.utils.UserInput import UserInput
from AdventureGame.game_files.characters.Character import Character
from AdventureGame.game_files.story.Choices import Choices
from AdventureGame.game_files.locations.Area import Area
from AdventureGame.game_files.actions.Move import Move
from AdventureGame.game_files.actions.Action import Action

class Location(Area):
    def __init__(self, description: str, choices: dict[str, Action] = None, adjacent_locations: dict[str, Area] = None):
        self.description: str = description
        self.choices: dict[str, Action] = choices if choices is not None else {}
        self.user_input: UserInput = UserInput()
        self.adjacent_locations = adjacent_locations if adjacent_locations is not None else {}

    def set_as_active(self):
        # Add locations as new move actions when location is made active.
        for description, new_location in self.adjacent_locations.items():
            move_action: Action = Move(new_location=new_location)
            self.choices[description] = move_action
        return self.choices

    def visit(self) -> Choices:
        self.set_as_active()
        print(self.description)
        return Choices(self.choices)

    def add_action(self, description: str, action: Action):
        self.choices[description] = action



