import math


def main(n, x, a):
    f1 = 0
    f2 = 0
    for c in range(1, n + 1):
        f1 += (1 - x - pow(math.log10(x ** 3 + 91 * c ** 2 + c), 3))
    for c in range(1, a + 1):
        for i in range(1, n + 1):
            f2 += 50 * pow((math.ceil(c ** 2 + i + c ** 3)), 6)
    f = f1 + f2
    return f
    
print(main(3, -0.81, 2))
