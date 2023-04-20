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
    person = {}
    for attribute in attributes:
        person[attribute] = attributeStatistic()

    return person


def printPersonagem(person):
    for attrib in person.keys():
        print('{0}: {1:>2}'.format(attrib, person[attrib]))


if __name__ == '__main__':
    enter = input('Quantos personagens deseja gerar? ')
    max = int(enter)

    for count in range(max):
        p = createStatistics()
        print('Person {}'.format(count+1))
        printPersonagem(p)
        print()
