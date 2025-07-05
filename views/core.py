from app import app, db
from flask import render_template, request, redirect, url_for, session

@app.route('/confirmacao')
def confirmacao():
    return render_template('confirmacao.html')