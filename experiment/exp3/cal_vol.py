import math


def deco(func):
    def check_deco(*args):
        for par in args:
            if par <= 0:
                return "Illegal Parameter!"
        return func(*args)

    return check_deco


@deco
def tri_cone(s, h):
    return s * h / 3


@deco
def ball_sphere(r):
    return (4 * math.pi * (r ** 3)) / 3


@deco
def rectangular(s, h):
    return s * h


if __name__ == '__main__':
    print(tri_cone(1, 0))
    print(ball_sphere(1))
    print(rectangular(1, 1))
