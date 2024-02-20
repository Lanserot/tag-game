class Button:
    def __init__(self, id: int, text: str, tag: str, active: bool = False):
        self.id = id
        self.text = text
        self.tag = tag
        self.active = active

    def set_active(self, active):
        self.active = active
