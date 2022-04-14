from ast import Return
""" clas create 2d points representation"""
class Point:
    def __init__(self, x = 0, y = 0):
       """initialice the point un the given parameters (x,y).
       if they are not present, the point is ceated in the origin"""
       self.move(x,y)

    def reset(self):
        """move the point back to the origin"""
        self.move(0,0)

    def move(self, x, y):
        """move the point to a new location"""
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        """calculate the distance using pytagoric rule.
        The result is a float number"""
        distance_x = self.x - other_point.x
        distance_y = self.y - other_point.y

        square_sum = distance_x ** 2 + distance_y ** 2
        return  square_sum ** (1/2)