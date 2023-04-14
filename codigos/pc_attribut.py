#!/bin/python3
#
import random


def attributeStatistic():
    # 1. remover um dos laços for e fazer tudo em apenas um laço
    d6 = []

    for i in range(4):
        d6.append(dice6())

    min = 99
    sum = 0
    for dice in d6:
        sum += dice
        if min > dice:
            min = dice

    return sum - min


def dice6():
    return random.randint(1, 6)


def dice8():
    return random.randint(1, 8)


if __name__ == '__main__':
    # 2. transformar isto numa função para gerar as estatísticas do personagem
    attributes = ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA')

    for attribute in attributes:
        valueAttribute = attributeStatistic()
        print(f'{attribute}: {valueAttribute:>2}')

    # 3. criar uma função para imprimir as estatíticas do personagem
    # 4. Gerar 10 personagens
