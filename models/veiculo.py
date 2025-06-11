from app import db
from .enums import TipoVeiculo

class Veiculo(db.Model):
    __tablename__ = 'veiculo'
    
    placa = db.Column(db.String(7), primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    cor = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.Enum(TipoVeiculo), nullable=False)
    
    # Foreign keys
    cliente_mensal_id = db.Column(db.Integer, db.ForeignKey('cliente_mensal.id'), nullable=True)
    
    # Relacionamentos
    estadias = db.relationship('Estadia',
                                backref=db.backref('veiculos', lazy=True))