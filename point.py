class Point:
    def __init__(self, x, y):
        if x < 0 or y < 0:
            raise ValueError("must be positive numbers")
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"

    @classmethod
    def from_string(cls, string):

        x, y = map(int, string[len("Point("):-1].split(','))
        return cls(x, y)