class Choice:
    def __init__(self, prompt: str, ndx: int, action: str):
        self.prompt = prompt
        self.action = action
        self.ndx = ndx
        self.selected = False

    def is_selected(self, selection):
        return self.is_selected()
