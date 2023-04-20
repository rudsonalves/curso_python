#!/bin/python3
#
import random


def attributeStatistic():
    sum = 0
    min = 99
    for i in range(4):
        d6 = dice6()
        sum += d6
        if min > d6:
            min = d6

    return sum - min


def dice6():
    return random.randint(1, 6)


def dice8():
    return random.randint(1, 8)


def createStatistics():
    attributes = ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA')
    for attribute in attributes:
        valueAttribute = attributeStatistic()
        print(f'{attribute}: {valueAttribute:>2}')


if __name__ == '__main__':
    createStatistics()
    # 3. criar uma função para imprimir as estatíticas do personagem
    # 4. Gerar 10 personagens
    # 5. fazer a execução pela linha de comando entrando quantos
    # personagens irá gerar.
