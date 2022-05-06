from math import ceil


def main(y):
    number = 0
    n = len(y)
    for i in range(1, n + 1):
        number += 28 * (((y[ceil(i / 3) - 1] ** 2 / 55) - (93 * y[ceil(i / 4) - 1]) - (y[ceil(i / 4) - 1] ** 3)) ** 4)
    return number

print(main([-0.01, 0.88, 0.37, -0.69]))
