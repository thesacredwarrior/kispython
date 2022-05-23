from math import *


def main(y):
    a = pow(1 + 33 * (y ** 2), 4)
    b = pow(1 - y - y ** 3, 7)
    c = pow(1 - y ** 3 - y, 3)
    d = pow(((y ** 2 / 84) + 62 + y**3), 2)
    return a - b - (c + d)


print(main(-0.06))
