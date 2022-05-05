class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.item = None

    def push(self, value):
        self.tail = value

    def __str__(self):
        return f"[{self.tail}]"
