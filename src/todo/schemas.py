from uuid import uuid4


class Todo:
    """
    Todo class
    """

    def __init__(self, text: str) -> None:
        self.id = uuid4()
        self.text = text
        self.done = False
