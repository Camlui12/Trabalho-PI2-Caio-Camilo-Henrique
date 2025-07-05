from app import app, db
from flask import render_template, request, redirect, url_for, session
from models import Veiculo, Estadia, Tarifa
from datetime import datetime, timezone, date
from views import core


@app.route('/confirmarEntrada', methods=['GET', 'POST'])
def confirmarEntrada():    
    carro = Veiculo.query.filter_by(placa=request.form.get('placa')).first()
    placa = request.form.get('placa')
    if carro:
        estadia_ativa = Estadia.query.filter_by(veiculo=placa, saida=None).first()
        if estadia_ativa:
            return redirect(url_for('index'))
        
        tarifa = Tarifa.query.order_by(Tarifa.dataVigencia.desc()).first()
        
        tarifa_id = tarifa.id if tarifa else None
        
        # Pegando a data de hoje

        # Cria a nova estadia
        nova_estadia = Estadia(entrada=datetime.now(timezone.utc),veiculo=placa,tarifa=tarifa_id)
        db.session.add(nova_estadia)
        db.session.commit()

        return redirect(url_for('confirmacao'))  # Sucesso
    else:
        return render_template('cadastro_veiculo.html', placa=placa)#não sei se aqui é melhor render ou redirect
    

@app.route('/cadastrarVeiculo', methods=['POST'])
def cadastrarVeiculo():
    placa = request.form['placa']
    modelo = request.form['modelo']
    cor = request.form['cor']
    tipo = request.form['tipo']

    newVeiculo = Veiculo(placa = placa, modelo = modelo, cor = cor, tipo = tipo)
    db.session.add(newVeiculo)
    db.session.commit()
    
    print(f"Veículo {placa} cadastrado com sucesso!")

    return redirect(url_for('registroEntrada'))

@app.route('/registro-saida')
def registroSaida():
    return render_template('registro_saida.html')

@app.route('/confirmarSaida', methods=['POST'])
def confirmarSaida():
    placa = request.form['placa']
    print(f"Placa recebida: {placa}")

    estadia = Estadia.query.filter_by(veiculo=placa, saida=None).first()
    tarifa_id = estadia.tarifa if estadia else None
    tarifa = Tarifa.query.get(tarifa_id) if tarifa_id else None

    # Corrige o timezone da entrada
    if estadia and estadia.entrada.tzinfo is None:
        entrada = estadia.entrada.replace(tzinfo=timezone.utc)
    elif estadia:
        entrada = estadia.entrada
    else:
        entrada = None

    periodo = datetime.now(timezone.utc) - entrada if entrada else None
    
    # Verificando se o período de permanência é maior que a tolerância
    if tarifa and periodo:
        tolerancia = tarifa.tolerancia
        if periodo.total_seconds() / 60 > tolerancia:
            # Calcula o valor a pagar
            horas = periodo.total_seconds() / 3600
            valor = tarifa.valorHora * horas
            
            # Verifica se o valor ultrapassa o teto diário
            if valor > tarifa.tetoDiario:
                valor = tarifa.tetoDiario
            if valor < tarifa.valorHora:
                valor = tarifa.valorHora
                
            valor_final = round(valor, 2)
            
            print(f"Valor a pagar: R$ {valor_final}")
        else:
            valor_final = round(0,2)
            print("Período dentro da tolerância, sem cobrança.")
    
    if estadia:
        estadia.saida = datetime.now(timezone.utc)
        estadia.valor = valor_final
        db.session.commit()
        print(f"Saída registrada para o veículo {placa}.")
        return redirect(url_for('confirmacao'))
    else:
        return render_template('registro_saida.html', error="Veículo não encontrado ou já saiu.")