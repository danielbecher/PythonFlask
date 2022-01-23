#Importa as bibliotecas e funções separadas necessárias
from flask import Flask, render_template, request
from rastrearencomenda import rastrear
from consultacep import consultarCep


#Cria o objeto app
app = Flask(__name__)

#Cria a página inicial "/"
@app.route('/', methods=['POST','GET'])
def inicio():
    return render_template('index.html')

#Cria a página de rastreamento
@app.route('/rastreio', methods=['POST','GET'])
def inicioRastreio():
    return render_template('rastreio.html')

#Cria a página de resposta do rastreamento
@app.route('/rastreio-consulta', methods=['GET','POST'])
def rastreioConsulta():
    codeguim = request.form.get('codigorastreio')
    rastrear(codeguim)
    return render_template('rastreio-consulta.html', codeguim=codeguim, listaeventos2=rastrear(codeguim))

#Cria a página de CEP
@app.route('/cep', methods=['POST','GET'])
def iniciocep():
    return render_template('cep.html')

#Cria a página de resposta do CEP
@app.route('/cep-consulta', methods=['POST','GET'])
def cepConsulta():
    cep = request.form.get('cep')
    consultarCep(cep)
    return render_template('cep-consulta.html',cep=cep, dadoscep=consultarCep(cep))

#Debug=True eu usei para que a cada salvamento do código, ele reiniciasse o app sem precisar dar reload.
app.run(debug=True)