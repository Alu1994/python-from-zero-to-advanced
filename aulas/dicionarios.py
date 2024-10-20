# Dicionarios

elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534,
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O dicionario possui: {len(elemento)} elementos.')

# Alterar item no dicionario
elemento['grupo'] = 'Alcalinos'
print(elemento)

# Adicionar item no dicionario
elemento['período'] = 1
print(elemento)

# Excluir item no dicionario
del elemento['período']
print(elemento)

# Exclui todos os itens do dicionario
# elemento.clear()
print(elemento)

# Exclui o dicionario da memoria do python
# del elemento
print(elemento)

print('\n\n')
print(elemento.items())
for item in elemento.items():
    print(item)

print('\n\n')
print(elemento.keys())
for key in elemento.keys():
    print(key)

print('\n\n')
print(elemento.values())
for value in elemento.values():
    print(value)
    
print('\n\n')
for key, value in elemento.items():
    print(f'{key}: {value}')