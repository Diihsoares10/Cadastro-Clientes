from flask import Flask, render_template, session, redirect, jsonify, url_for, flash, request, current_app, send_file
from app.main.forms import *
from .. import main
from sqlalchemy import asc, desc
from datetime import datetime
import pandas as pd 
from app import app

clientes = []

@main.route('/cadastro', methods=["GET","POST"])
def cadastro():
# Lista de clientes (por simplicidade, use uma lista; em um projeto real, use um banco de dados)

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
    return render_template('cadastro.html', clientes=clientes)
