#!/bin/python3
from math import pi

raio = float(input('Entre com um raio: '))

area = pi*raio**2
print()
print('A área do círculo de raio {}m é {:.2f}m²'.format(raio, area))
print()

print(__name__)
