import requests
import sys

#param = sys.argv[1]

class API_Client():
    def __init__(self, url):
        self.url = url
        self.result = self.connect()

    def connect(self):

#        params = {
#            'cif': 1191148.14,
#            'dataEntrada': "2021-10-03",
#            'dataSaida': "2021-10-05",
#            'pesoBruto': "579",
#            'pesoLiquido': "172.90"
#        }

        json = requests.get(self.url).json()

        return json

#a = API_Client('http://127.0.0.1:5000/Rio?cif=1191148.14&dataEntrada=2021-10-03&dataSaida=2021-10-05&dataSaida=2021-10-05&pesoBruto=579&pesoLiquido=172.90').result
##a = API_Client('http://127.0.0.1:5000/Rio').result
#b = API_Client('http://127.0.0.2:5000/Libra?cif=1712602.58&container=40&taxaConver=5.2585&dias=2&valor=38165.65').result
c = API_Client('http://127.0.0.3:5000/Multi?cif=1689043.88&container=40&dias=4&valor=9988.43').result
#
#d = API_Client('http://127.0.0.1:5000/DHL?pesoBruto=579&transportation=SEA&taxaEUR=6.3&taxaUSD=5.0&qtdContainer=1').result
#
#e = API_Client('http://127.0.0.1:5000/DMS?numLI=1&transportation=SEA&dataEntrada=2021-03-07&dataSaida=2021-03-05').result
#
#f = API_Client('http://127.0.0.1:5000/KN?origem=MONTEVIDEO&emissao=02-03-2022&container=20&qtdContainer=1&tipoContainer=REFEER').result

#g = API_Client('http://0.0.0.0:8080/KN?origem=MONTEVIDEO&emissao=02-03-2022&container=20&qtdContainer=1&tipoContainer=REFEER').result

#a = API_Client('https://wise.klink.ai/api/admin/comexview/containerpercentual/1').result
#b = API_Client('https://wise.klink.ai/api/admin/comexview/containervalores/1').result
#c = API_Client('https://wise.klink.ai/api/admin/comexview/servicopercentual/1').result
#d = API_Client('https://wise.klink.ai/api/admin/comexview/servicovalores/1').result
#e = API_Client('https://wise.klink.ai/api/admin/comexview/cargageralpercentual/1').result
#f = API_Client('https://wise.klink.ai/api/admin/comexview/cargageralvalores/1').result

#print(a)
#print(b)
print(c)
#print(d)
#print(e)
#print(f)
