from app import db

class ClienteMensal(db.Model):
    __tablename__ = 'cliente_mensal'
    
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), primary_key=True, index=True)
    
    # Foreign key para o plano mensal
    plano_id = db.Column(db.Integer, db.ForeignKey('plano_mensal.id'), nullable=False, index=True)
    
    # Relacionamentos
    veiculos = db.relationship('Veiculo',
                                backref=db.backref('cliente_mensal', lazy=True))
    
    __table_args__ = (
        db.Index('idx_cliente_cpf', 'cpf', unique=True),
        db.Index('idx_cliente_plano_id', 'plano_id'),
    )
    
class PlanoMensal(db.Model):
    __tablename__ = 'plano_mensal'
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    
    # Relacionamento com ClienteMensal
    clientes = db.relationship('ClienteMensal', 
                                backref=db.backref('plano_mensal', lazy=True))