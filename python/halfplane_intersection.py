# -*- coding: utf-8 -*-

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cross(self, point):
        return self.x * point.y - self.y * point.x

    def minus(self, point):
        return Point(self.x - point.x, self.y - point.y)

    def plus(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def mul(self, w):
        return Point(self.x * w, self.y * w)

    def on_left(self, line):
        """ if the point is on the left of the line """
        return line.vector.cross(self.minus(line.point)) < 0

    def on_line(self, line):
        return line.vector.cross(self.minus(line.point)) == 0


class Vector:
    def __init__(self, direc):
        self.direc = direc


class Line:
    def __init__(self, p, v):
        self.point = p
        self.vector = v


def polygon_area(points):
    area = 0
    for i in range(len(points)):
        j = (i+1) % len(points)
        area += points[i].cross(points[j])

    return -area * 0.5


def get_intersection(line_a, line_b):
    u = line_a.point.minus(line_b.point)
    t = line_b.vector.cross(u) * 1.0 / line_a.vector.cross(line_b.vector)
    return line_a.point.plus(line_a.vector.mul(t))


def cut(count, point_x, point_y, p):
    line = Line(point_x, point_y.minus(point_x))
    cur = 0
    q = []
    for i in range(1, count + 1):
        if p[i].on_left(line) or p[i].on_line(line):
            cur += 1
            q.append(p[i])
        else:
            if p[i-1].on_left(line):
                cur += 1
                line_oth = Line(p[i], p[i-1].minus(p[i]))
                q.append(get_intersection(line, line_oth))
            if p[i+1].on_left(line):
                cur += 1
                line_oth = Line(p[i], p[i+1].minus(p[i]))
                q.append(get_intersection(line, line_oth))

    for i in range(cur):
        if i == len(p):
            p.append(q[i])
        else:
            p[i+1] = q[i]

    if cur == 0:
        return 0
    p[0] = q[cur-1]
    if cur >= len(p) - 1:
        p.append(q[0])
    else:
        p[cur + 1] = q[0]

    return cur

    
def halfplane_intersection(contour_a, contour_b):
    # 默认点是顺时针
    n = len(contour_a)
    m = len(contour_b)
    p = []
    p.append(Point(contour_a[n-1][0], contour_a[n-1][1]))
    for i in range(len(contour_a)):
        p.append(Point(contour_a[i][0], contour_a[i][1]))

    p.append(Point(contour_a[0][0], contour_a[0][1]))
    for i in range(len(contour_b)):
        n = cut(n, Point(contour_b[i][0], contour_b[i][1]), Point(contour_b[(i + 1) % m][0], contour_b[(i + 1) % m][1]), p)

    final_point = []
    for i in range(1, n+1):
        print p[i].x, p[i].y
        final_point.append(p[i])

    area = polygon_area(final_point)
    print area


if __name__ == '__main__':
    contour_a = [(5, 5), (8, 1),  (2, 3)]
    # contour_b = [(5, 5), (8, 1),  (2, 3)]
    contour_b = [(1, 2),  (1, 4),  (5, 4),  (5, 2)]
    halfplane_intersection(contour_a, contour_b)
