from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

# Listas para armazenar despesas e receitas
despesas = []
receitas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar_despesa', methods=['POST'])
def registrar_despesa():
    try:
        valor = float(request.form['valor'])
        descricao = request.form['descricao']
        data_insercao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        despesas.append({'valor': valor, 'descricao': descricao, 'data': data_insercao})
    except ValueError:
        return redirect(url_for('index'))  # Redireciona em caso de erro
    return redirect(url_for('index'))

@app.route('/registrar_receita', methods=['POST'])
def registrar_receita():
    try:
        valor = float(request.form['valor'])
        descricao = request.form['descricao']
        data_insercao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        receitas.append({'valor': valor, 'descricao': descricao, 'data': data_insercao})
    except ValueError:
        return redirect(url_for('index'))  # Redireciona em caso de erro
    return redirect(url_for('index'))

@app.route('/consultar', methods=['GET', 'POST'])
def consultar():
    if request.method == 'POST':
        periodo = request.form['periodo']
        if periodo == 'dia':
            data_limite = datetime.now() - timedelta(days=1)
        elif periodo == 'semana':
            data_limite = datetime.now() - timedelta(weeks=1)
        elif periodo == 'mes':
            data_limite = datetime.now() - timedelta(days=30)
        elif periodo == 'ano':
            data_limite = datetime.now() - timedelta(days=365)
        
        despesas_filtradas = [d for d in despesas if datetime.strptime(d['data'], "%Y-%m-%d %H:%M:%S") >= data_limite]
        receitas_filtradas = [r for r in receitas if datetime.strptime(r['data'], "%Y-%m-%d %H:%M:%S") >= data_limite]
        
        return render_template('resumo.html', despesas=despesas_filtradas, receitas=receitas_filtradas, saldo_liquido=sum(r['valor'] for r in receitas_filtradas) - sum(d['valor'] for d in despesas_filtradas))
    
    return render_template('consultar.html')

@app.route('/resumo')
def resumo():
    total_despesas = sum(d['valor'] for d in despesas)
    total_receitas = sum(r['valor'] for r in receitas)
    saldo_liquido = total_receitas - total_despesas
    return render_template('resumo.html', despesas=despesas, receitas=receitas, saldo_liquido=saldo_liquido)

if __name__ == '__main__':
    app.run(debug=True)
