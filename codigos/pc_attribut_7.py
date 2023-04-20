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


# def figther():
#     attributes = {'STR': 3, 'CON': 3}
#     while (attributes['STR'] < 15) | (attributes['CON'] < 15):
#         attributes = createStatistics()
#     return attributes


def figther():
    while True:
        attributes = createStatistics()
        if (attributes['STR'] > 14) & (attributes['CON'] > 14):
            return attributes


if __name__ == '__main__':
    p = figther()
    printPersonagem(p)
