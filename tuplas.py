# São imutáveis
# São mais rapidas que as listas

tupla = (2,4,6,7,9)
#tupla[1] = 5  ## vai dar erro
print(tupla)


halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres

print(halogenios[-1])
print(gases_nobres[-1])
print(elementos)

t1 = (5,2,6,8,4,5,6)
print(t1.count(5)) ## Quantas vezes aparece o 'item' na tupla

print('Cl' in halogenios)
print('Fe' in halogenios)

## Operacoes nao disponiveis
## .sort(), .append(), .reverse(), .pop() ...
## operacoes que alteram a tupla nao podem ser utilizadas

## Criando lista a partir de tupla
grupo17 = list(halogenios)
grupo17[0] = 'H'
print(grupo17)
print(type(grupo17))

## Criando tupla a partir da lista
grupo1 = ['Li','Na','K','Rb','Cs','Fr']
alcalinos = tuple(grupo1)
print(type(grupo1))
print(type(alcalinos))

## print(alcalinos.sort()) ## nao funciona
print(sorted(alcalinos))