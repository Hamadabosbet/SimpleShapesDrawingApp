from Rectangle import Rectangle

class Square(Rectangle):
    def __str__(self):
        return f"Square({self.top_left},{self.bottom_right})"
