class Winner:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"Winner: name = '{self.name}'; score = {self.score};"