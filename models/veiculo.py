from app import db
from .enums import TipoVeiculo

class Veiculo(db.Model):
    __tablename__ = 'veiculo'
    
    placa = db.Column(db.String(7), primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    cor = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.Enum(TipoVeiculo), nullable=False, index=True)
    
    # Foreign keys
    cliente_mensal_cpf = db.Column(db.String(11), db.ForeignKey('cliente_mensal.cpf'), nullable=True, index=True)
    
    # Relacionamentos
    estadias = db.relationship('Estadia',
                                backref=db.backref('veiculos', lazy=True))

    __table_args__ = (
        db.Index('idx_veiculo_tipo', 'tipo'),
        db.Index('idx_veiculo_cliente_mensal_cpf', 'cliente_mensal_cpf'),
    )