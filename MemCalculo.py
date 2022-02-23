from excelExtraciton import getRow
from datetime import datetime
import traceback
import re

class MemCalculo:

    def __init__(self):
        self.valoresPeriodos = {}
    def getNumPeriodos(self,dias):
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
    def __init__(self, valoresPorPeriodo20, valoresPorPeriodo40, servicosAdi20, servicosAdi40, quantServAdic):
        self.valoresPorPeriodos20 = valoresPorPeriodo20
        self.valoresPorPeriodos40 = valoresPorPeriodo40
        self.servicosAdi20 = servicosAdi20
        self.servicosAdi40 = servicosAdi40
        self.quantServAdic = quantServAdic
        self.variaveisPeriodoC20 = {}
        self.variaveisPeriodoC40 = {}
        self.servicosAdic20 = {}
        self.servicosAdic40 = {}
        self.quantServicAdic = {}

        for i in range(len(valoresPorPeriodo20)):
            self.variaveisPeriodoC20[i + 1] = valoresPorPeriodo20[i]
    
        for i in range(len(valoresPorPeriodo40)):
            self.variaveisPeriodoC40[i + 1] = valoresPorPeriodo20[i] 

        for i in range(len(servicosAdi20)):
            self.servicosAdic20[i + 1] = servicosAdi20[i]
            
        for i in range(len(servicosAdi40)):
            self.servicosAdic40[i + 1] = servicosAdi40[i]

        for i in range(len(quantServAdic)):
            self.quantServicAdic[i + 1] = quantServAdic[i]

    

    def calcular(self, cif, **kwargs):        

        container = kwargs.get("container")
        dias = kwargs.get("dias")
        numPeriodos = self.getNumPeriodos(dias)
        variaveisPeriodo = {}
        variaveisPeriodo['20'] = self.variaveisPeriodoC20
        variaveisPeriodo['40'] = self.variaveisPeriodoC40
        servicosAdi = {}
        servicosAdi['20'] = self.servicosAdic20
        servicosAdi['40'] = self.servicosAdic40
        taxaConver = kwargs.get("taxaConver")

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
    def __init__(self, valoresPorPeriodo20, valoresPorPeriodo40, servicosAdi20, servicosAdi40, quantServAdic):
        self.valoresPorPeriodos20 = valoresPorPeriodo20
        self.valoresPorPeriodos40 = valoresPorPeriodo40
        self.servicosAdi20 = servicosAdi20
        self.servicosAdi40 = servicosAdi40
        self.quantServAdic = quantServAdic
        self.variaveisPeriodoC20 = {}
        self.variaveisPeriodoC40 = {}
        self.servicosAdic20 = {}
        self.servicosAdic40 = {}
        self.quantServicAdic = {}

        for i in range(len(valoresPorPeriodo20)):
            self.variaveisPeriodoC20[i + 1] = valoresPorPeriodo20[i]
    
        for i in range(len(valoresPorPeriodo40)):
            self.variaveisPeriodoC40[i + 1] = valoresPorPeriodo20[i] 

        for i in range(len(servicosAdi20)):
            self.servicosAdic20[i + 1] = servicosAdi20[i]
            
        for i in range(len(servicosAdi40)):
            self.servicosAdic40[i + 1] = servicosAdi40[i]

        for i in range(len(quantServAdic)):
            self.quantServicAdic[i + 1] = quantServAdic[i]

    def calcular(self, cif, **kwargs):

        container = kwargs.get("container")
        dias = kwargs.get("dias")
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
    def __init__(self, valoresPorPeriodo, pesoLiquido):
        self.valoresPorPeriodo = valoresPorPeriodo
        self.pesoLiquido = pesoLiquido
        self.variaveisPeriodo = {}
        self.variaveisPesoLiquido = {}

        for i in range(len(valoresPorPeriodo)):
            self.variaveisPeriodo[i + 1] = valoresPorPeriodo[i]
        
        for i in range(len(pesoLiquido)):
            self.variaveisPesoLiquido[i + 1] = pesoLiquido[i]

        

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






from dicionarioCalculos import dicionarioLibra, dicionarioMulti, dicionarioRioGaleao
#calc = MemCalculoLibra(dicionarioLibra['valoresPorPeriodo20'], dicionarioLibra['valoresPorPeriodo40'], dicionarioLibra['servicosAdi20'], dicionarioLibra['servicosAdi40'], dicionarioLibra['quantServAdic'])
#print(calc.calcular(1712602.58, container = '40', taxaConver = 5.2585, dias= 2))
#
#calc2 = MemCalculoMulti(dicionarioMulti['valoresPorPeriodo40'], dicionarioMulti['valoresPorPeriodo40'], dicionarioMulti['servicosAdi20'], dicionarioMulti['servicosAdi40'], dicionarioMulti['quantServAdic'])
#print(calc2.calcular(1689043.88, container='40', dias= 4))
#

#x = MemCalculo()
#print(x.getDias('2021-09-13 00:00:00', '2021-09-16 00:00:00'))
dataEntrada, dataSaida, pesoBruto, pesoLiq, cif, valor = getRow('PLANILHA - 2 QZ SETEMBRO 2021#.xlsx',1191148.14)
calc3 = MemCalculoRio(dicionarioRioGaleao['valoresPorPeriodo'], dicionarioRioGaleao['pesoLiquido'])

#print(calc3.calcular(1191148.14, dias = 3, pesoBruto = 579, pesoLiquido = 172.90))
print(calc3.calcular(cif, dataEntrada=dataEntrada, dataSaida=dataSaida, pesoBruto=pesoBruto, pesoLiquido=pesoLiq))


##### A Fazer
#Mudar o construtor para pegar dados padrão ou inseridos pelo usuário
#Outros fornecedores: DHL, KN, API Bacen
#Coordenadas documentos novos
#Modulos paddle(fuzzy/rgx) para notas comex
#Confirmar campos a serem extraídos


