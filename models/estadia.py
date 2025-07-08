from app import db

class Estadia(db.Model):
    __tablename__ = 'estadia'
    
    # Colunas principais
    id = db.Column(db.Integer, primary_key=True)
    entrada = db.Column(db.DateTime, nullable=False, index=True)
    saida = db.Column(db.DateTime, nullable=True, index=True)
    valor = db.Column(db.Float, nullable=True)
    
    # Foreign keys
    veiculo = db.Column(db.String(7), db.ForeignKey('veiculo.placa'), nullable=False, index=True)
    tarifa = db.Column(db.Integer, db.ForeignKey('tarifa.id'), nullable=False)
    
    # Relacionamentos
    tarifa_rel = db.relationship('Tarifa', backref='estadias', uselist=False)

    __table_args__ = (
        db.Index('idx_estadia_veiculo_entrada', 'veiculo', 'entrada'),
        db.Index('idx_estadia_veiculo_saida', 'veiculo', 'saida'),
    )

