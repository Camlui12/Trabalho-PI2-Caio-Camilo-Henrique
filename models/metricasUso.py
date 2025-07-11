from app import db

class MetricasUso(db.Model):
    __tablename__ = 'metricas_uso'
    
    __bind_key__ = 'baratinha'  # Define o bind para a tabela específica
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False, index=True)
    acessos = db.Column(db.Integer, nullable=False, default=0)  # Número de acessos ao sistema
    registros_entrada = db.Column(db.Integer, nullable=False, default=0)  # Registros de entrada
    registros_saida = db.Column(db.Integer, nullable=False, default=0)  # Registros de saída
    registros_gerados = db.Column(db.Integer, nullable=False, default=0)  # Registros gerados
