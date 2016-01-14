# -*- coding: utf-8 -*-

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cross(point):
        return self.x * point.y - self.y * point.x

    def minus(point):
        return Point(self.x - point.x, self.y - point.y)

    def plus(point):
        return Point(self.x + point.x, self.y + point.y)

    def mul(w):
        return Point(self.x * w, self.y * w)


class Vector:
    def __init__(self, direc):
        self.direc = direc


class Line:
    def __init__(self, p, v, ang):
        self.point = p
        self.vector = v
        self.angle = ang

    def on_left(self, p):
        """ if the point is on the left of the line """
        return self.vector.cross(p.minus(self.point)) > 0


def polygon_area(points):
    area = 0
    for i in range(len(points)):
        j = (i+1)%len(points)
        area += points[i].cross(points[j])

    return area * 0.5


def get_intersection(line_a, line_b):
    u = line_a.point.minus(line_b.point)
    t = line_b.vector.cross(u) / line_a.vector.cross(line_b.vector)
    return line_a.point.plus(line_a.vector.mul(t))


def cut(count, point_x, point_y):
    a = point_y.y - point_x.y
    b = point_x.x - point_y.x
    c = -point_x.cross(point_y)
    for i in range(count + 1):
        if a*

def halfplane_intersection(lines, points):
    # 默认点是顺时针
    for i in range(len(lines)):
        
