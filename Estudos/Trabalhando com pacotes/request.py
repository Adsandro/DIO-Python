import requests

def Retorna_dados_cep():
    cep = str(input('Informe um cep: '))
    resp = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    dados_cep = resp.json()
    print(dados_cep['complemento'])
    return dados_cep

print(Retorna_dados_cep())
