from .enums import TipoUsuario
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.Enum(TipoUsuario), nullable=False)
    
    __mapper_args__ = {
        'polymorphic_on': tipo
    }

class Admin(Usuario):
    __mapper_args__ = {
        'polymorphic_identity': TipoUsuario.ADMIN
    }

class Operador(Usuario):
    __mapper_args__ = {
        'polymorphic_identity': TipoUsuario.OPERADOR
        }
