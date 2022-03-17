from excelExtraciton import getRow
from datetime import datetime
import traceback
import re
from api_client import API_Client
from bacen import getCotacao

class MemCalculo:

    def __init__(self):
        self.valoresPeriodos = {}
    def getNumPeriodos(self,dias):
        if type(dias)==type('str'):
            dias = eval(dias)
        l = lambda: 1 if dias % 7 > 0 else 0
        numPeriodos = dias // 7 + l()
        return numPeriodos

    def getPeriodosRio(self, dias):
        if dias >= 1 and dias < 3:
            return 1
        if dias >= 3 and dias < 6:
            return 2
        if dias >= 6 and dias < 11:
            return 3
        elif dias >= 11:
            x = dias - 10
            r = x // 10
            if r == 0:
                return 1 + self.getPeriodosRioGaleao(10)
            else:
                return 1 + self.getPeriodosRioGaleao(dias - 10)

    def floatfy(self, rCurrentValue):
        splitCurrentValue = rCurrentValue.split('.')
        currentValue = ''
        for cSlice in splitCurrentValue:
            currentValue += cSlice
        comma = currentValue.find(',')
        if comma != -1:
            currentValue = currentValue[:comma]+'.'+currentValue[comma+1:]

        return eval(currentValue)

    def getDias(self, dataEntrada, dataSaida, inputFormat='standard'):
        #r1 = re.search(r'[0-9]+(?:/|-)[0-9]+(?:/|-)[0-9]+', dataEntrada)
        #r2 = re.search(r'[0-9]+(?:/|-)[0-9]+(?:/|-)[0-9]+', dataSaida)
        #if r1 != None and r2 != None:
        #    dataEntrada = r1.group()
        #    dataSaida = r2.group()
        dataEntrada = str(dataEntrada).split()[0]
        dataSaida = str(dataSaida).split()[0]
        try:
            if inputFormat == 'DD MM YYYY':
                if dataEntrada.find('/') != -1 or dataSaida.find('/') != -1:
                    d1, m1, y1 = [int(x) for x in dataEntrada.split('/')]
                    d2, m2, y2 = [int(x) for x in dataSaida.split('/')]
                elif dataEntrada.find('-') != -1 or dataSaida.find('-') != -1:
                    d1, m1, y1 = [int(x) for x in dataEntrada.split('-')]
                    d2, m2, y2 = [int(x) for x in dataSaida.split('-')]
            elif inputFormat == 'MM DD YYYY':
                if dataEntrada.find('/') != -1 or dataSaida.find('/') != -1:
                    m1, d1, y1 = [int(x) for x in dataEntrada.split('/')]
                    m2, d2, y2 = [int(x) for x in dataSaida.split('/')]
                elif dataEntrada.find('-') != -1 or dataSaida.find('-') != -1:
                    m1, d1, y1 = [int(x) for x in dataEntrada.split('-')]
                    m2, d2, y2 = [int(x) for x in dataSaida.split('-')]
            else:
                if dataEntrada.find('/') != -1 or dataSaida.find('/') != -1:
                    y1, m1, d1 = [int(x) for x in dataEntrada.split('/')]
                    y2, m2, d2 = [int(x) for x in dataSaida.split('/')]
                elif dataEntrada.find('-') != -1 or dataSaida.find('-') != -1:
                    y1, m1, d1 = [int(x) for x in dataEntrada.split('-')]
                    y2, m2, d2 = [int(x) for x in dataSaida.split('-')]

            date1 = datetime(y1, m1, d1)
            date2 = datetime(y2, m2, d2)


            dias = str(date2 - date1)
            d = re.search('[0-9]+', dias)
            if d != None:
                dias = eval(d.group())


            return dias
        except:
            print('Invalid datetime input')
            traceback.print_exc()
            return None


