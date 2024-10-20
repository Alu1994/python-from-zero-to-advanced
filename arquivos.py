# manipulador = open('arquivo.txt', 'r', encoding='utf-8')

# print(f'Método read():')
# print(f' ')

# print(manipulador.readline())
# print(manipulador.read())

# print(manipulador.readlines())

texto = input('Qual termo deseja procurar no arquivo? ')

try:
    manipulador = open('C:\\Users\\caval\\source\\Python-Projects\\python-from-zero-to-advanced\\teste-arquivos\\arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()
        if texto in linha:
            print(f'A string foi encontrada!')
            print(linha)
        else:
            print(f'A string não foi encontrada!')
except IOError:
    print(f'Não foi possível abrir o arquivo.')
else:
    manipulador.close()

print(f'   ')
print(f'   ')
    
try:
    manipulador = open('C:\\Users\\caval\\source\\Python-Projects\\python-from-zero-to-advanced\\teste-arquivos\\arquivo-2.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()
        print(linha)
except IOError:
    print(f'Não foi possível abrir o arquivo.')
else:
    manipulador.close()
    
    
## Escrever em arquivos de texto
texto = 'texto adicionado'
try:
    manipulador = open('C:\\Users\\caval\\source\\Python-Projects\\python-from-zero-to-advanced\\teste-arquivos\\arquivos.txt', 'w', encoding='utf-8')
    manipulador.write('\nTestando escrita')
    manipulador.write('\nFim da escrita!')
    manipulador.write(f'\n{texto}')
except IOError:
    print(f'Não foi possível abrir o arquivo.')
else:
    manipulador.close()
    
frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola\n']
try:
    manipulador = open('C:\\Users\\caval\\source\\Python-Projects\\python-from-zero-to-advanced\\teste-arquivos\\frutas.dat', 'w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
    print(f'Não foi possível abrir o arquivo.')
else:
    manipulador.close()
    
try:
    manipulador = open('C:\\Users\\caval\\source\\Python-Projects\\python-from-zero-to-advanced\\teste-arquivos\\frutas.dat', 'r', encoding='utf-8')
    print(manipulador.read())
except IOError:
    print(f'Não foi possível abrir o arquivo.')
else:
    manipulador.close()