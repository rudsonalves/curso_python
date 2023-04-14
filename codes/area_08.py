#!/bin/python3
#
from math import pi
import sys
import errno


class Colors:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi*raio**2


def quadrado(aresta):
    return aresta**2


def help():
    print('É necessário informar um raio/aresta.')
    print('\nSintaxe: {} <raio/aresta>\n'.format(sys.argv[0]))


if __name__ == '__main__':
    arg = sys.argv

    if len(arg) < 2:
        help()
        exit(errno.EPERM)

    if not arg[1].isnumeric():
        help()
        print(Colors.ERRO +
              'O argumento deve ser um valor numérico valido!' +
              Colors.NORMAL)
        exit(errno.EINVAL)

    raio = float(arg[1])

    area = circulo(raio)
    print(f'Área do círculo de raio {raio}m é {area:.2f}m²')

    area = quadrado(raio)
    print(f'Área do quadrado de aresta {raio}m é {area:.2f}m²')
