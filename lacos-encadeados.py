for count_ex in range(1,6):
    print(f'\nRodada: {count_ex}')
    for count_in in range(5, 0, -1):
        print(f'Valor: {count_in}')

print('Fim dos laços')

import random

for A in range(1,6):
    print(f'\nConjunto: {A}')
    for B in range(5):
        num = random.randint(1,100)
        print(f'Valor: {num}')