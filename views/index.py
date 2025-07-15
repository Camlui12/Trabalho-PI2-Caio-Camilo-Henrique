from flask import render_template, request, redirect, url_for, session
from app import app
from models import Usuario, Estadia, Tarifa

@app.route('/')
def index():
    if 'usuario_logado' in session:
        login = session['usuario_logado']
        tipo = session['tipo_usuario']
        user = Usuario.query.filter_by(login = login).first()
        nome = user.nome
        estadias = Estadia.query.all()
        vagas_ocupadas = Estadia.query.filter(Estadia.saida == None).count()
        vagas_totais = 100
        vagas_disponiveis = vagas_totais - vagas_ocupadas
        
        if tipo == 'admin':
            return render_template('index_adm.html', usuario = nome, vagas_disponiveis = vagas_disponiveis, vagas_totais = vagas_totais, vagas_ocupadas = vagas_ocupadas)
        if tipo == 'operador':
            return render_template('index_op.html', usuario = nome, vagas_disponiveis = vagas_disponiveis, vagas_totais = vagas_totais, vagas_ocupadas = vagas_ocupadas)
    return redirect(url_for('login'))

@app.route('/registro-entrada')
def registroEntrada():
    return render_template('registro_entrada.html')

@app.route('/mensalistas')
def mensalistas():
    return render_template('mensalistas.html')

@app.route('/mensalistas-op')
def mensalistasOp():
    return render_template('mensalistas_op.html')

@app.route('/configuracao-cobranca')
def configuracaoCobranca():
    lastTarifa = Tarifa.query.order_by(Tarifa.dataVigencia.desc()).first()
    tarifa_formatada = f'R${lastTarifa.valorHora:.2f}'.replace('.', ',')
    tetoFormatado = f'R${lastTarifa.tetoDiario:.2f}'.replace('.',',')
    return render_template('configuracao_cobranca.html', tarifa = tarifa_formatada, tolerancia = lastTarifa.tolerancia, teto = tetoFormatado)