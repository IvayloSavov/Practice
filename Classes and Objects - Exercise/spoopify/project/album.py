class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = [*args]
        self.published = False

