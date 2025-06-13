from app import app
from flask import render_template, request, redirect, url_for, session
from models import Usuario

mensagem = ''

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    global mensagem
    
    user = Usuario.query.filter_by(login=request.form.get('usuario')).first()
    if user:
        if request.form.get('senha') == user.senha:
            
            session['usuario_logado'] = user.login
            session['tipo_usuario'] = user.tipo.value
            
            mensagem = ''
            
            return redirect(url_for('index'))
        else:
            mensagem = 'Usuário ou senha inválidos'
            redirect(url_for('login'))
        
    else: 
        mensagem = 'Usuario ou sehna inválidos'
        return redirect(url_for('login'))
