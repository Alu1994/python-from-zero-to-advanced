# Orientação a Objetos: Paradigma de Programação
# Classes e Objetos

class Veiculo:
    def __init__(self, fabricante, modelo):
        self.open = None ## public
        self.__fabricante = fabricante ## private
        self.__modelo = modelo
        self.__numero_registro = None
    
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')
        
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}\n')
        
    def set_num_registro(self, registro):
        self.__numero_registro = registro
    
    def get_num_registro(self):
        return self.__numero_registro

class Carro(Veiculo):
    # Método __init__ será herdado
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas!')
        
class Motocicleta(Veiculo):
    # Método __init__ será herdado
    def movimentar(self):
        print(f'Corro muito!')
        
class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)
    
    def get_categoria(self):
        return self.__cat

    def movimentar(self):
        print(f'Eu voo alto!')

if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('490321-1')
    print(f'Registro: {meu_veiculo.get_num_registro()}\n')
    
    meu_carro = Carro('Volkswagen', 'Golf')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()
    
    seu_carro = Carro('Audi', 'A5 Sportback')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()
    
    moto = Motocicleta('Harley-Davidson', 'Nightster Special')
    moto.movimentar()
    moto.get_fabr_modelo()
    
    aviao = Aviao('Boing', '747', 'Comercial')
    aviao.movimentar()
    aviao.get_fabr_modelo()
    print(f'Categoria: {aviao.get_categoria()}')