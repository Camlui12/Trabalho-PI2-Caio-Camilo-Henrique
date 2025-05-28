from app import app
from flask import render_template, request, redirect, url_for, session

@app.route('/login')
def login():
    return render_template('login.html')