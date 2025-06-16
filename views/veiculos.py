from app import app
from flask import render_template, request, redirect, url_for, session
from models import Veiculo, Estadia
from datetime import datetime, timezone


@app.route('/confirmarEntrada', methods=['GET', 'POST'])
def confirmarEntrada():#não consegui testar pq n tem nd no banco de dados sobre as placas eu acho    
    carro = Veiculo.query.filter_by(placa=request.form.get('placa')).first()
    placa = request.form.get('placa')
    if carro:
        estadia_ativa = Estadia.query.filter_by(veiculo=placa, saida=None).first()
        if estadia_ativa:
            return redirect(url_for('index'))
        
        #tarifa_id

        # Cria a nova estadia
        #nova_estadia = Estadia(entrada=datetime.now(timezone.utc),veiculo=placa,tarifa=tarifa_id)
        #db.session.add(nova_estadia)
        #db.session.commit()

        return redirect(url_for('index'))  # Sucesso
    else:
        return render_template('cadastro_veiculo.html')#não sei se aqui é melhor render ou redirect
    

@app.route('/cadastrarVeiculo', methods=['POST'])
def cadastrarVeiculo():
    placa = request.form['placa']
    modelo = request.form['modelo']
    cor = request.form['cor']
    tipo = request.form['tipo']

    newVeiculo = Veiculo(placa = placa, modelo = modelo, cor = cor, tipo = tipo)
    #db.session.add(newVeiculo)
    #db.session.comit()

    return redirect(url_for('confirmarEntrada', placa = placa))

        
        
       