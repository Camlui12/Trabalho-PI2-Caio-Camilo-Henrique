from app import app, db, cache
from flask import render_template, request, redirect, url_for, session, jsonify
from models import ClienteMensal,Veiculo, PlanoMensal
from views import core
from datetime import date

@app.route('/novo-mensalista')
def novoMensalista(): 
    return render_template('novo_mensalista.html')

@app.route('/remover-mensalista')
def removerMensalista():
    return render_template('remover_mensalista.html')

@app.route('/valor-mensal')
def valorMensal():
    return render_template('valor_mensal.html')

@app.route('/Confirmar-cliente', methods = ['POST'])
def confirmarCliente():
    nome = request.form['nome']
    cpf = request.form['cpf']
    placa = request.form['placa']
    veiculo = Veiculo.query.filter_by(placa=placa).first()
    valor = 100

    if ClienteMensal.query.filter_by(cpf = cpf).first():
        return redirect(url_for('novoMensalista'))
    if veiculo:
        clientes = ClienteMensal.query.all()
        if clientes:
            id = max(cliente.id for cliente in clientes) + 1
        else:
            id = 1
        novoCliente = ClienteMensal(id = id, nome = nome, cpf = cpf, valor = valor)
        db.session.add(novoCliente)
        veiculo.cliente_mensal_id = id
        db.session.commit()
        return redirect(url_for('confirmacao'))
    else:
        return render_template('cadastro_veiculo.html', placa = placa)
    
@app.route('/atualizar-valor-mensal', methods=['POST'])
def atualizar_atualizar_valor_mensal():
    novo_valor = request.form['novo_valor_tarifa']
    novo_valor_limpo = novo_valor.replace('R$', '').strip()
    novo_valor_ponto = novo_valor_limpo.replace(',', '.')
    novo_valor_float = float(novo_valor_ponto)

    #pegando o plano mensal mais recente
    ultimo_plano = PlanoMensal.query.order_by(PlanoMensal.data.desc()).first()
    if ultimo_plano:
        id = ultimo_plano.id + 1
    else:
        id = 1
        
    try:
        novo_plano = PlanoMensal(id=id, data=date.today(), valor=novo_valor_float)
        db.session.add(novo_plano)
        db.session.commit()
    except Exception as e:
        print(f"Erro ao atualizar o valor mensal: {e}")
        return render_template('valor_mensal.html', error="Erro ao atualizar o valor mensal.")

    return redirect(url_for('confirmacao'))
    
