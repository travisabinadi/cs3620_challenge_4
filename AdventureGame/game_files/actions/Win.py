from AdventureGame.game_files.actions.Action import Action

class Win(Action):
    def __init__(self, win_message: str):
        self.win_message = win_message

    def execute(self, game_engine):
        print(self.win_message)
        game_engine.is_game_over = True


