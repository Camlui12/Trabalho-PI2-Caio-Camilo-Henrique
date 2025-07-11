from app import db
from datetime import datetime, timezone

class LogPedidoRelatorio(db.Model):
    __tablename__ = 'log_pedido_relatorio'
    
    __bind_key__ = 'baratinha'
    
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, nullable=False, index=True)
    data_pedido = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc), index=True)
    tipo_relatorio = db.Column(db.String(50), nullable=False, index=True)