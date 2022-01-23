import requests

def rastrear(codeguim):
    request = requests.get('https://proxyapp.correios.com.br/v1/sro-rastro/{}'.format(codeguim))
    resp_consulta = (request.json())
    listaeventos = []
    listaeventos2 = []
    i = 0
    try:
        while i < len(resp_consulta['objetos'][0]['eventos']):
            listaeventos.append(resp_consulta['objetos'][0]['eventos'][i])
            i += 1
        #print(listaeventos)

        controle = 0
        for c in listaeventos:
            listaeventos2.append(listaeventos[controle])
            controle += 1

        controle = 0
        #print('=-='*25)
        #print('=== PESQUISANDO ENCOMENDA NÚMERO {} ==='.format(codeguim))
        #for x in range(len(listaeventos2)):
        #    print('|| Data: {}'.format(listaeventos2[x]['dtHrCriado']))
        #    print('|| Situação: [{}] - {}'.format(listaeventos2[x]['codigo'],listaeventos2[x]['descricao']))
        #    print('=-=' * 25)
        #    x += 1
        return listaeventos2

    #Se der erro e o código não estiver obsoleto, vai informar que o código ainda não foi postado ou é inválido.
    except:
        listaeventos2 = []
        return listaeventos2