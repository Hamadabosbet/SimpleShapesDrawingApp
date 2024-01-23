from point import Point
from Rectangle import  Rectangle
from ShapeUtils import ShapeActions
def main():
    point1 = Point(3, 3)
    point2 = Point(100, 100)

    rectangle = Rectangle(point1, point2)
    print(rectangle)

    ShapeActions.move_shape(rectangle, (-1, -1), (100,-30))
    print(rectangle)

if __name__ == "__main__":
    main()
