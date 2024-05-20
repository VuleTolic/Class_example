class Point:
    # all classes need to have an init method
    def __init__(self, x, y):
        """"
        Init method that inititializes the point with X and Y
        :param x: X coordinate value
        :param y: Y coordinate value
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        How to print this point?
        :return:
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        """
        How to print if in a list?
        :return:
        """
        return self.__str__()

    def distance_orig(self):
        """
        Return the distance from the origin of the point instance
        :return:
        """
        return ((self.x**2 + self.y**2)**0.5)

    def __gt__(self, other):
        """
        How to compare 2 points? We define it here
        :param other: the other point we are comparing against
        :return:
        """
        my_size = self.distance_orig()
        their_size = other.distance_orig()
        return my_size > their_size

if __name__ == "__main__":
    a = Point(2,3) #instantiate by calling the name of the class and parameters in brackets


    print(a.x)
    print(a.y)

    b = Point(7,9)
    print(b.x, b.y)

    import random

    points = []
    for i in range(5):
        x = random.randint(0,100)
        y = random.randint(0,100)
        points.append(Point(x,y))

    for point in points:
        print(point) # here it calls point.__str__

    print(points)
    a = Point(3,4)
    b = Point(12,5)
    c = Point(5,12)

    print(a.distance_orig(), b.distance_orig())
    print(a>b)
    print(a<b)
    print(a==b)
    points.sort()
    print(f"the biggest point is {points[-1]} and the smallest point is {points[0]}")
