# frase = 'vamos aprender python hoje.'
# palavras = frase.split()

# print(frase[0:5])

# print(palavras[1])

# for palavra in palavras:
#     print(palavra)

# for letra in frase:
#     print(letra)
    
# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

produtos = 'carbonato de sódio e óxido de zinco'
print('sódio' in produtos)
print('magnésio' in produtos)
print('magnésio' not in produtos)

item = 'hipoclorito'
pos = item.find('clor')
print(pos)
pos = item.find('flu')
print(pos)

objeto_celeste = 'galáxia espiral M31'
print(objeto_celeste.upper())
print(objeto_celeste.lower())
print(objeto_celeste.capitalize())
print(objeto_celeste.title())

suplemento = '   cloreto de magnésio!'
n_suplemento = suplemento.replace('magnésio', 'zinco')
print(suplemento)
print(n_suplemento)

print(suplemento.lstrip())
print(suplemento.rstrip())
print(suplemento.strip())

fruta = 'Abacate'
print(fruta)
print(fruta.rjust(20))
print(fruta.center(20, '-'))
print(fruta.ljust(20, '-'))

p = 'Bóson treinamentos'
print(p.startswith('B'))
print(p.endswith('s'))


## DocStrings - pode ser usado em uma variavel ou 
## como um tipo de comentário

texto = """
Docstring é uma espécie de documentação
que podemos inserir dentro de um módulo, função
ou classe no Python, entre outros locais.
    Respeita o deslocamento do texto e é multilinhas.
"""

print(texto)