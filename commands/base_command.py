class BaseCommand:
    def __init__(self, name):
        self.name = name

    def execute(self):
        raise NotImplementedError("Tuto metodu je nutné implementovat.")
