#task2
from math import *


def main(z):
    if z < 34:
        return pow(1 + 33 * z ** 2, 4) - pow((1 - z - z ** 3), 7)
    if 34 <= z < 73:
        return (59 * pow(z, 3)) - 0.03 - (20 * z) + (77 * pow(tan(z), 7))
    else:
        return 97 * pow(36 * z, 4) + pow((z ** 2 + 50 + z ** 3), 2) / 94


print(main(62))
