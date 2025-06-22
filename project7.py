import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):  # x1,y1 bottom-left; x2,y2 top-right
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
    def corners(self):
        return [
            Point(self.x1, self.y1),
            Point(self.x1, self.y2),
            Point(self.x2, self.y1),
            Point(self.x2, self.y2),
        ]

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

# Instantiate the circle
c = Circle(Point(150, 100), 75)

def point_in_circle(circle, pt):
    dx = pt.x - circle.center.x
    dy = pt.y - circle.center.y
    return dx*dx + dy*dy <= circle.radius*circle.radius

def rect_in_circle(circle, rect):
    return all(point_in_circle(circle, corner) for corner in rect.corners())

def rect_circle_overlap(circle, rect):
    cx, cy, r = circle.center.x, circle.center.y, circle.radius
    # Find closest point to circle center on/in rectangle
    nx = max(rect.x1, min(cx, rect.x2))
    ny = max(rect.y1, min(cy, rect.y2))
    dx = nx - cx
    dy = ny - cy
    return dx*dx + dy*dy <= r*r
