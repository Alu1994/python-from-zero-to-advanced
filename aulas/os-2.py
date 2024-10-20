import os

os.chdir('c:\\TesteNovo')
print(f'Diretorio atual: {os.getcwd()}')

padrao_nome = input('Qual o padrao de nomes de arquivos a usar (sem a extensao)? ')

contador = 0
for c, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        if exten_arq == '.txt':
            nome_arq = padrao_nome + '-' + str(contador)            
            nome_novo = f'{nome_arq}{exten_arq}'
            os.rename(arq, nome_novo)
        else:
            contador -= 1
        contador += 1
        
print(f'\nArquivos renomeados.')