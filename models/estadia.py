from app import db

class Estadia(db.Model):
    __tablename__ = 'estadia'
    
    # Colunas principais
    id = db.Column(db.Integer, primary_key=True)
    entrada = db.Column(db.DateTime, nullable=False)
    saida = db.Column(db.DateTime, nullable=True)
    valor = db.Column(db.Float, nullable=True)
    
    # Foreign keys
    veiculo = db.Column(db.String(7), db.ForeignKey('veiculo.placa'), nullable=False)
    tarifa = db.Column(db.Integer, db.ForeignKey('tarifa.id'), nullable=False)

