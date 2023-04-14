#!/bin/python3
#
from math import sqrt
import sys


def eqBaska(a, b=0, c=0):
    # print('a = {}  b = {}  c = {}'.format(a, b, c))
    delta = b**2 - 4*a*c

    if delta >= 0:
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

    # print(args, len(args))

    a, b, c = 0, 0, 0

    if len(args) == 4:
        c = float(args[3])

    if len(args) >= 3:
        b = float(args[2])

    if len(args) >= 2:
        a = float(args[1])

    if (len(args) == 1) or (len(args) > 4):
        print('Necessita passar coeficientes')
        print('Use: {} <a> <b> <c>'.format(args[0]))
        sys.exit(1)

    print(f'Resolvendo {a}x² + {b}x + {c} = 0')

    resposta = eqBaska(a, b, c)
    print(resposta)

    # resposta = eqBaska(2, 3, 5)
    # print(resposta)
