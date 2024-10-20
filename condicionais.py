media = 0.0

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

media = (n1 + n2) / 2

if (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif (media >= 5):
    print("Resultado: Recuperação!")
else:
    print("Resultado: Aluno reprovado.")
    
print('Sua média é {}'.format(media))