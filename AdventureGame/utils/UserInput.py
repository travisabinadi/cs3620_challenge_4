from AdventureGame.utils.handle_error import HandleError
from AdventureGame.game_files.story import Choice, Choices

class UserInput:
    def __init__(self):
        self.err_handler = HandleError()

    def get_values(self, promts: list[str]):
        inputs: list[str] = []
        for prompt in promts:
            user_input = input(prompt)
            inputs.append(user_input)
        return inputs

    def get_nums(self, promts: list[float]):
        inputs: list[float] = []
        for prompt in promts:
            invalid_input = True
            while invalid_input:
                user_input = input(prompt)
                try:
                    float(user_input)
                    invalid_input = False
                except ValueError as err:
                    self.err_handler.invalid_input(ex=err)
            inputs.append(user_input)
        return inputs

    def get_selected_choice(self, choices: Choices):
        if choices.is_empty():
            return None
        selected_choice = None
        while selected_choice is None:
            print("What will you do?")
            for choice in choices.choices:
                print(str(choice.ndx) + ": " + choice.prompt)
            resp = input("Choice: ")
            selected_choice: Choice = choices.check_choice(resp)
        return selected_choice.action
