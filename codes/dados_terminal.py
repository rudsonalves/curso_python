#!/bin/python3
#

import sys

if __name__ == '__main__':
    arg = sys.argv[0]
    nome = arg[0]
    d1 = arg[1]
    d2 = arg[2]

    print('Nome: ', nome)
    print('d1:', d1, type(d1))
    print('d2:', d2, type(d2))
