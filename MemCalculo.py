from excelExtraciton import getRow
from datetime import datetime
import traceback
import re

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
    def __init__(self, varJson=None):
        varJson = {'valoresPorPeriodo20' :[{'percent': 0.0034, 'min': 1138.27},
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

        for i in range(len(varJson['valoresPorPeriodo20'])):
            self.variaveisPeriodoC20[i + 1] = varJson['valoresPorPeriodo20'][i]
    
        for i in range(len(varJson['valoresPorPeriodo20'])):
            self.variaveisPeriodoC40[i + 1] = varJson['valoresPorPeriodo20'][i] 

        for i in range(len(varJson['servicosAdi20'])):
            self.servicosAdic20[i + 1] = varJson['servicosAdi20'][i]
            
        for i in range(len(varJson['servicosAdi40'])):
            self.servicosAdic40[i + 1] = varJson['servicosAdi40'][i]

        for i in range(len(varJson['quantServAdic'])):
            self.quantServicAdic[i + 1] = varJson['quantServAdic'][i]

    @property
    def variables (self):
        return (self.variaveisPeriodoC20, self.variaveisPeriodoC40, self.servicosAdic20, self.servicosAdic40, self.quantServicAdic)


    @variables.setter
    def variables (self, varJson):
        self.variaveisPeriodoC20 = {}
        self.variaveisPeriodoC40 = {}
        self.servicosAdic20 = {}
        self.servicosAdic40 = {}
        self.quantServicAdic = {}

        for i in range(len(varJson.get('valoresPorPeriodo20'))):
            self.variaveisPeriodoC20[i + 1] = varJson.get('valoresPorPeriodo20')[i]
    
        for i in range(len(varJson.get('valoresPorPeriodo40'))):
            self.variaveisPeriodoC40[i + 1] = varJson.get('valoresPorPeriodo40')[i] 

        for i in range(len(varJson('servicosAdi20'))):
            self.servicosAdic20[i + 1] = varJson('servicosAdi20')[i]
            
        for i in range(len(varJson.get('servicosAdi40'))):
            self.servicosAdic40[i + 1] = varJson.get('servicosAdi40')[i]

        for i in range(len(varJson('quantServAdic'))):
            self.quantServicAdic[i + 1] = varJson('quantServAdic')[i]


    def calcular(self, cif, **kwargs):        
        if(type(cif) == type('str')):
            cif = eval(cif)
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
        
        carregamento = formulaSerAdic(self.quantServicAdic[1].get('quantCarregamento'), servicosAdi[container][1].get('carregamento'))
        pesagem = formulaSerAdic(self.quantServicAdic[2].get('quantPesagem'), servicosAdi[container][2].get('pesagemCTNR'))
        lacre = formulaSerAdic(self.quantServicAdic[4].get('quantLacre'), servicosAdi[container][5].get('lacre'))
        insInvasiva = formulaSerAdic(self.quantServicAdic[6].get('quabtInsInvasiva'), servicosAdi[container][4].get('insInvasiva'))
        transito = formulaSerAdic(self.quantServicAdic[7].get('quantTransito'), servicosAdi[container][7].get('transito'))
        reefer = formulaReefer(self.quantServicAdic[3].get('quantReefer'), servicosAdi[container][6].get('reefer'))
        posicionamento = formulaSerAdic(self.quantServicAdic[5].get('quantPosi'), servicosAdi[container][3].get('posicionamento'))
        subAdi = carregamento + pesagem + lacre + reefer + posicionamento + insInvasiva + transito

        subArm = 0
        valorPerAdic = 0
        for i in range(numPeriodos):
            if i + 1 <= 1:
                subArm += formulaPeriodos(taxaConver,cif, variaveisPeriodo[container][i + 1].get('percent'), variaveisPeriodo[container][i + 1].get('min'), valorFixo = self.quantServicAdic[8]['valorFixo'])
                valorPerAdic = formulaPeriodos(taxaConver,cif, variaveisPeriodo[container][i + 1].get('percent'), variaveisPeriodo[container][i + 1].get('min'),valorFixo = self.quantServicAdic[8]['valorFixo'])
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
        return dadosLibra




class MemCalculoMulti(MemCalculo):
    def __init__(self, varJson=None):
        varJson = {
            'valoresPorPeriodo20': [{'percent': 0.0041, 'min': 1611.22},
                                    {'percent': 0.0076, 'min': 1384.42},
                                    {'percent': 0.0140, 'min': 1522.87},
                                    {'percent': 0.0180, 'min': 1675.16}],

            'valoresPorPeriodo40': [{'percent': 0.0041, 'min': 1741.44},
                                    {'percent': 0.0076, 'min': 1527.68},
                                    {'percent': 0.0140, 'min': 1680.45},
                                    {'percent': 0.0180, 'min': 1848.48}],

            'servicosAdi20': [{'carregamento': 383.67},
                                {'pesagem': 94.00 },
                                {'posicionamento': 300.92},
                                {'desunitizacao': 300.92},
                                {'lacre': 45.13 },
                                {'reefer': 290.58},
                                {'aliquota': 0.166181955726821}],

            'servicosAdi40': [{'carregamento': 383.67},
                                {'pesagem': 94.00 },
                                {'posicionamento': 476.47},
                                {'desunitizacao': 476.47},
                                {'lacre': 45.13 },
                                {'reefer': 290.58},
                                {'aliquota': 0.166181955726821}],

            'quantServAdic': [{'quantContainer': 1},
                                {'quantCarregamento': 1},
                                {'quantPesagem': 1},
                                {'quantReefer': 1},
                                {'quantLacre': 0 },
                                {'quantPosi': 0}]

            }

        self.variaveisPeriodoC20 = {}
        self.variaveisPeriodoC40 = {}
        self.servicosAdic20 = {}
        self.servicosAdic40 = {}
        self.quantServicAdic = {}

        for i in range(len(varJson.get('valoresPorPeriodo20'))):
            self.variaveisPeriodoC20[i + 1] = varJson.get('valoresPorPeriodo20')[i]
    
        for i in range(len(varJson.get('valoresPorPeriodo40'))):
            self.variaveisPeriodoC40[i + 1] = varJson.get('valoresPorPeriodo40')[i] 

        for i in range(len(varJson.get('servicosAdi20'))):
            self.servicosAdic20[i + 1] = varJson.get('servicosAdi20')[i]
            
        for i in range(len(varJson.get('servicosAdi40'))):
            self.servicosAdic40[i + 1] = varJson.get('servicosAdi40')[i]

        for i in range(len(varJson.get('quantServAdic'))):
            self.quantServicAdic[i + 1] = varJson.get('quantServAdic')[i]

    @property
    def variables(self):                   
        return (self.variaveisPeriodoC20, self.variaveisPeriodoC40, self.servicosAdic20, self.servicosAdic40, self.quantServicAdic)   

    @variables.setter
    def variables(self, varJson):
        self.variaveisPeriodoC20 = {}
        self.variaveisPeriodoC40 = {}
        self.servicosAdic20 = {}
        self.servicosAdic40 = {}
        self.quantServicAdic = {}

        for i in range(len(varJson.get('valoresPorPeriodo20'))):
            self.variaveisPeriodoC20[i + 1] = varJson.get('valoresPorPeriodo20')[i]
    
        for i in range(len(varJson.get('valoresPorPeriodo40'))):
            self.variaveisPeriodoC40[i + 1] = varJson.get('valoresPorPeriodo40')[i] 

        for i in range(len(varJson.get('servicosAdi20'))):
            self.servicosAdic20[i + 1] = varJson.get('servicosAdi20')[i]
            
        for i in range(len(varJson.get('servicosAdi40'))):
            self.servicosAdic40[i + 1] = varJson.get('servicosAdi40')[i]

        for i in range(len(varJson.get('quantServAdic'))):
            self.quantServicAdic[i + 1] = varJson.get('quantServAdic')[i]

    def calcular(self, cif, **kwargs):

        if type(cif) == type('str'):
            cif = eval(cif)

        container = kwargs.get("container")
        dias = kwargs.get("dias")
        if type(dias) == type('str'):
            dias = eval(dias)
        numPeriodos = self.getNumPeriodos(dias)
        variaveisPeriodo = {}
        variaveisPeriodo['20'] = self.variaveisPeriodoC20
        variaveisPeriodo['40'] = self.variaveisPeriodoC40
        servicosAdi = {}
        servicosAdi['20'] = self.servicosAdic20
        servicosAdi['40'] = self.servicosAdic40


        formulaPeriodos = lambda x, y, z: x*y if(x*y/self.quantServicAdic[1].get('quantContainer') > z ) else z*self.quantServicAdic[1].get('quantContainer')
        formulaSerAdic = lambda quant,d : quant*d
        formulaReefer = lambda quant,d : quant*d*dias
        
        carregamento = formulaSerAdic(self.quantServicAdic[2].get('quantCarregamento'), servicosAdi[container][1].get('carregamento'))
        pesagem = formulaSerAdic(self.quantServicAdic[3].get('quantPesagem'), servicosAdi[container][2].get('pesagem'))
        lacre = formulaSerAdic(self.quantServicAdic[5].get('quantLacre'), servicosAdi[container][5].get('lacre'))
        reefer = formulaReefer(self.quantServicAdic[4].get('quantReefer'), servicosAdi[container][6].get('reefer'))
        posicionamento = formulaSerAdic(self.quantServicAdic[6].get('quantPosi'), servicosAdi[container][3].get('posicionamento'))
        subAdi = carregamento + pesagem + lacre + reefer + posicionamento

        subArm = 0
        for i in range(numPeriodos):
            if i + 1 <= 4:
                subArm += formulaPeriodos(cif, variaveisPeriodo[container][i + 1].get('percent'), variaveisPeriodo[container][i + 1].get('min'))
                #res.append(formula(cif, variaveisPeriodo[container][i + 1].get('percent'), variaveisPeriodo[container][i + 1].get('min')))
            else:
                subArm += (formulaPeriodos(cif, variaveisPeriodo[container][4].get('percent'), variaveisPeriodo[container][4].get('min')))
                #res.append(formula(cif, variaveisPeriodo[container][4].get('percent'), variaveisPeriodo[container][4].get('min')))

        valorISS = (subAdi + subArm) * servicosAdi[container][7].get('aliquota')
        faturamentoT = valorISS + subArm + subAdi


        dadosMulti = {
            "carregamento": carregamento,
            "pesagem": pesagem,
            "lacre": lacre,
            "reefer": reefer,
            "posicionamento": posicionamento,
            "faturamentoT": faturamentoT
        }

        return dadosMulti


class MemCalculoRio(MemCalculo):
    def __init__(self, varJson=None):
        varJson = {
                'valoresPorPeriodo': [{'percent': 0.0075},
                        {'percent': 0.0150},
                        {'percent': 0.0225},
                        {'percent': 0.0450},
                        {'percent': 0.0675},
                        {'percent': 0.0900},
                        {'percent': 0.1125},
                        {'percent': 0.1350},
                        {'percent': 0.1575},
                        {'percent': 0.1800}],

                'pesoLiquido': [{'percent': 0.0060, 'min': 19999.99 },
                                {'percent': 0.0030, 'min': 79999.99},
                                {'percent': 0.0015, 'min': 80000.00}]
                }
        self.variaveisPeriodo = {}
        self.variaveisPesoLiquido = {}

        for i in range(len(varJson.get('valoresPorPeriodo'))):
            self.variaveisPeriodo[i + 1] = varJson.get('valoresPorPeriodo')[i]
        
        for i in range(len(varJson.get('pesoLiquido'))):
            self.variaveisPesoLiquido[i + 1] = varJson.get('pesoLiquido')[i]

    @property 
    def varibles(self):
        return(self.variaveisPeriodo, self.variaveisPesoLiquido)
    
    @varibles.setter
    def varibles(self, varJson):
        self.variaveisPeriodo = {}
        self.variaveisPesoLiquido = {}

        for i in range(len(varJson.get('valoresPorPeriodo'))):
            self.variaveisPeriodo[i + 1] = varJson.get('valoresPorPeriodo')[i]
        
        for i in range(len(varJson.get('pesoLiquido'))):
            self.variaveisPesoLiquido[i + 1] = varJson.get('pesoLiquido')[i]

    def calcular(self, cif, **kwargs):
        cif = eval(cif)
        dataEntrada = kwargs.get("dataEntrada")
        dataSaida = kwargs.get("dataSaida")
        dias = self.getDias(dataEntrada, dataSaida)
        numPeriodos = self.getPeriodosRio(dias)
        pesoBruto = kwargs.get("pesoBruto")
        pesoLiquido = kwargs.get("pesoLiquido")
        pesoBruto = self.floatfy(pesoBruto)
        pesoLiquido = self.floatfy(pesoLiquido)
        subArm = 0
        percent = 0
        cifPesoLiquido = cif/pesoLiquido
        if(cifPesoLiquido < 5000):

            formulaPeriodos = lambda cif, percent : cif * percent if (numPeriodos <= 4) else (cif* self.variaveisPeriodo[4].get('percent') +((0.045 + (0.025*(numPeriodos-4)))*cif)*(numPeriodos-4))
            formulaCapatazia = lambda pesoBruto: pesoBruto*0.0674 if(pesoBruto*0.0674 >  20.53) else 20.53
            capatazia = formulaCapatazia(pesoBruto)
            
            
            for i in range(numPeriodos):
                subArm = formulaPeriodos(cif, self.variaveisPeriodo[i + 1].get('percent'))

            total = capatazia + subArm

            return total

        else:
            if(cifPesoLiquido <= self.variaveisPesoLiquido[1].get('min')):
                percent = self.variaveisPesoLiquido[1].get('percent')
            elif(cifPesoLiquido <= self.variaveisPesoLiquido[2].get('min')):
                percent = self.variaveisPesoLiquido[2].get('percent')
            else:
                percent = self.variaveisPesoLiquido[3].get('percent')

            formulaPeriodos = lambda cif, percent : cif * percent

            for i in range(numPeriodos):
                subArm += formulaPeriodos(cif, percent)                                                                

            total = subArm
        total = format(total, '.2f')
        return total

class MemCalculoDHL(MemCalculo):
    def __init__(self, varJson=None):
        varJson = {
            'taxaAdminMarit': 98,
            'capataMarit': 178,
            'handlingAereo': {'percent': 0.0005, 'min': 40.00},
            'delivreyFeeAereo': {'percent': 0.0005, 'min': 28.00},
            'iss': 0.1662
        }
        self.taxaAdminMarit = varJson.get('taxaAdminMarit')
        self.capataMarit = varJson.get('capataMarit')
        self.handlingAereo = varJson.get('handlingAereo')
        self.delivreyFeeAereo =  varJson.get('handlingAereo')
        self.iss = varJson.get('iss')

    @property
    def variables (self):
        return (self.taxaAdminMarit, self.capataMarit, self.handlingAereo, self.delivreyFeeAereo, self.iss)
    
    @variables.setter
    def variables (self, varJson):
        self.taxaAdminMarit = varJson.get('taxaAdminMarit')
        self.capataMarit = varJson.get('capataMarit')
        self.handlingAereo = varJson.get('handlingAereo')
        self.delivreyFeeAereo =  varJson.get('handlingAereo')
        self.iss = varJson.get('iss')
    
    
    def calcular(self,**kwargs):
        transportation = kwargs.get("transportation")
        pesoBruto = kwargs.get("pesoBruto")
        qtdContainer = kwargs.get("qtdContainer")
        if type(qtdContainer) == type('str'):
            qtdContainer = eval(qtdContainer)

        if transportation == "Marítimo":
            taxaEUR = kwargs.get("taxaEUR")
            if type(taxaEUR) == type('str'):
                taxaEUR = eval(taxaEUR)
            formulaPisMarit = self.iss * self.taxaAdminMarit
            formulaEUR = self.taxaAdminMarit + formulaPisMarit
            valorBRLImposto = formulaEUR * taxaEUR
            valorBRL = taxaEUR * self.capataMarit * qtdContainer

            return valorBRLImposto, valorBRL
        
        elif transportation == "Aéreo":
            taxaUSD = kwargs.get("taxaUSD")
            if type(taxaUSD) == type('str'):
                taxaUSD = eval(taxaUSD)
            formulaHandlingAereo = lambda : pesoBruto*self.handlingAereo.get("percent") if(pesoBruto*self.handlingAereo.get("percent")  > self.handlingAereo.get("min")) else self.handlingAereo.get("min")
            formulaDeliveryFeeAereo  = lambda : pesoBruto*self.delivreyFeeAereo.get("percent") if(pesoBruto*self.delivreyFeeAereo.get("percent")  >  self.delivreyFeeAereo.get("percent")) else self.delivreyFeeAereo.get("min")
            formaulaPis =  self.iss*(formulaHandlingAereo()+formulaDeliveryFeeAereo())
            formulaUSD  = formulaHandlingAereo()+formulaDeliveryFeeAereo()+formaulaPis()
            valorBRL = lambda: formulaUSD*taxaUSD-(formulaUSD * taxaUSD * 0.015) if(formulaUSD * taxaUSD * 0.015 > 10) else formulaUSD * taxaUSD     
            
            return valorBRL()
            #multiplica container?

class MemCalculoDMS(MemCalculo):
    def __init__(self, varJson=None):
        varJson = {
                    'valorProcesso': {'10 dias': 1242.95, '11 a 15 dias': 955.9, '16 a 20 dias': 847.77, 'acima de 20 dias': 739.74},
                    'valorLI': {'10 dias': 217.30},
                    'valorExpurgo': {'10 dias': 177.85},
                    'iss': 0.05
                    }

        self.valorProcesso = varJson.get('valorProcesso')
        self.valorLI = varJson.get('valorLI')
        self.valorExpurgo = varJson.get('valorExpurgo')
        self.iss = varJson.get('iss')
      

    @property
    def variables (self):
        return (self.valorProcesso, self.valorLI, self.valorExpurgo, self.iss)
    
    @variables.setter
    def variables (self, varJson):
        self.valorProcesso = varJson.get('valorProcesso')
        self.valorLI = varJson.get('valorLI')
        self.valorExpurgo = varJson.get('valorExpurgo')
        self.iss = varJson.get('iss')
      
    
    def calcular(self,**kwargs):
        dataEntrada = kwargs.get("dataEntrada")
        dataSaida = kwargs.get("dataSaida")
        leadtime = self.getDias(dataEntrada, dataSaida)
        transportation = kwargs.get("transportation")
        numLI = kwargs.get("numLI")
        if type(numLI) == type('str'):
            numLI = eval(numLI)
        

        valor = lambda : self.valorProcesso ['acima de 20 dias'] if(leadtime > 20) else self.valorProcesso['16 a 20 dias'] if (leadtime > 15) else self.valorProcesso['11 a 15 dias'] if(leadtime > 10) else self.valorProcesso['10 dias']
        expurgo = lambda : self.valorExpurgo.get("10 dias") if (transportation == 'SEA') else 0
        li = self.valorLI.get ("10 dias") * numLI 
        valorIss = (valor() + expurgo() + li) * self.iss
        total =  valor() + expurgo() + li + valorIss
               
                 
        return total



#from dicionarioCalculos import dicionarioLibra, dicionarioMulti, dicionarioRioGaleao, dicionarioDHL
#calc = MemCalculoLibra(dicionarioLibra['valoresPorPeriodo20'], dicionarioLibra['valoresPorPeriodo40'], dicionarioLibra['servicosAdi20'], dicionarioLibra['servicosAdi40'], dicionarioLibra['quantServAdic'])
#calc = MemCalculoLibra()

#print(calc.calcular(1712602.58, container = '40', taxaConver = 5.2585, dias= 2))
#
#calc2 = MemCalculoMulti(dicionarioMulti['valoresPorPeriodo40'], dicionarioMulti['valoresPorPeriodo40'], dicionarioMulti['servicosAdi20'], dicionarioMulti['servicosAdi40'], dicionarioMulti['quantServAdic'])
#calc2 = MemCalculoMulti()
#print(calc2.calcular(1689043.88, container='40', dias= 4))
#

#x = MemCalculo()
#print(x.getDias('2021-09-13 00:00:00', '2021-09-16 00:00:00'))
#dataEntrada, dataSaida, pesoBruto, pesoLiq, cif, valor = getRow('PLANILHA - 2 QZ SETEMBRO 2021#.xlsx',1191148.14)
#calc3 = MemCalculoRio(dicionarioRioGaleao['valoresPorPeriodo'], dicionarioRioGaleao['pesoLiquido'])
#calc3 = MemCalculoRio()

#print(calc3.calcular("1191148.14", dataEntrada = "2021-10-03",dataSaida="2021-10-05", pesoBruto = "579", pesoLiquido = "172.90"))
#print(calc3.calcular(cif, dataEntrada=dataEntrada, dataSaida=dataSaida, pesoBruto=pesoBruto, pesoLiquido=pesoLiq))

#calc4 = MemCalculoDHL(12, 10, dicionarioDHL['handlingAereo'], dicionarioDHL['delivreyFeeAereo'], 0.05)

#print(calc4.calcular( pesoBruto = "579", transportation="Marítimo", taxaEUR=6.3, taxaUSD=5.0, qtdContainer=1))

#calc4 = MemCalculoDHL()

#print(calc4.calcular( pesoBruto = "579", transportation="Marítimo", taxaEUR=6.3, taxaUSD=5.0, qtdContainer=1))

#calc5 = MemCalculoDMS()

#print(calc5.calcular( numLI = 1, transportation="SEA", dataEntrada= "2021-03-07", dataSaida= "2021-03-05"))

##### A Fazer
#Mudar o construtor para pegar dados padrão ou inseridos pelo usuário #OK
#Outros fornecedores: DHL, KN, API Bacen
#Coordenadas documentos novos ok
#Modulos paddle(fuzzy/rgx) para notas comex 
#Confirmar campos a serem extraídos (LIZ)
#Verificar KN com a Liz




