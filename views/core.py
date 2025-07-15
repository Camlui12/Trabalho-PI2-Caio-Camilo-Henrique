from app import app, db
from flask import render_template, request, redirect, url_for, session

@app.route('/confirmacao')
def confirmacao():
    mensagem_da_url = request.args.get('mensagem')
    return render_template('confirmacao.html', mensagem = mensagem_da_url)

@app.route('/erro')
def erro():
    mensagem_da_url = request.args.get('mensagem_de_erro')
    return render_template('erro.html', mensagem_de_erro = mensagem_da_url)