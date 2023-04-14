#!/bin/python3
#
from math import sqrt
import sys


def eqBaska(a, b=0, c=0):
    # print('a = {}  b = {}  c = {}'.format(a, b, c))
    delta = b**2 - 4*a*c

    if delta > 0:
        a2 = a*2
        dealtaSqrt = sqrt(delta)

        x1 = (-b + dealtaSqrt)/a2
        x2 = (-b - dealtaSqrt)/a2

        return x1, x2

    else:
        print('Não possui raízes reais!')


if __name__ == '__main__':
    args = sys.argv
    # argsv é atributo do módulo sys que retorna as entradas via
    # teclado como strings

    # print(args)

    a = float(args[1])
    b = float(args[2])
    c = float(args[3])

    resposta = eqBaska(a, b, c)
    print(resposta)

    # resposta = eqBaska(2, 3, 5)
    # print(resposta)
