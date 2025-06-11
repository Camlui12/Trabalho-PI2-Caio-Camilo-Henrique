from app import db

class ClienteMensal(db.Model):
    __tablename__ = 'cliente_mensal'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    
    # Relacionamentos
    veiculos = db.relationship('Veiculo',
                                backref=db.backref('cliente_mensal', lazy=True))