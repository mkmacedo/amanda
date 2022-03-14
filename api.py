import MemCalculo

import sys
from flask import Flask
from flask_restful import Resource, Api, reqparse
from icecream import ic

serverIP = sys.argv[1]
print(serverIP)

app = Flask(__name__)
api = Api(app)

class MemCalcRio(Resource):
#    def __init__(self):
#        pass
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('cif', required=True)
        parser.add_argument('dataEntrada', required=True)
        parser.add_argument('dataSaida', required=True)
        parser.add_argument('pesoBruto', required=True)
        parser.add_argument('pesoLiquido', required=True)
        parser.add_argument('valor')
        args = parser.parse_args()

        data = MemCalculo.MemCalculoRio()
        result = data.calcular(args['cif'], dataEntrada=args['dataEntrada'], dataSaida=args['dataSaida'], pesoBruto=args['pesoBruto'], pesoLiquido=args['pesoLiquido'])
        #result = '{:.2f}'.format(result)
        return {'data': result}, 200

class MemCalcLibra(Resource):
#    def __init__(self):
#        pass
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('cif', required=True)
        parser.add_argument('container', required=True)
        parser.add_argument('taxaConver', required=True)
        parser.add_argument('dias', required=True)
        parser.add_argument('valor')
        args = parser.parse_args()

        data = MemCalculo.MemCalculoLibra()
        result = data.calcular(args['cif'], container=str(args['container']), taxaConver=args['taxaConver'], dias=args['dias'])
        return {'data': result}, 200


class MemCalcMulti(Resource):
#    def __init__(self):
#        pass
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('cif', required=True)
        parser.add_argument('container', required=True)
        parser.add_argument('dias', required=True)
        parser.add_argument('valor')
        args = parser.parse_args()

        data = MemCalculo.MemCalculoMulti()
        result = data.calcular(args['cif'], container=str(args['container']), dias=args['dias'])
        return {'data': result}, 200

class MemCalcDHL(Resource):
#    def __init__(self):
#        pass
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pesoBruto', required=True)
        parser.add_argument('transportation', required=True)
        parser.add_argument('taxaEUR', required=True)
        parser.add_argument('taxaUSD', required=True)
        parser.add_argument('qtdContainer', required=True)
        parser.add_argument('valor')
        args = parser.parse_args()

        data = MemCalculo.MemCalculoDHL()
        result = data.calcular(pesoBruto=args['pesoBruto'], transportation=str(args['transportation']), taxaEUR=args['taxaEUR'], taxaUSD=args['taxaUSD'], qtdContainer=args['qtdContainer'] )
        return {'data': result}, 200

class MemCalcDMS(Resource):
#    def __init__(self):
#        pass
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('numLI', required=True)
        parser.add_argument('transportation', required=True)
        parser.add_argument('dataEntrada', required=True)
        parser.add_argument('dataSaida', required=True)
        parser.add_argument('valor')
        args = parser.parse_args()

        data = MemCalculo.MemCalculoDMS()
        result = data.calcular(numLI=args['numLI'], transportation=str(args['transportation']), dataEntrada=args['dataEntrada'], dataSaida=args['dataSaida'])
        return {'data': result}, 200

class MemCalcKN(Resource):
#    def __init__(self):
#        pass
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('origem', required=True)
        parser.add_argument('emissao', required=True)
        parser.add_argument('container', required=True)
        parser.add_argument('qtdContainer', required=True)
        parser.add_argument('tipoContainer', required=True)
        parser.add_argument('valor')
        args = parser.parse_args()

        data = MemCalculo.MemCalculoKN()
        result = data.calcular(origem=args['origem'], emissao=args['emissao'], container=str(args['container']), qtdContainer=args['qtdContainer'], tipoContainer=args['tipoContainer'], valor=args['valor'])
        #result = '{:.2f}'.format(result)
        return {'data': result}, 200



api.add_resource(MemCalcKN, '/KN')

api.add_resource(MemCalcDMS, '/DMS')

api.add_resource(MemCalcDHL, '/DHL')

api.add_resource(MemCalcMulti, '/Multi')

api.add_resource(MemCalcRio, '/Rio')

api.add_resource(MemCalcLibra, '/Libra')

if __name__ == '__main__':
    #app.run(debug=True)
    from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    serve(app, host=serverIP, port=5000)


