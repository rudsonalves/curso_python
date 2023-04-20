#!/bin/python3
#
# 1 1 2 3 5 8 13 ...
#


def fibonacci(n):
    fib = [1, 1]
    a, b = 1, 1

    for i in range(n-2):
        a, b = b, a + b
        fib.append(b)

    return fib


if __name__ == '__main__':

    print(fibonacci(100))
