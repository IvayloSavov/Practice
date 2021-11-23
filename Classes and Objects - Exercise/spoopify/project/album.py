from project.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = [*args]
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        elif song in self.songs:
            return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."

        song = [s for s in self.songs if s.name == song_name]

        if not song:
            return "Song is not in the album."

        self.songs.remove(song[0])
        return f"Removed song {song[0].name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return f"Album {self.name}\n" + "\n".join(f"== {s.get_info()}" for s in self.songs) + "\n"
