from AdventureGame.game_files.actions.Action import Action

class Move(Action):
    def __init__(self, new_location):
        self.new_location = new_location

    def execute(self, game_engine):
        game_engine.move_location(self.new_location)


