from Box import Box
class Cube(Box):
    def __str__(self):
        return f"Cube({self.top_left},{self.bottom_right})"
