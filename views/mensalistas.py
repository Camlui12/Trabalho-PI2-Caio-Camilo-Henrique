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
    lista_de_clientes = ClienteMensal.query.order_by(ClienteMensal.nome).all()
    return render_template('remover_mensalista.html', clientes = lista_de_clientes)

@app.route('/valor-mensal')
def valorMensal():
    lastValor = PlanoMensal.query.order_by(PlanoMensal.data.desc()).first()
    valorFormatado = f'R${lastValor.valor:.2f}'.replace('.',',')
    return render_template('valor_mensal.html', valor = valorFormatado)

@app.route('/Confirmar-cliente', methods = ['POST'])
def confirmarCliente():
    nome = request.form['nome']
    cpf = request.form['cpf']
    placa = request.form['placa']
    veiculo = Veiculo.query.filter_by(placa=placa).first()
    PlanoAtual = PlanoMensal.query.order_by(PlanoMensal.data.desc()).first()

    if ClienteMensal.query.filter_by(cpf = cpf).first():
        return redirect(url_for('erro', mensagem_de_erro = 'Esse cpf já é cliente mensal.'))
    if veiculo:
        novoCliente = ClienteMensal(nome = nome, cpf = cpf, plano_id = PlanoAtual.id)
        db.session.add(novoCliente)
        veiculo.cliente_mensal_id = cpf
        db.session.commit()
        return redirect(url_for('confirmacao', mensagem = 'Cliente registrado.'))
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
        return redirect(url_for('erro', mensagem_de_erro = 'Erro ao atualizar valor mensal'))

    return redirect(url_for('confirmacao', mensagem = 'Valor mensal atualizado.'))
    
@app.route('/confirmar-remocao-mensalista', methods=['POST'])
def confirmarRemocaoMensalista():
    ids_dos_clientes_selecionados = request.form.getlist('selecionados')
    if not ids_dos_clientes_selecionados:
        return redirect(url_for('removerMensalista'))
    try:
        for cliente_cpf in ids_dos_clientes_selecionados:
            cliente_a_remover = ClienteMensal.query.get(cliente_cpf)
            
            if cliente_a_remover:
                db.session.delete(cliente_a_remover)
                
        db.session.commit()
    
    except Exception as e:
        db.session.rollback()
        print(f"Erro ao remover clientes: {e}")

    return redirect(url_for('confirmacao', mensagem = 'Cliente(s) removido(s) com sucesso.'))