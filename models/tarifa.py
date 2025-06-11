from app import db

class Tarifa(db.Model):
    __tablename__ = 'tarifa'
    
    # Colunas principais
    id = db.Column(db.Integer, primary_key=True)
    valorHora = db.Column(db.Float, nullable=False)
    tolerancia = db.Column(db.Integer, nullable=False)  # Tolerância em minutos
    tetoDiario = db.Column(db.Float, nullable=False)  # Teto diário em reais
    dataVigencia = db.Column(db.Date, nullable=False)  # Data de vigência da tarifa
    
    # Relacionamentos
    estadia = db.relationship('Estadia',
                                backref=db.backref('tarifas', uselist=False), uselist=False)
