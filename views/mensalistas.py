from app import app, db
from flask import render_template, request, redirect, url_for, session
from models import ClienteMensal,Veiculo
from views import core

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
    
