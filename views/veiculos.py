from app import app, db
from flask import render_template, request, redirect, url_for, session
from models import Veiculo, Estadia, Tarifa
from datetime import datetime, timezone, date
from views import core
from sqlalchemy.orm import joinedload


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
        
        # Verifica se há vagas disponíveis
        vagas_ocupadas = Estadia.query.filter(Estadia.saida == None).count()
        vagas_totais = 100  # Defina o número total de vagas conforme sua lógica
        vagas_disponiveis = vagas_totais - vagas_ocupadas
        
        if vagas_disponiveis <= 0:
            return render_template('registro_entrada.html', error="Não há vagas disponíveis.")

        # Cria a nova estadia
        nova_estadia = Estadia(entrada=datetime.now(timezone.utc),veiculo=placa,tarifa=tarifa_id)
        db.session.add(nova_estadia)
        db.session.commit()

        return redirect(url_for('confirmacao'))  # Sucesso
    else:
        return render_template('cadastro_veiculo.html', placa=placa) #não sei se aqui é melhor render ou redirect
    

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

    estadia = Estadia.query.options(joinedload(Estadia.tarifa)).filter_by(veiculo=placa, saida=None).first()
    
    if not estadia or not estadia.tarifa:
        print(f"Estadia não encontrada ou já finalizada para o veículo {placa}.")
        return render_template('registro_saida.html', error="Veículo não encontrado ou já saiu.")
    
    tarifa = estadia.tarifa if estadia else None
    agora_utc = datetime.now(timezone.utc)
    valor_final = 0.0

    # Corrige o timezone da entrada
    if estadia and estadia.entrada.tzinfo is None:
        entrada = estadia.entrada.replace(tzinfo=timezone.utc)
    elif estadia:
        entrada = estadia.entrada
    else:
        entrada = None

    periodo = agora_utc - entrada if entrada else None
    
    # Verificando se o período de permanência é maior que a tolerância
    if tarifa and periodo:
        if periodo.total_seconds() / 60 > tarifa.tolerancia:
            # Calcula o valor a pagar
            horas = max(1, periodo.total_seconds() / 3600)
            valor_calculado = tarifa.valorHora * horas
            
            valor_final = min(valor_calculado, tarifa.tetoDiario)
            print(f"Período excedido. Valor a pagar: R$ {valor_final:.2f}")
    
    if estadia:
        estadia.saida = agora_utc
        estadia.valor = round(valor_final, 2)
        db.session.commit()
        print(f"Saída registrada para o veículo {placa}.")
        return redirect(url_for('confirmacao'), valor_cobrado = f"{valor_final:.2f}")