from flask import render_template, request, redirect, url_for, session
from app import app

@app.route('/')
def index():
    if 'usuario_logado' in session:
        return render_template('index.html')
    return redirect(url_for('login'))