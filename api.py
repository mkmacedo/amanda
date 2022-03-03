import MemCalculo
from flask import Flask
from flask_restful import Resource, Api, reqparse
from icecream import ic

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
        args = parser.parse_args()

        data = MemCalculo.MemCalculoRio()
        result = data.calcular(args['cif'], dataEntrada=args['dataEntrada'], dataSaida=args['dataSaida'], pesoBruto=args['pesoBruto'], pesoLiquido=args['pesoLiquido'])
        result = '{:.2f}'.format(result)
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
        args = parser.parse_args()

        data = MemCalculo.MemCalculoMulti()
        result = data.calcular(args['cif'], container=str(args['container']), dias=args['dias'])
        return {'data': result}, 200


api.add_resource(MemCalcMulti, '/Multi')

api.add_resource(MemCalcRio, '/Rio')

api.add_resource(MemCalcLibra, '/Libra')

if __name__ == '__main__':
    app.run(debug=True)


