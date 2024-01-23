from point import Point


class Rectangle:
    def __init__(self, top_left, bottom_right):
        if not (0 <= top_left.x <= bottom_right.x <= 2240) or not (0 <= top_left.y <= bottom_right.y <= 1080):
            raise ValueError("Invalid rectangle coordinates. Coordinates must be within (0, 0) and (2240, 1080).")
        self.top_left = top_left
        self.bottom_right = bottom_right

    def get_width(self):
        return self.bottom_right.x - self.top_left.x

    def get_height(self):
        return self.bottom_right.y - self.top_left.y

    def get_area(self):
        return self.get_width() * self.get_height()

    def __str__(self):
        return f"Rectangle({self.top_left},{self.bottom_right})"