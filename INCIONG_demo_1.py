class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width

    def Perimeter(self):
        return (self.length + self.width) * 2

    def display(self):
        print("The area of a rectangle is", self.Area())
        print("The perimeter of a rectangle is", self.Perimeter())


class Rectangle(Shape):
    pass


rectangle = Shape(10, 5)
rectangle2 = Rectangle(3, 6)

rectangle.display()
rectangle2.display()