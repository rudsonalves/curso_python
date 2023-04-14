#!/bin/python3
#
from math import pi
import sys


def circulo(raio):
    return pi*raio**2


def quadrado(aresta):
    return aresta**2


if __name__ == '__main__':
    arg = sys.argv

    raio = float(arg[1])

    area = circulo(raio)
    print(f'Área do círculo de raio {raio}m é {area:.2f}m²')

    area = quadrado(raio)
    print(f'Área do quadrado de aresta {raio}m é {area:.2f}m²')
