from AdventureGame.game_files.actions.Action import Action
from AdventureGame.game_files.story.Choice import Choice

class Choices:
    def __init__(self, choices: dict[str, Action] = None):
        self.choices: list[Choice] = []
        if choices != None:
            ndx_counter = 1
            for description, action in choices.items():
                self.choices.append(Choice(description, ndx_counter, action))
                ndx_counter += 1

    def check_choice(self, ndx_selected: str):
        try:
            selected = int(ndx_selected)
            for choice in self.choices:
                if choice.ndx == selected:
                    return choice
        except Exception:
            print("Invalid entry for choice. Please enter numeric index for the corresponding choice.")
        return None

    def is_empty(self):
        if len(self.choices) == 0:
            return True
        else:
            return False