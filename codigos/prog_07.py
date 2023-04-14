#!/bin/python3
from math import pi


def circulo(raio):
    area = pi*raio**2
    return area


def quadrado(aresta):
    area = aresta**2
    return area


def reatangulo(base, altura):
    return base*altura


if __name__ == '__main__':
    strRaio = input('Entre com um raio: ')

    raio = float(strRaio)
    areaCirculo = circulo(raio)
    string = 'A área do círculo' + \
        ' de raio {}m é {:.2f}m²'
    print()
    print(string.format(raio, areaCirculo))
    print()

    areaQuadrado = quadrado(raio)
    string = 'A área do quadrado de raio {}m é {:.2f}m²'
    print()
    print(string.format(raio, areaQuadrado))
    print()
