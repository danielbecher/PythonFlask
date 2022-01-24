#ConsultaCEP
#importa as bibliotecas
import requests

def consultarCep(cep):
    dadoscep = []
    #verifica o cep válido
    if len(cep) != 8:
        return "CEP inválido!"
    else:
        request = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
        dadosendereco = (request.json())
        #Verifica se o CEP existe e retorna seus dados.
        return dadosendereco