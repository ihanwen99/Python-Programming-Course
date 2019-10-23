from math import sin, cos, pi


def calculation():
    x = input("Please input x: ")
    s = sin(x) ** 2
    t = cos(x)

    if x == 0:
        return pi
    elif x > 0:
        return (s + t + 1) ** 3 - 3 * (s + t)
    else:
        return 4 * s + 4 * t - 1


if __name__ == '__main__':
    re = calculation()
    print "The result is ", re
