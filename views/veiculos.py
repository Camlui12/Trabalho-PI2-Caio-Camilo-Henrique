from app import app
from flask import render_template, request, redirect, url_for, session
from models import Veiculo


@app.route('/confirmarEntrada', methods=['POST'])

def confirmarEntrada():#não consegui testar pq n tem nd no banco de dados sobre as placas eu acho    
    carro = Veiculo.query.filter_by(placa=request.form.get('placa')).first()
    if carro:
        return redirect(url_for('index'))#confimação que entrada foi registrada
    else:
        return render_template('cadastro_veiculo.html')#não sei se aqui é melhor render ou redirect
        
        
       