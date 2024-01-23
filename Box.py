from Rectangle import Rectangle



class Box(Rectangle):
    def get_volume(self):
        return self.get_width() * self.get_height()*(self.get_area()/self.get_width())

    def __str__(self):
        return f"Box({self.top_left},{self.bottom_right})"

