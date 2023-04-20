#!/bin/python3
#

def media(values):
    sum = 0
    for value in values:
        sum += value

    return sum/len(values)


if __name__ == '__main__':
    print(media([11, 12, 13, 14, 15, 16, 17, 18, 19]))
