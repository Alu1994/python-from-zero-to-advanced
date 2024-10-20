# Modularização, Reúso de Código, Legibilidade
# def <nome_função>([argumentos]):
#     <instruções>

def mensagem():
    print('Curso de Python')
    
mensagem()

def soma(a, b):
    return a + b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return 'Impossível dividir por zero!'
    return a / b

def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)
    return quadrados

def contar(num=11, caractere='+'):
    for i in range(1, num):
        print(caractere)

# if __name__ == '__main__':
#     print(soma(12, 7))
#     print(mult(12, 7))

# if __name__ == '__main__':
#     a = int(input('Digite um número: '))
#     b = int(input('Digite outro número: '))
    
#     r = div(a, b)
#     print(f'{a} dividido por {b} é igual a {r}')

# if __name__ == '__main__':
#     valores = [2,5,7,9,12]
#     resultados = quadrado(valores)
#     for g in resultados:
#         print(g)

if __name__ == '__main__':
    contar(num=5, caractere='&')
    contar(6, '@')