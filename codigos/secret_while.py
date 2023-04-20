#!/bin/pythin3
#
import random

secretNumber = random.randint(1, 100)
tryNumber = 0

while secretNumber != tryNumber:
    strNum = input('Entre com um inteiro de 1 a 100: ')
    tryNumber = int(strNum)

    if secretNumber > tryNumber:
        print(f'Número secreto é maior que {tryNumber}')
    elif secretNumber < tryNumber:
        print(f'Número secreto é menor que {tryNumber}')

print(f'Parabéns! O número secreto é {secretNumber}')
