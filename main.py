from flask import Flask, render_template, flash, request, jsonify, url_for, redirect, session, flash
from api import *
import json

from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pedrosantb:20112001p@localhost/praja'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

class clients(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    passwd = db.Column(db.String(100))
    nome = db.Column(db.String(100))
    sobrenome = db.Column(db.String(100))
    telefone = db.Column(db.String(100), unique=True)
    cpf = db.Column(db.String(100), unique=True)
    data = db.Column(db.String(100))
    status = db.Column(db.String(1))


class address(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    rua = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    numero = db.Column(db.Integer)
    complemento = db.Column(db.String(100))
    cep = db.Column(db.String(11))
    infos = db.Column(db.String(300))
    idOwner = db.Column(db.Integer)


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
            return render_template('login.html', error='Usuario ou senha invalidos')


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

# @app.route('/simulador/', methods=['POST', 'GET'])
# def simulador():
#     global valorJad

#     if request.method == 'POST':

#         cepOrig = request.form["cepOrig"]
#         cepDest = request.form["cepDest"]
#         altura = request.form["altura"]
#         largura = request.form["largura"]
#         comprimento = request.form["comprimento"]
#         peso = request.form["peso"]
#         valor = request.form["valor"]

#         dados = {
#                 "cepOrig": cepOrig,
#                 "cepDest": cepDest,
#                 "peso": peso,
#                 "pesoRodo" :"",
#                 "pesoAero": "",
#                 "valor": valor,
#                 "altura": altura,
#                 "largura": largura,
#                 "comprimento": comprimento
#             }

#         obj = objeto(float(peso), float(altura), float(largura), float(comprimento), float(valor))

#         dados["pesoRodo"] = obj.cubagem(3000)
#         dados["pesoAero"] = obj.cubagem(6000)
                
            
#         headers = {
#             'Content-Type': 'application/json'
#         }

#         url = '1234'

#         data = json.dumps(dados)

#         result = requests.post(url, headers=headers, data=data)
        
#         return render_template('resultado.html', VjadPkg=VjadPkg, prazoPkg=prazoPkg)
#     else:
#         return render_template('simulador.html')

# @app.route('/infos/<valor>', methods=['POST', 'GET'])
# def infos(valor):
#     if request.method == 'POST':

#         found_user = clients.query.filter_by(email='viniciusssa.alves@gmail.com').first()

#         print(found_user)
         
#         found_address = address.query.filter_by(_id=1).first()

#         url = "http://www.jadlog.com.br/embarcador/api/pedido/incluir"
#         headers = {

#             'Content-Type': 'application/json',
#             'Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOjcxMzcwLCJkdCI6IjIwMjAxMTE2In0.zwA3MRs4rzBnr7LSDgepLTja291K7giz4b5H29Jbh1w"
#         }
        
        
        
#         nomeRem = str(found_user.nome) + " " + str(found_user.sobrenome)

#         dados = {
#             "conteudo": "PENDRIVE",
#             "pedido": [
#                 "1"
#             ],
#             "totPeso": request.form["peso"],
#             "totValor": valor,
#             "obs": "OBS XXXXX",
#             "modalidade": 3,
#             "contaCorrente": "000001",
#             "tpColeta": "K",
#             "tipoFrete": 0,
#             "cdUnidadeOri": "1",
#             "cdUnidadeDes": None,
#             "cdPickupOri": None,
#             "cdPickupDes": "BR00001",
#             "nrContrato": 12345,
#             "servico": 1,
#             "shipmentId": None,
#             "vlColeta": None,
#             "rem": {
#                 "nome": nomeRem,
#                 "cnpjCpf": cpf,
#                 "ie": None,
#                 "endereco": found_address.rua,
#                 "numero": found_address.numero,
#                 "compl": None,
#                 "bairro": found_address.bairro,
#                 "cidade": found_address.cidade,
#                 "uf": "BA",
#                 "cep": found_address.cep,
#                 "fone": found_user.telefone,
#                 "cel": found_user.telefone,
#                 "email": found_user.email,
#                 "contato": found_user.nome
#             },
#             "des": {
#                 "nome": 'pedro',
#                 "cnpjCpf": request.form["cpf"],
#                 "ie": None,
#                 "endereco": request.form["rua"],
#                 "numero": request.form["numero"],
#                 "compl": None,
#                 "bairro": request.form["bairro"],
#                 "cidade": request.form["cidade"],
#                 "uf": request.form["UF"],
#                 "cep": request.form["cepDest"],
#                 "fone": request.form["fone"],
#                 "cel": request.form["fone"],
#                 "email": request.form["email"],
#                 "contato": request.form["dest"]
#             },
#             "dfe": [
#                 {
#                     "cfop": "6909",
#                     "danfeCte": "00000000000000000000000000000000000000000000",
#                     "nrDoc": "00000000",
#                     "serie": "0",
#                     "tpDocumento": 2,
#                     "valor": valor
#                 }
#             ],
#             "volume": [
#                 {
#                     "altura": request.form["altura"],
#                     "comprimento": request.form["comprimento"],
#                     "identificador": "1234567890",
#                     "largura": request.form["largura"],
#                     "peso": request.form["peso"]
#                 }
#             ]
#         }

#         data = json.dumps(dados)
#         cotacao = requests.post(url, data=data, headers=headers)
#         print(cotacao.text)
#         return cotacao.text

#     else:
#         return render_template('infos.html')

# @app.route('/checkout/', methods=['POST', 'GET'])
# def checkout():
    # if request.method == 'POST':
    #     pass

if __name__ == '__main__':
    app.run(debug=True)
