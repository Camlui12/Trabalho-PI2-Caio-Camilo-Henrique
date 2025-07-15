from app import db
from .enums import TipoRelatorio, TipoVigencia
from sqlalchemy.dialects.mysql import JSON

estadia_relatorio = db.Table(
    'estadia_relatorio',
    db.Column('relatorio_id', db.Integer, db.ForeignKey('relatorio.id'), primary_key=True),
    db.Column('estadia_id', db.Integer, db.ForeignKey('estadia.id'), primary_key=True),
    db.Index('idx_estadiarelatorio_relatorio_id', 'relatorio_id'),
    db.Index('idx_estadiarelatorio_estadia_id', 'estadia_id')
)

class Relatorio(db.Model):
    __tablename__ = 'relatorio'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Enum(TipoRelatorio), nullable=False, index=True)
    geracao = db.Column(db.DateTime, nullable=False, index=True)
    conteudo = db.Column(JSON, nullable=False)
    vigenciaDias = db.Column(db.Enum(TipoVigencia), nullable=True)
    
    # Relacionamentos
    estadias = db.relationship('Estadia',
                                secondary=estadia_relatorio,
                                backref=db.backref('relatorios', lazy=True))

    __table_args__ = (
        db.Index('idx_relatorio_tipo_geracao', 'tipo', 'geracao'),
    )