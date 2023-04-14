#! python
from math import pi


def circulo(raio):
    area = pi*raio**2
    return area


def quadrado(aresta):
    area = aresta**2
    return area


def retangulo(base, altura):
    area = base*altura
    return area


if __name__ == '__main__':
    strRaio = input('Entre com um raio: ')

    raio = float(strRaio)

    areaCirculo = circulo(raio)
    string = 'A area do circulo de raio {}m e: {:.2f}m^2'
    print()
    print(string.format(raio, areaCirculo))
    print()

    areaQuadrado = quadrado(raio)
    string = 'A area do quadrado de aresta {}m e: {:.2f}m^2'
    print()
    print(string.format(raio, areaQuadrado))
    print()
