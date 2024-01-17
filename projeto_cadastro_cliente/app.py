
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de clientes (por simplicidade, use uma lista; em um projeto real, use um banco de dados)
clientes = []

@app.route('/')
def cadastro():
    return render_template('cadastro.html', clientes=clientes)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    idade = request.form['idade']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    cidade = request.form['cidade']
    estado = request.form['estado']

    cliente = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'idade': idade,
        'cpf': cpf,
        'endereco': endereco,
        'cidade': cidade,
        'estado': estado
    }

    clientes.append(cliente)
    return redirect(url_for('cadastro'))

if __name__ == '__main__':
    app.run(debug=True)
