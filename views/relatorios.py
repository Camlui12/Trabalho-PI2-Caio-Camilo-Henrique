from flask import render_template, request, redirect, url_for, session
from app import app, db 
from models import *
from datetime import datetime, timezone, date, timedelta
from views import core

@app.route('/relatorios', methods=['GET', 'POST'])
def relatorios():
    
    if 'usuario_logado' not in session or session['tipo_usuario'] != 'admin':
            return redirect(url_for('login'))
    
    # Verificando qual o metodo HTTP
    if request.method == 'GET':
        met = 'get'
        relatorios = Relatorio.query.all()
        last_relatorio = relatorios[-1] if relatorios else None
        data_hj = date.today()
        print(f"Data de hoje: {data_hj}")

        # Se não houver relatório, cria um exemplo para exibir gráfico
        if not last_relatorio:
            from models.enums import TipoRelatorio, TipoVigencia
            class Dummy:
                pass
            last_relatorio = Dummy()
            last_relatorio.tipo = TipoRelatorio.ESTADIA
            last_relatorio.vigenciaDias = TipoVigencia.DIARIO
            last_relatorio.conteudo = {
                'entradas': [12, 19, 7, 5, 2, 3, 9]
            }

        return render_template('gerar_relatorio.html',
                                relatorios=relatorios,
                                last_relatorio=last_relatorio,
                                data_hj=data_hj,
                                met=met)
    
    elif request.method == 'POST':
        met = 'post'
        tipo_relatorio = request.form.get('tipo')
        vigencia_dias = request.form.get('vigencia')
        if not tipo_relatorio or not vigencia_dias:
            return redirect(url_for('relatorios'))
        relatorios = Relatorio.query.all()
        if relatorios:
            id = max(relatorio.id for relatorio in relatorios) + 1
        else:
            id = 1

        conteudo = {}
        from sqlalchemy import func, extract
        if tipo_relatorio == 'ESTADIA':
            if vigencia_dias == 'DIARIO':
                # Entradas por dia da semana (últimos 7 dias)
                hoje = date.today()
                dias = [hoje - timedelta(days=i) for i in range(6, -1, -1)]
                entradas = [
                    db.session.query(func.count()).filter(
                        func.date(Estadia.entrada) == d
                    ).scalar() for d in dias
                ]
                conteudo = {'entradas': entradas}
            elif vigencia_dias == 'SEMANAL':
                # Entradas por semana do mês atual
                hoje = date.today()
                ano, mes = hoje.year, hoje.month
                semanas = [1, 2, 3, 4]
                estadias = []
                for semana in semanas:
                    inicio = date(ano, mes, 1) + timedelta(days=(semana-1)*7)
                    fim = inicio + timedelta(days=6)
                    count = db.session.query(func.count()).filter(
                        Estadia.entrada >= inicio,
                        Estadia.entrada <= fim
                    ).scalar()
                    estadias.append(count)
                conteudo = {'estadias': estadias}
            elif vigencia_dias == 'MENSAL':
                # Entradas por mês do ano atual
                hoje = date.today()
                ano = hoje.year
                estadias = []
                for mes in range(1, 7):
                    count = db.session.query(func.count()).filter(
                        extract('year', Estadia.entrada) == ano,
                        extract('month', Estadia.entrada) == mes
                    ).scalar()
                    estadias.append(count)
                conteudo = {'estadias': estadias}
        elif tipo_relatorio == 'FINANCEIRO':
            if vigencia_dias == 'DIARIO':
                # Receita por dia da semana (últimos 7 dias)
                hoje = date.today()
                dias = [hoje - timedelta(days=i) for i in range(6, -1, -1)]
                receita = [
                    db.session.query(func.sum(Estadia.valor)).filter(
                        func.date(Estadia.saida) == d
                    ).scalar() or 0 for d in dias
                ]
                conteudo = {'receita': receita}
            elif vigencia_dias == 'SEMANAL':
                # Receita por semana do mês atual
                hoje = date.today()
                ano, mes = hoje.year, hoje.month
                semanas = [1, 2, 3, 4]
                receita = []
                for semana in semanas:
                    inicio = date(ano, mes, 1) + timedelta(days=(semana-1)*7)
                    fim = inicio + timedelta(days=6)
                    soma = db.session.query(func.sum(Estadia.valor)).filter(
                        Estadia.saida >= inicio,
                        Estadia.saida <= fim
                    ).scalar() or 0
                    receita.append(soma)
                conteudo = {'receita': receita}
            elif vigencia_dias == 'MENSAL':
                # Receita por mês do ano atual
                hoje = date.today()
                ano = hoje.year
                receita = []
                for mes in range(1, 7):
                    soma = db.session.query(func.sum(Estadia.valor)).filter(
                        extract('year', Estadia.saida) == ano,
                        extract('month', Estadia.saida) == mes
                    ).scalar() or 0
                    receita.append(soma)
                conteudo = {'receita': receita}

        from models.enums import TipoRelatorio, TipoVigencia
        relatorio = Relatorio(
            id=id,
            tipo=TipoRelatorio[tipo_relatorio],
            geracao=datetime.now(timezone.utc),
            conteudo=conteudo,
            vigenciaDias=TipoVigencia[vigencia_dias]
        )
        db.session.add(relatorio)
        db.session.commit()
        return redirect(url_for('ver_relatorio', id=relatorio.id))

@app.route('/ver_relatorio/<int:id>')
def ver_relatorio(id):
    if 'usuario_logado' not in session or session['tipo_usuario'] != 'admin':
        return redirect(url_for('login'))
    
    relatorio = Relatorio.query.get_or_404(id)
    if not relatorio:
        return redirect(url_for('relatorios'))
    
    relatorios = Relatorio.query.all()
    
    # Reaproveita o mesmo template de gráficos dinâmicos
    return render_template(
        'gerar_relatorio.html',
        relatorios=relatorios,
        last_relatorio=relatorio,
        data_hj=relatorio.geracao.date() if relatorio.geracao else '',
        met='detalhe'
    )