numeros = [1,4,7,9,10,12,21]

quadrados = list(map(lambda num: num**2, numeros))
print(quadrados)

quadrados = [num**2 for num in numeros]
print(quadrados)

# Criar uma lista de numeros pares de 0 a 10
pares = [num for num in range(11) if num % 2 == 0]
print(pares)

# ele primeiro faz o loop, em seguida faz o if e por ultimo volta para o começo e eleva a 2
pares = [num**2 for num in range(11) if num <= 10]
print(pares)


frase = 'A lógica é apenas o princípio da sabedoria, e não o seu fim.'
vogais = ['a','e','i','o','u','á','é','í','ó','ú','ã']

lista_vogais = [v for v in frase if str.lower(v) in vogais]
print(f'A frase possui {len(lista_vogais)} vogais:')
print(lista_vogais)

# Distributiva entre valores de duas listas
distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)