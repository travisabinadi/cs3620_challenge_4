from AdventureGame.game_files.actions.Action import Action
from random import random

class BattleAction(Action):
    def __init__(self, chance_to_win: float, win_action: Action, win_message: str, lose_message: str):
        self.chance_to_win = chance_to_win
        self.win_action = win_action
        self.win_message = win_message
        self.lose_message = lose_message

    def execute(self, game_engine):
        player_roll = random()
        if player_roll > 1 - self.chance_to_win:
            print(self.win_message)
            self.win_action.execute(game_engine)
        else:
            print(self.lose_message)
            game_engine.is_game_over = True
            print("You have lost.")
