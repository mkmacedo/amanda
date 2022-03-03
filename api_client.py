import requests
import sys

#param = sys.argv[1]

class API_Client():
    def __init__(self, url):
        self.url = url
        self.result = self.connect()

    def connect(self):

        params = {
            'cif': 1191148.14,
            'dataEntrada': "2021-10-03",
            'dataSaida': "2021-10-05",
            'pesoBruto': "579",
            'pesoLiquido': "172.90"
        }

        json = requests.get(self.url, params=params).json()

        return json

#a = API_Client('http://127.0.0.1:5000/Rio?cif=1191148.14&dataEntrada="2021-10-03"&dataSaida="2021-10-05"&dataSaida="2021-10-05"&pesoBruto="579"&pesoLiquido="172.90"').result
a = API_Client('http://127.0.0.1:5000/Rio').result

print(a)
