notas = [5,7,8,6,9]
print(notas)

print('\n\n')

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,4]
valores = n1 + n2
valores[0] = 9
print(valores)
print(valores[6])
print(valores[-1])
print(valores[-2])
print(valores[3:5])
print(valores[-2:])
print(len(valores))
print(sorted(valores))
print(sorted(valores, reverse=True))
print(sum(valores))
print(max(valores))
print(min(valores))

print('\n\n')

valores.append(13)
print(valores)

valores.pop()
print(valores)

valores.pop(3)
print(valores)

valores.insert(3, 21)
print(valores)

print(12 in valores)
print(17 in valores)

## cria lista vazia
## planetas = list()
## planetas = []

print('\n\n')
planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta)