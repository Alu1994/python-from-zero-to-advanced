# Trocar valores entre duas variaveis
var1 = 12
var2 = 31

# em outras linguagens
# aux = var1
# var1 = var2
# var2 = aux

print(f'var1: {var1}, var2: {var2}')

var2, var1 = var1, var2

print(f'var1: {var1}, var2: {var2}')

print(f'  ')
print(f'  ')


# Operadores condicionais ternarios
menor = var1 if var1 < var2 else var2
print(f'menor: {menor}')
print(f'menor: {(var2,var1)[var1 < var2]}')

print(f'  ')
print(f'  ')


# Generators
valores = [1,3,5,7,9,11,13,15]
quadrados = (item**2 for item in valores)
print(quadrados) # Soh eh gerado quando for solicitado *Lazy Loading*
for valor in quadrados:
    print(valor)

print(f'  ')
print(f'  ')


    
# Funcao Enumerate()
bebidas = ['Cafe', 'Cha', 'Agua', 'Suco', 'Refrigerante']
for i, item in enumerate(bebidas):
    print(f'Índice: {i}, Item: {item}')
    
temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
total = 0
for i, t in enumerate(temperaturas):
    if t < 0:
        print(f'A temperatura em {i} é negativa, com {t}°C.')
        total += 1
        
print(f'Há {total} temperaturas negativas na amostra.')

print(f'  ')
print(f'  ')



# Gerenciamento de contexto com with

try:
    manipulador = open('C:\\Users\\caval\\source\\Python-Projects\\python-from-zero-to-advanced\\teste-arquivos\\frutas.dat', 'r', encoding='utf-8')
    print(manipulador.read())
except IOError:
    print(f'Não foi possível abrir o arquivo.')
else:
    manipulador.close()
    
with open('C:\\Users\\caval\\source\\Python-Projects\\python-from-zero-to-advanced\\teste-arquivos\\frutas.dat', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha.rstrip())