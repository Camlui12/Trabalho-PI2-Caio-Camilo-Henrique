from app import db
from .enums import TipoRelatorio

estadia_relatorio = db.Table(
    'estadia_relatorio',
    db.Column('relatorio_id', db.Integer, db.ForeignKey('relatorio.id'), primary_key=True),
    db.Column('estadia_id', db.Integer, db.ForeignKey('estadia.id'), primary_key=True)
)

class Relatorio(db.Model):
    __tablename__ = 'relatorio'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Enum(TipoRelatorio), nullable=False)
    geracao = db.Column(db.DateTime, nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    vigenciaDias = db.Column(db.Integer, nullable=True)
    
    # Relacionamentos
    estadias = db.relationship('Estadia',
                                secondary=estadia_relatorio,
                                backref=db.backref('relatorios', lazy=True))