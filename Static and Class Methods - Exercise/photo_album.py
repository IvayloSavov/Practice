from typing import List


class PhotoAlbum:
    photos: List[List[str]]

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label: str):
        free_space, index = self.find_free_space()
        if free_space:
            self.photos[index].append(label)
            return f"{label} photo added successfully on page {index + 1} slot " \
                   f"{len(self.photos[index])}"
        return "No more free slots"

    def find_free_space(self):
        for row_index in range(len(self.photos)):
            if len(self.photos[row_index]) < 4:
                return True, row_index

        return False, None

    def display(self):
        delimiter = f"{'-' * 11}\n"
        output = delimiter
        for row_index in range(len(self.photos)):
            current_row = ""
            for col_index in range(len(self.photos[row_index])):
                if self.photos[row_index][col_index] != "":
                    current_row += "[] "
            output += current_row.rstrip() + "\n" + delimiter

        return output.rstrip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

