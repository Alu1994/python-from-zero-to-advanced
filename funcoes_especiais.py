# Funções Lambda (anônimas)
# Sintaxe:
# lambda argumentos: expressão

quadrado = lambda x: x**2
for i in range(1,11):
    print(quadrado(i))
    
par = lambda x: x % 2 == 0
print(par(10))

f_to_c = lambda f: (f - 32 ) * 5/9
print(f_to_c(32))

# Função map()
# Sintaxe
# map(função, iterável)

num = [1,2,3,4,5,6,7,8]
dobro = list(map(lambda x: x*2, num))
print(dobro)

palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
maiusculas = list(map(str.upper, palavras))
print(maiusculas)


# Função filter()
# Sintaxe
# filter(função, sequência)

def numeros_pares(n):
    return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num_par = list(filter(numeros_pares, numeros))
print(num_par)


numeros_impar = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num_impar = list(filter(lambda x: x%2 != 0, numeros_impar))
print(num_impar)


# Função reduce()
# Sintaxe
# reduce(função, sequência, valor_inicial)

from functools import reduce

def mult(x, y):
    return x * y

numeros_reduce = [1,2,3,4,5,6]
num_reduce = reduce(mult, numeros_reduce)
print(num_reduce)



## Soma cumulativa dos quadrados de valores, usando expressão lambda
numeros_soma = [1,2,3,4]
# ((1² + 2²)² + 3²)² + 4²
total = reduce(lambda x, y: x ** 2 + y ** 2, numeros_soma)
print(total)