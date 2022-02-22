from typing import Container
from dicionarioCalculos import *
#from icecream import ic 

def getNumPeriodos(dias):
    l = lambda: 1 if dias % 7 > 0 else 0
    numPeriodos = dias // 7 + l()
    return numPeriodos  

def getPeriodosRioGaleao(dias):
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
            return 1 + getPeriodosRioGaleao(10)
        else:
            return 1 + getPeriodosRioGaleao(dias - 10)

def calculoMulti(cif, **kwargs): 
    variaveisPeriodoC20 = {}
    variaveisPeriodoC40 = {}
    servicosAdic20 = {}
    servicosAdic40 = {}
    quantServicAdic = {}

    for i in range(len(dicionarioMulti.get('valoresPorPeriodo20'))):
        variaveisPeriodoC20[i + 1] = dicionarioMulti.get('valoresPorPeriodo20')[i]
    
    for i in range(len(dicionarioMulti.get('valoresPorPeriodo40'))):
        variaveisPeriodoC40[i + 1] = dicionarioMulti.get('valoresPorPeriodo40')[i]

    for i in range(len(dicionarioMulti.get('servicosAdi20'))):
        servicosAdic20[i + 1] = dicionarioMulti.get('servicosAdi20')[i]
        
    for i in range(len(dicionarioMulti.get('servicosAdi40'))):
        servicosAdic40[i + 1] = dicionarioMulti.get('servicosAdi40')[i]
    
    for i in range(len(dicionarioMulti.get('quantServAdic'))):
        quantServicAdic[i + 1] = dicionarioMulti.get('quantServAdic')[i]

    container = kwargs.get("container")
    dias = kwargs.get("dias")
    numPeriodos = getNumPeriodos(dias)
    variaveisPeriodo = {}
    variaveisPeriodo['20'] = variaveisPeriodoC20
    variaveisPeriodo['40'] = variaveisPeriodoC40
    servicosAdi = {}
    servicosAdi['20'] = servicosAdic20
    servicosAdi['40'] = servicosAdic40

    formulaPeriodos = lambda x, y, z: x*y if(x*y/quantServicAdic[1]['quantContainer'] > z ) else z*quantServicAdic[1]['quantContainer']
    formulaSerAdic = lambda quant,d : quant*d
    formulaReefer = lambda quant,d : quant*d*dias
    
    carregamento = formulaSerAdic(quantServicAdic[2]['quantCarregamento'], servicosAdi[container][1]['carregamento'])
    pesagem = formulaSerAdic(quantServicAdic[3]['quantPesagem'], servicosAdi[container][2]['pesagem'])
    lacre = formulaSerAdic(quantServicAdic[5]['quantLacre'], servicosAdi[container][5]['lacre'])
    reefer = formulaReefer(quantServicAdic[4]['quantReefer'], servicosAdi[container][6]['reefer'])
    posicionamento = formulaSerAdic(quantServicAdic[6]['quantPosi'], servicosAdi[container][3]['posicionamento'])
    subAdi = carregamento + pesagem + lacre + reefer + posicionamento

    subArm = 0
    for i in range(numPeriodos):
        if i + 1 <= 4:
            subArm += formulaPeriodos(cif, variaveisPeriodo[container][i + 1]['percent'], variaveisPeriodo[container][i + 1]['min'])
            #res.append(formula(cif, variaveisPeriodo[container][i + 1]['percent'], variaveisPeriodo[container][i + 1]['min']))
        else:
            subArm += (formulaPeriodos(cif, variaveisPeriodo[container][4]['percent'], variaveisPeriodo[container][4]['min']))
            #res.append(formula(cif, variaveisPeriodo[container][4]['percent'], variaveisPeriodo[container][4]['min']))

    valorISS = (subAdi + subArm) * servicosAdi[container][7]['aliquota']
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

#print(calculoMulti(1689043.88, container='40', dias= 4))
#----------------------------------------------------------------------------------------

