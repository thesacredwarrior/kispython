def main(n):
    if n == 0:
        return -0.09
    if n == 1:
        return -0.22
    if n >= 2:
        return pow(main(n - 2), 2) + 9 * main(n - 1) + 27
      
print(main(6))
