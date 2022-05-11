from flask import Flask, render_template, flash, request, jsonify, url_for, redirect, session, flash
import json

from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

from flask_cors import CORS

app = Flask(__name__)

CORS(app)


app.permanent_session_lifetime = timedelta(days=3)
app.secret_key = "ZRkK1RRZW8YWYKa72ohmCFeUQNh4tN1JA4ExYP2rzzT7"

class objeto:
    def __init__(self, peso, altura, largura, comprimento, valor):
        
        self.peso = peso
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento
        self.valor = valor

    def cubagem(self, cubo):
        
        volume = self.altura * self.largura * self.comprimento
        cubagem = volume / cubo  

        return cubagem

# Estrutura banco de dados

# class clients(db.Model):
#     _id = db.Column("id", db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     passwd = db.Column(db.String(100))
#     nome = db.Column(db.String(100))
#     sobrenome = db.Column(db.String(100))
#     telefone = db.Column(db.String(100), unique=True)
#     cpf = db.Column(db.String(100), unique=True)
#     data = db.Column(db.String(100))
#     status = db.Column(db.String(1))


# class address(db.Model):
#     _id = db.Column("id", db.Integer, primary_key=True)
#     rua = db.Column(db.String(100))
#     cidade = db.Column(db.String(100))
#     bairro = db.Column(db.String(100))
#     numero = db.Column(db.Integer)
#     complemento = db.Column(db.String(100))
#     cep = db.Column(db.String(11))
#     infos = db.Column(db.String(300))
#     idOwner = db.Column(db.Integer)


@app.route('/')
def main():    
    return render_template('index.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':

        email = request.form["user"]
        passwd = request.form["passwd"]

        headers = {
                'Content-Type': 'application/json'
        }

        data = {
            "email": email,
            "passwd": passwd
        }

        data = json.dumps(data)

        url = "http://18.228.16.239/login/" 
        status = requests.post(url, data=data, headers=headers)

        status = status.json()
        
        if status['status']:
            session['id'] = status["id"]
            return redirect(url_for('user'))

        else:
            return render_template('login.html')


    else:
        return render_template('login.html')

@app.route('/cadastro/', methods=['POST', 'GET'])
def cadastro():
    
    if request.method == 'POST':
        
        email = request.form["user"]
        passwd = request.form["passwd"]
        passwd2 = request.form["passwd2"]

        if passwd == passwd2:

            headers = {
                'Content-Type': 'application/json'
            }

            data = {
                "email": email,
                "passwd": passwd
            }

            data = json.dumps(data)

            url = "http://18.228.16.239/cadastro/" 
            status = requests.post(url, data=data, headers=headers)

            return redirect(url_for('login'))
        
        else: 
            return render_template('cadastroPasswd.html')

    else:
        return render_template('cadastro.html')

@app.route('/user/', methods=['POST', 'GET'])
def user():
    
    if request.method == 'POST':
        pass
    else:
        return render_template('user.html')

@app.route('/busca/', methods=['POST', 'GET'])
def resultado():
    pass

if __name__ == '__main__':
    app.run(debug=True)