def calculoLibra(cif, **kwargs): 
    variaveisPeriodoC20 = {}
    variaveisPeriodoC40 = {}
    servicosAdic20 = {}
    servicosAdic40 = {}
    quantServicAdic = {}

    for i in range(len(dicionarioLibra.get('valoresPorPeriodo20'))):
        variaveisPeriodoC20[i + 1] = dicionarioLibra.get('valoresPorPeriodo20')[i]
    
    for i in range(len(dicionarioLibra.get('valoresPorPeriodo40'))):
        variaveisPeriodoC40[i + 1] = dicionarioLibra.get('valoresPorPeriodo40')[i]

    for i in range(len(dicionarioLibra.get('servicosAdi20'))):
        servicosAdic20[i + 1] = dicionarioLibra.get('servicosAdi20')[i]
        
    for i in range(len(dicionarioLibra.get('servicosAdi40'))):
        servicosAdic40[i + 1] = dicionarioLibra.get('servicosAdi40')[i]

    for i in range(len(dicionarioLibra.get('quantServAdic'))):
        quantServicAdic[i + 1] = dicionarioLibra.get('quantServAdic')[i]

    container = kwargs.get("container")
    dias = kwargs.get("dias")
    numPeriodos = getNumPeriodos(dias)
    variaveisPeriodo = {}
    variaveisPeriodo['20'] = variaveisPeriodoC20
    variaveisPeriodo['40'] = variaveisPeriodoC40
    servicosAdi = {}
    servicosAdi['20'] = servicosAdic20
    servicosAdi['40'] = servicosAdic40
    taxaConver = kwargs.get("taxaConver")

    if(container == '40'):
        formulaPeriodos = lambda taxaConver,x, taxaConteiner, valorMinimo, valorFixo: (((taxaConteiner*x*taxaConver) + valorFixo )/0.8575) if((taxaConteiner*x*taxaConver) > valorMinimo) else (valorMinimo + valorFixo)/0.8575
    else:
        formulaPeriodos = lambda taxaConteiner,x, taxaConver, valorMinimo, valorFixo: ((taxaConteiner*x*taxaConver) + valorFixo + 0/0.8575) if((taxaConteiner*x*taxaConver) > valorMinimo) else valorMinimo + valorFixo + 0/0.8575

    
    formulaSerAdic = lambda quant,d : quant*d
    formulaReefer = lambda quant,d : quant*d*dias
    
    carregamento = formulaSerAdic(quantServicAdic[1]['quantCarregamento'], servicosAdi[container][1]['carregamento'])
    pesagem = formulaSerAdic(quantServicAdic[2]['quantPesagem'], servicosAdi[container][2]['pesagemCTNR'])
    lacre = formulaSerAdic(quantServicAdic[4]['quantLacre'], servicosAdi[container][5]['lacre'])
    insInvasiva = formulaSerAdic(quantServicAdic[6]['quabtInsInvasiva'], servicosAdi[container][4]['insInvasiva'])
    transito = formulaSerAdic(quantServicAdic[7]['quantTransito'], servicosAdi[container][7]['transito'])
    reefer = formulaReefer(quantServicAdic[3]['quantReefer'], servicosAdi[container][6]['reefer'])
    posicionamento = formulaSerAdic(quantServicAdic[5]['quantPosi'], servicosAdi[container][3]['posicionamento'])
    subAdi = carregamento + pesagem + lacre + reefer + posicionamento + insInvasiva + transito

    subArm = 0
    valorPerAdic = 0
    for i in range(numPeriodos):
        if i + 1 <= 1:
            subArm += formulaPeriodos(taxaConver,cif, variaveisPeriodo[container][i + 1]['percent'], variaveisPeriodo[container][i + 1]['min'], valorFixo = quantServicAdic[8]['valorFixo'])
            valorPerAdic = formulaPeriodos(taxaConver,cif, variaveisPeriodo[container][i + 1]['percent'], variaveisPeriodo[container][i + 1]['min'],valorFixo = quantServicAdic[8]['valorFixo'])
            #res.append(formula(cif, variaveisPeriodo[container][i + 1]['percent'], variaveisPeriodo[container][i + 1]['min']))
        else:
            subArm += formulaPeriodos(taxaConver,cif, variaveisPeriodo[container][i + 1]['percent'], variaveisPeriodo[container][i + 1]['min'], valorFixo = 0)
            valorPerAdic = formulaPeriodos(taxaConver,cif, variaveisPeriodo[container][i + 1]['percent'], variaveisPeriodo[container][i + 1]['min'], valorFixo = 0)          
            #res.append(formula(cif, variaveisPeriodo[container][4]['percent'], variaveisPeriodo[container][4]['min']))
    
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

#print(calculoLibra(1712602.58, container = '40', taxaConver = 5.2585, dias= 2))

# ----------------------------------------------------------------------------------------

def calculoRioGaleao(cif, **kwargs):
    valoresPorPeriodoRio = {}
    pesoLiquidoRio = {}

    for i in range(len(dicionarioRioGaleao.get('valoresPorPeriodo'))):
        valoresPorPeriodoRio[i + 1] = dicionarioRioGaleao.get('valoresPorPeriodo')[i]
        
    for i in range(len(dicionarioRioGaleao.get('pesoLiquido'))):
        pesoLiquidoRio[i + 1] = dicionarioRioGaleao.get('pesoLiquido')[i]
          
    dias = kwargs.get("dias")
    numPeriodos = getPeriodosRioGaleao(dias)
    pesoBruto = kwargs.get("pesoBruto")
    pesoLiquido = kwargs.get("pesoLiquido")
    subArm = 0
    percent = 0
    cifPesoLiquido = cif/pesoLiquido
    print('cifPesoLiquido',cifPesoLiquido )
    print(numPeriodos)
    if(cifPesoLiquido < 5000):

        formulaPeriodos = lambda cif, percent : cif * percent if (numPeriodos <= 4) else (cif* valoresPorPeriodoRio[4]['percent'] +((0.045 + (0.025*(numPeriodos-4)))*cif)*(numPeriodos-4))
        formulaCapatazia = lambda pesoBruto: pesoBruto*0.0674 if(pesoBruto*0.0674 >  20.53) else 20.53
        capatazia = formulaCapatazia(pesoBruto)
        
        
        for i in range(numPeriodos):
            subArm = formulaPeriodos(cif, valoresPorPeriodoRio[i + 1]['percent'])

        total = capatazia + subArm

        return total

    else:
        if(cifPesoLiquido <= pesoLiquidoRio[1]['min']):
            percent = pesoLiquidoRio[1]['percent']
        elif(cifPesoLiquido <= pesoLiquidoRio[2]['min']):
            percent = pesoLiquidoRio[2]['percent']
        else:
            percent = pesoLiquidoRio[3]['percent']

        formulaPeriodos = lambda cif, percent : cif * percent

        for i in range(numPeriodos):
            subArm += formulaPeriodos(cif, percent)                                                                

        total = subArm 
    return total

print(calculoRioGaleao(1191148.14, dias = 3, pesoBruto = 579, pesoLiquido = 172.90))