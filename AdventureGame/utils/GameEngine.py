from AdventureGame.utils.UserInput import UserInput
from AdventureGame.game_files.characters.Hero import Hero
from AdventureGame.game_files.locations.Location import Location
from AdventureGame.game_files.locations.NewGameStart import NewGameStart
from AdventureGame.game_files.story.Choices import Choices

class GameEngine:
    def __init__(self):
        self.user_input = UserInput()
        self.player = Hero()
        self.current_location: Location
        self.is_game_over: bool = False

    def start(self, start_room):
        self.current_location = start_room
        while not self.is_game_over:
            chioces: Choices = self.current_location.visit()
            action = self.user_input.get_selected_choice(chioces)
            if action is None:
                self.is_game_over = True
                return
            action.execute(game_engine=self)

    def move_location(self, new_location: Location):
        self.current_location = new_location
