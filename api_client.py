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
#a = API_Client('http://127.0.0.1:5000/Rio').result
#a = API_Client('http://127.0.0.1:5000/Libra?cif=1712602.58&container=40&taxaConver=5.2585&dias=2').result
#a = API_Client('http://127.0.0.1:5000/Multi?cif=1689043.88&container=40&dias=4').result

a = API_Client('http://127.0.0.1:5000/DHL?pesoBruto=579&transportation=Marítimo&taxaEUR=6.3&taxaUSD=5.0&qtdContainer=1').result


print(a)

