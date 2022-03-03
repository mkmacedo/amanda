import requests

def getCotacao(data):    
    splitURL = ["https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='","'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"]
    url = splitURL[0] + data + splitURL[1]
    dolar = requests.get(url).json()
    return dolar["value"][0]["cotacaoCompra"]

#print(getcotacao("02-03-2022")) #forma EUA