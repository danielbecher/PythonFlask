from flask import Flask, render_template, request
from rastrearencomenda import rastrear

app = Flask(__name__)

#Cria a página inicial de consula
@app.route('/', methods=['POST','GET'])
def inicio():
    return render_template('index.html')

#Cria a página de resposta da consulta
@app.route('/consulta', methods=['GET','POST'])
def consulta():
    codeguim = request.form.get('codigorastreio')
    rastrear(codeguim)
    return render_template('consulta.html', codeguim=codeguim, listaeventos2=rastrear(codeguim))

app.run(debug=True)