class ShapeActions:
    @staticmethod
    def move_shape(shape, top_left_shift, bottom_right_shift):
        shape.top_left.x += top_left_shift[0]
        shape.top_left.y += top_left_shift[1]
        shape.bottom_right.x += bottom_right_shift[0]
        shape.bottom_right.y += bottom_right_shift[1]