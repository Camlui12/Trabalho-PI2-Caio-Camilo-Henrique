from flask import render_template, request, redirect, url_for, session
from app import app, db 
from models import *
from datetime import datetime, timezone
from views import core

@app.route('/relatorios')
def relatorios():
    if 'usuario_logado' not in session or session['tipo_usuario'] != 'ADMIN':
        return redirect(url_for('login'))
    
    return render_template('gerar_relatorios.html')

@app.route('/relatorios/<int:id>')
def relatorio_detalhes(id):
    if 'usuario_logado' not in session or session['tipo_usuario'] != 'ADMIN':
        return redirect(url_for('login'))
    
    relatorio = Relatorio.query.get_or_404(id)
    if not relatorio:
        return redirect(url_for('relatorios'))
    
    return render_template('detalhes_relatorio.html', relatorio=relatorio)

@app.route('/gerar-relatorio', methods=['POST'])
def gerar_relatorio():
    if 'usuario_logado' not in session or session['tipo_usuario'] != 'ADMIN':
        return redirect(url_for('login'))
    
    tipo_relatorio = request.form.get('tipo')
    vigencia_dias = request.form.get('vigencia')
    
    relatorios = Relatorio.query.all()
    if relatorios:
        id = max(relatorio.id for relatorio in relatorios) + 1
    else:
        id = 1
    
    if tipo_relatorio == 'financeiro':
        
        # Implementar lógica para gerar relatório financeiro
        conteudo = {
            
        }
    
    relatorio = Relatorio(id=id, tipo=TipoRelatorio[tipo_relatorio], geracao=datetime.now(timezone.utc), conteudo={}, vigenciaDias=vigencia_dias)
    
    db.session.add(relatorio)
    db.session.commit()
    
    return redirect(url_for('relatorio_detalhes', id=relatorio.id))