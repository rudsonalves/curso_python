#!/bin/python3
#
from math import pi


def circulo(raio):
    return pi*raio**2


def quadrado(aresta):
    return aresta**2


if __name__ == '__main__':
    raio = float(input('Entre com o raio: '))

    area = circulo(raio)
    print(f'Área do círculo de raio {raio}m é {area:.2f}m²')

    area = quadrado(raio)
    print(f'Área do quadrado de aresta {raio}m é {area:.2f}m²')
