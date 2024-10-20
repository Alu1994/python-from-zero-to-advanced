import os
import shutil  ## remove todas as pastas e arquivos dentro de uma pasta
import pathlib

caminho = pathlib.Path()
print(caminho.cwd())

os.mkdir('c:\\Teste')
os.makedirs('c:\\teste\\america\\brasil\\ilha-bela')

manipulador = open('c:\\teste\\america\\brasil\\ilha-bela\\arq.txt', 'x')
manipulador.close()

print(os.listdir('c:\\teste\\america\\brasil\\ilha-bela'))

shutil.rmtree('c:\\teste')