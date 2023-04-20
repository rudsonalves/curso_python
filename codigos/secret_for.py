#!/bin/python3
#
import random

if __name__ == '__main__':
    raffle = random.randint(1, 100)

    for count in range(10):
        ans = input('Entre com um número de 1 - 100: ')
        number = int(ans)

        if number == raffle:
            print('Parabéns. Você acertou!!!')
            break
        elif number > raffle:
            print(f'{number} é maior!')
        else:
            print(f'{number} é menor!')

    print(f'O número sorteado foi {raffle}')
