from math import ceil


def main(y):
    number = 0
    n = len(y)
    for i in range(1, n + 1):
        number += 28 * (((y[ceil(i / 3) - 1] ** 2 / 55) - (93 * y[ceil(i / 4) - 1]) - (y[ceil(i / 4) - 1] ** 3)) ** 4)
    return number

print(main([-0.01, 0.88, 0.37, -0.69]))


import math



def main(y):
    sum = 0
    for i in range(len(y)):
        dif1 = (pow(y[1 - math.trunc(i/3)], 2) / 55)
        dif2 = 93 * y[math.trunc(i/4)]
        dif3 = pow(y[math.trunc(i/4)], 3)
        sub_res = (dif1 - dif2 - dif3)
        sum += 28 * pow(sub_res, 4)
    return sum

print(main([-0.01, 0.88, 0.37, -0.69]))
