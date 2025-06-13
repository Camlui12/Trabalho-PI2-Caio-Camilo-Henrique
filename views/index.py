from flask import render_template, request, redirect, url_for, session
from app import app
from models import Usuario

@app.route('/')
def index():
    if 'usuario_logado' in session:
        login = session['usuario_logado']
        tipo = session['tipo_usuario']
        user = Usuario.query.filter_by(login = login).first()
        nome = user.nome
        if tipo == 'admin':
            return render_template('index_adm.html', usuario = nome)
        if tipo == 'operador':
            return render_template('index_op.html', usuario = nome)
    return redirect(url_for('login'))


@app.route('/registro-entrada')
def registroEntrada():
    return render_template('registro_entrada.html')