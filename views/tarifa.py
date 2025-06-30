from app import app, db
from flask import render_template, request, redirect, url_for, session
from models import Tarifa
from datetime import date


@app.route('/atualizartarifa', methods = ['POST'])
def atualizarTarifa():
    tarifa = request.form['tarifa']
    tarifa_limpo = tarifa.replace('R$', '').strip()
    tarifa_ponto = tarifa_limpo.replace(',', '.')
    tarifa_float = float(tarifa_ponto)
    tolerancia = request.form['tolerancia']
    teto = request.form['teto']
    teto_limpo = teto.replace('R$', '').strip()
    teto_ponto = teto_limpo.replace(',', '.')
    teto_float = float(teto_ponto)

    lastTarifa = Tarifa.query.order_by(Tarifa.dataVigencia.desc()).first()
    id = lastTarifa.id + 1

    nova_tarifa = Tarifa(id = id, valorHora = tarifa_float, tolerancia = tolerancia, tetoDiario = teto_float, dataVigencia = date.today())
    db.session.add(nova_tarifa)
    db.session.commit()
    print(f'tarifa de valor {tarifa_float:.2f} adicionada')
    return redirect(url_for('index'))
