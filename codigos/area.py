#!/bin/python3
from math import pi


def circulo(raio):
    area = pi*raio**2
    print()
    print('A área do círculo de raio {}m é {:.2f}m²'.format(raio, area))
    print()


def quadrado(aresta):
    area = aresta**2
    print()
    print('A área do quadrado de aresta {}m é {:.2f}m²'.format(aresta, area))
    print()


def reatangulo(base, altura):
    area = base*altura
    print()
    print('A área do retângulo de basexaltura ({}m x {}m) é {:.2f}m²'.
          format(base, altura, area))
    print()


if __name__ == '__main__':
    strRaio = input('Entre com um raio: ')

    raio = float(strRaio)

    circulo(raio)
