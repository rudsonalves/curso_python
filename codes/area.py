#!/bin/python3
#
from math import pi


def circulo(raio):
    area = pi*raio**2
    print(f'Área do círculo de raio {raio}m é {area:.2f}m²')


def quadrado(aresta):
    area = aresta**2
    print(f'Área do quadrato de aresta {aresta}m é {area:.2f}m²')


if __name__ == '__main__':
    raio = float(input('Entre com o raio: '))
    circulo(raio)
    quadrado(raio)
