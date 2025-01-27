import random

from classexample import Point

# just to test that Point was imported as expected
a = Point(5,5)
print(a)

class ColorPoint(Point):
    # this is a class that inherits from Point
    COLORS = ["red", "blue", "green", "yellow", "purple", "cyan", "black", "white", "celadon", "xandaoo"]
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        super().__init__(x, y)
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception("This is an unsupported color. Allowed colors are: {self.COLORS}")

    @classmethod
    def add_extra_color(cls, color):
        cls.COLORS.append(color)

    @property
    def distance_orig(self):
        """
        Return the distance from origin of the point instance
        :return:
        """
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return f"{self.color}<{self.x},{self.y}>"
if __name__ == "__main__":
    red_point = ColorPoint(10, 10, "red")
    red_point.add_extra_color("orange")
    orange_point = ColorPoint(20, 20, "orange")
    red_point.x = 30
    print(f"{red_point} has distance to origin = {red_point.distance_orig}")

