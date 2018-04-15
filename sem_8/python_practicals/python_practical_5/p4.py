import numpy
import math


def cross(a, b):
    c = (a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0])
    return c


def dot(a, b):
    c = (a[0]*b[0] + a[1]*b[1] + a[2]*b[2])
    return c


def mag(x):
    return math.sqrt(sum(i**2 for i in x))


def main():
    print("enter points in format (x,y,z)")
    a = tuple(map(float, input("A").split()))
    b = tuple(map(float, input("B").split()))
    c = tuple(map(float, input("C").split()))
    d = tuple(map(float, input("D").split()))
    ab = tuple(numpy.subtract(b, a))
    bc = tuple(numpy.subtract(c, b))
    cd = tuple(numpy.subtract(d, c))
    print(ab, bc, cd)
    x = cross(ab, bc)
    y = cross(bc, cd)
    print(x, y)
    x_dot_y = dot(x, y)
    print(x_dot_y)
    ans = (math.cos(x_dot_y / (mag(x) * mag(y))))
    print(ans)



if __name__ == '__main__':
    main()