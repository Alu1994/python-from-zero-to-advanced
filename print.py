nome = input('Digite seu nome: ')
msg = 'Olá ' + nome + '! Bem-vindo ao curso de python!'
print(msg)
print('Outro texto \n\n')

print('Imprime a mensagem e muda de linha')
print('Imprime a mensagem e permanece na linha.', end='')
print(' Continuo na mesma linha!\n\n')

nome_novo = 'Maria'
idade = 30
msg_formatada = 'O nome dela é {0} e ela tem {1} anos.'.format(nome_novo, idade)
print(msg_formatada)
print('O nome dela é {0} e ela tem {1} anos.\n\n'.format(nome_novo, idade))

nome_novo_2 = 'Matheus'
peso = 92
msg = f'Olá, meu nome é {nome_novo_2} e eu peso {peso} quilos.'
print(msg)
print(f'Olá, meu nome é {nome_novo_2} e eu peso {peso} quilos.\n\n')


a = 10
b = 5

res = f'{a+b}'
print(res)

valor = 125.579637
res2 = f'O valor é \'{valor:.2f}\''
print(res2)

nome_new = 'João'
idade_new = 32
res2 = f'Nome: {nome_new}\tIdade: {idade_new}'
print(res2)