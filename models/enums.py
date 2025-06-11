from enum import Enum

class TipoUsuario(Enum):
    ADMIN = 'admin'
    OPERADOR = 'operador'
    
class TipoVeiculo(Enum):
    CARRO = 'carro'
    MOTO = 'moto'
    CAMINHAO = 'caminhao'
    VAN = 'van'
    
class TipoRelatorio(Enum):
    FINANCEIRO = 'financeiro'
    ESTADIA = 'estadia'