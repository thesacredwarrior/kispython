import math


def main(y):
    n = len(y)
    y.insert(0, 0)
    total = 0
    for i in range(1, n + 1):
        left = (y[n + 1 - math.ceil(i / 3)] ** 2) / 55
        middle = 93 * y[math.ceil(i / 4)]
        right = (y[math.ceil(i / 4)]) ** 3
        total += (left - middle - right) ** 4
    return 28 * total

print(main([-0.01, 0.88, 0.37, -0.69]))
