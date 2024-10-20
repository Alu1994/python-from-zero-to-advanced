# Escopo Global e Local

var_global = 'Curso de Python'

def escreve_texto():
    global var_global
    var_global = "Banco de Dados com SQL"
    var_local = "Fábio dos Reis"
    print(f'Váriavel Global: {var_global}')
    print(f'Váriavel Local: {var_local}')
    
if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()
    
    print(f'Tentar acessar as váriaveis diretamente')
    print(f'Váriavel Global: {var_global}')
    ## print(f'Váriavel Local: {var_local}')