class MemCalculoLibra(MemCalculo):
    def __init__(self, api=False):
        if api == False:
            varJson = {
                'valoresPorPeriodo20' :[{'percent': 0.0034, 'min': 1138.27},
                        {'percent': 0.0066, 'min': 1252.11},
                        {'percent': 0.0136, 'min': 1377.30},
                        {'percent': 0.0174, 'min': 1515.03}],

                    'valoresPorPeriodo40' : [{'percent': 0.0034, 'min': 1707.40},
                                    {'percent': 0.0066, 'min': 1878.14},
                                    {'percent': 0.0136, 'min': 2065.94},
                                    {'percent': 0.0174, 'min': 2272.54}],
                                    
                    'servicosAdi20' : [{'carregamento': 529.19},
                                    {'pesagemCTNR': 117.99},
                                    {'posicionamento': 476.47},
                                    {'insInvasiva': 314.85},
                                    {'lacre': 60.30 },
                                    {'reefer': 319.45},
                                    {'transito': 447.45}],

                    'servicosAdi40' : [{'carregamento': 529.19},
                                    {'pesagemCTNR': 117.99},
                                    {'posicionamento': 476.47},
                                    {'insInvasiva': 314.85},
                                    {'lacre': 60.30 },
                                    {'reefer': 319.45},
                                    {'transito': 447.45}],

                    'quantServAdic' : [{'quantCarregamento': 1 },
                                    {'quantPesagem': 1},
                                    {'quantReefer': 1},
                                    {'quantLacre': 0 },
                                    {'quantPosi': 0},
                                    {'quabtInsInvasiva': 1},
                                    {'quantTransito' : 1},
                                    {'valorFixo': 351.11}]
                    }

            self.variaveisPeriodoC20 = {}
            self.variaveisPeriodoC40 = {}
            self.servicosAdic20 = {}
            self.servicosAdic40 = {}
            self.quantServicAdic = {}   

            for i in range(len(varJson.get['valoresPorPeriodo20'])):
                self.variaveisPeriodoC20[i + 1] = varJson.get['valoresPorPeriodo20'][i]
        
            for i in range(len(varJson.get['valoresPorPeriodo20'])):
                self.variaveisPeriodoC40[i + 1] = varJson.get['valoresPorPeriodo20'][i] 

            for i in range(len(varJson.get['servicosAdi20'])):
                self.servicosAdic20[i + 1] = varJson.get['servicosAdi20'][i]
                
            for i in range(len(varJson.get['servicosAdi40'])):
                self.servicosAdic40[i + 1] = varJson.get['servicosAdi40'][i]

            for i in range(len(varJson.get['quantServAdic'])):
                self.quantServicAdic[i + 1] = varJson.get['quantServAdic'][i]

        elif api == True:

        #Percentuais por container
            varPercent = API_Client('https://wise.klink.ai/api/admin/comexview/containerpercentual/2').result
            varMin = API_Client('https://wise.klink.ai/api/admin/comexview/containervalores/2').result
            varFixoTransitorio = API_Client('https://wise.klink.ai/api/admin/comexview/servicovalores/2').result

            self.variaveisPeriodoC20 = {}
            self.variaveisPeriodoC40 = {}
            self.servicosAdic20 = {}
            self.servicosAdic40 = {}
            self.quantServicAdic = {}

            for i in range(len(varPercent)):
                self.variaveisPeriodoC20[i + 1] = {'percent': varPercent[i].get('container20Percentual')/100}
                self.variaveisPeriodoC40[i + 1] = {'percent': varPercent[i].get('container40Percentual')/100}

        
            for i in range(len(varMin)):
                self.variaveisPeriodoC20[i + 1]['min'] = varMin[i].get('container20ValorMinimo')
                self.variaveisPeriodoC40[i + 1]['min'] = varMin[i].get('container40ValorMinimo') 


            self.servicosAdic20['valorFixo'] = varFixoTransitorio[0].get('container20ValorMinimo')
            self.servicosAdic40['valorFixo'] = varFixoTransitorio[0].get('container40ValorMinimo')

            self.servicosAdic20['transito'] = varFixoTransitorio[1].get('container20ValorMinimo')
            self.servicosAdic40['transito'] = varFixoTransitorio[1].get('container40ValorMinimo')

            varJson = {                              
                    'servicosAdi20' : [{'carregamento': 529.19},
                                    {'pesagemCTNR': 117.99},
                                    {'posicionamento': 476.47},
                                    {'insInvasiva': 314.85},
                                    {'lacre': 60.30 },
                                    {'reefer': 319.45},
                                    {'transito': 447.45}],

                    'servicosAdi40' : [{'carregamento': 529.19},
                                    {'pesagemCTNR': 117.99},
                                    {'posicionamento': 476.47},
                                    {'insInvasiva': 314.85},
                                    {'lacre': 60.30 },
                                    {'reefer': 319.45},
                                    {'transito': 447.45}],

                    'quantServAdic' : [{'quantCarregamento': 1 },
                                    {'quantPesagem': 1},
                                    {'quantReefer': 1},
                                    {'quantLacre': 0 },
                                    {'quantPosi': 0},
                                    {'quabtInsInvasiva': 1},
                                    {'quantTransito' : 1},
                                    {'valorFixo': 351.11}]
                    }


            for i in range(len(varJson['servicosAdi20'])):
                k = list(varJson['servicosAdi20'][i].keys())
                k = k[0] 
                self.servicosAdic20[k] = varJson['servicosAdi20'][i].get(k)
   

            
            for i in range(len(varJson['servicosAdi40'])):
                k = list(varJson['servicosAdi40'][i].keys())
                k = k[0]
                self.servicosAdic40[k] = varJson['servicosAdi40'][i].get(k)          

            for i in range(len(varJson['quantServAdic'])):
                k = list(varJson['quantServAdic'][i].keys())
                k = k[0]
                self.quantServicAdic[k] = varJson['quantServAdic'][i].get(k)

            #self.servicosAdic20['carregamento'] =  varServicosValores[0].get('container20ValorMinimo')
            #self.servicosAdic20['pesagem'] =  varServicosValores[1].get('container20ValorMinimo')
            #self.servicosAdic20['posicionamento'] =  varServicosValores[2].get('container20ValorMinimo')
            #self.servicosAdic20['lacre'] =  varServicosValores[3].get('container20ValorMinimo')
            #self.servicosAdic20['desunitização'] =  varServicosValores[4].get('container20ValorMinimo')
            #self.servicosAdic20['reefer'] =  varServicosValores[5].get('container20ValorMinimo')

            #self.servicosAdic40['carregamento'] =  varServicosValores[0].get('container40ValorMinimo')
            #self.servicosAdic40['pesagem'] =  varServicosValores[1].get('container40ValorMinimo')
            #self.servicosAdic40['posicionamento'] =  varServicosValores[2].get('container40ValorMinimo')
            #self.servicosAdic40['lacre'] =  varServicosValores[3].get('container40ValorMinimo')
            #self.servicosAdic40['desunitizacao'] =  varServicosValores[4].get('container40ValorMinimo')
            #self.servicosAdic40['reefer'] =  varServicosValores[5].get('container40ValorMinimo')



    def calcular(self, cif, **kwargs):        
        if(type(cif) == type('str')):
            cif = eval(cif)

        valor = kwargs.get("valor")
        if(type(valor) == type('str')):
            valor = valor.replace('.', '').replace(',','')
            valor = valor[:-2]+'.'+valor[-2:]
            valor = eval(valor)

        container = kwargs.get("container")

        dias = kwargs.get("dias")
        if type(dias) == type('str'):
            dias = int(kwargs.get("dias"))
        numPeriodos = self.getNumPeriodos(dias)
        variaveisPeriodo = {}
        variaveisPeriodo['20'] = self.variaveisPeriodoC20
        variaveisPeriodo['40'] = self.variaveisPeriodoC40
        servicosAdi = {}
        servicosAdi['20'] = self.servicosAdic20
        servicosAdi['40'] = self.servicosAdic40
        taxaConver = kwargs.get("taxaConver")
        if type(taxaConver) == type('str'):
            taxaConver = eval(kwargs.get("taxaConver"))

        if(container == '40'):
            formulaPeriodos = lambda taxaConver,x, taxaConteiner, valorMinimo, valorFixo: (((taxaConteiner*x*taxaConver) + valorFixo )/0.8575) if((taxaConteiner*x*taxaConver) > valorMinimo) else (valorMinimo + valorFixo)/0.8575
        else:
            formulaPeriodos = lambda taxaConteiner,x, taxaConver, valorMinimo, valorFixo: ((taxaConteiner*x*taxaConver) + valorFixo + 0/0.8575) if((taxaConteiner*x*taxaConver) > valorMinimo) else valorMinimo + valorFixo + 0/0.8575

        
        formulaSerAdic = lambda quant,d : quant*d
        formulaReefer = lambda quant,d : quant*d*dias
        
        carregamento = formulaSerAdic(self.quantServicAdic.get('quantCarregamento'), servicosAdi[container].get('carregamento'))
        pesagem = formulaSerAdic(self.quantServicAdic.get('quantPesagem'), servicosAdi[container].get('pesagemCTNR'))
        lacre = formulaSerAdic(self.quantServicAdic.get('quantLacre'), servicosAdi[container].get('lacre'))
        insInvasiva = formulaSerAdic(self.quantServicAdic.get('quabtInsInvasiva'), servicosAdi[container].get('insInvasiva'))
        transito = formulaSerAdic(self.quantServicAdic.get('quantTransito'), servicosAdi[container].get('transito'))
        reefer = formulaReefer(self.quantServicAdic.get('quantReefer'), servicosAdi[container].get('reefer'))
        posicionamento = formulaSerAdic(self.quantServicAdic.get('quantPosi'), servicosAdi[container].get('posicionamento'))
        subAdi = carregamento + pesagem + lacre + reefer + posicionamento + insInvasiva + transito

        subArm = 0
        valorPerAdic = 0
        for i in range(numPeriodos):
            if i + 1 <= 1:
                subArm += formulaPeriodos(taxaConver,cif, variaveisPeriodo[container][i + 1].get('percent'), variaveisPeriodo[container][i + 1].get('min'), valorFixo = self.quantServicAdic['valorFixo'])
                valorPerAdic = formulaPeriodos(taxaConver,cif, variaveisPeriodo[container][i + 1].get('percent'), variaveisPeriodo[container][i + 1].get('min'),valorFixo = self.quantServicAdic['valorFixo'])
                #res.append(formula(cif, variaveisPeriodo[container][i + 1].get('percent'), variaveisPeriodo[container][i + 1].get('min')))
            else:
                subArm += formulaPeriodos(taxaConver,cif, variaveisPeriodo[container][i + 1].get('percent'), variaveisPeriodo[container][i + 1].get('min'), valorFixo = 0)
                valorPerAdic = formulaPeriodos(taxaConver,cif, variaveisPeriodo[container][i + 1].get('percent'), variaveisPeriodo[container][i + 1].get('min'), valorFixo = 0)          
                #res.append(formula(cif, variaveisPeriodo[container][4].get('percent'), variaveisPeriodo[container][4].get('min')))
        
        total = valorPerAdic + subAdi
        faturamentoT = subArm + subAdi
        
        dadosLibra = {
            "carregamento": carregamento,
            "pesagem": pesagem,
            "lacre": lacre,
            "reefer": reefer,
            "posicionamento": posicionamento,
            "faturamentoT": faturamentoT,
            "valorPerAdic": valorPerAdic,
            "total": total
        }
        t = format(dadosLibra.get('total'), '.2f')
        t = float(t)

        if valor != None:

            if t == valor:
                return True
            else:
                return False

        else:
            return t
        #return dadosLibra

calc = MemCalculoLibra(True)

print(calc.calcular(1712602.58, container = '40', taxaConver = 5.2585, dias= 2, valor = 38165.65))