from datetime import datetime
import traceback
import re

def getDias(dataEntrada, dataSaida, inputFormat='standard'):
    r1 = re.search(r'[0-9]+(?:/|-)[0-9]+(?:/|-)[0-9]+', dataEntrada)
    r2 = re.search(r'[0-9]+(?:/|-)[0-9]+(?:/|-)[0-9]+', dataSaida)
    if r1 != None and r2 != None:
        dataEntrada = r1.group()
        dataSaida = r2.group()

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

def getPeriodo(dataEntrada, dataSaida, inputFormat='standard'):
    r1 = re.search(r'[0-9]+(?:/|-)[0-9]+(?:/|-)[0-9]+', dataEntrada)
    r2 = re.search(r'[0-9]+(?:/|-)[0-9]+(?:/|-)[0-9]+', dataSaida)
    if r1 != None and r2 != None:
        dataEntrada = r1.group()
        dataSaida = r2.group()
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

        l = lambda: 1 if dias % 7 > 0 else 0
        numPeriodos = dias // 7 + l()

        return numPeriodos
    except:
        print('Invalid datetime input')
        traceback.print_exc()
        return None

#17/08/2021 19/08/2021
print(getDias('2021-09-13 00:00:00', '2021-09-16 00:00:00'))
print(getPeriodo('2021-09-13 00:00:00', '2021-09-16 00:00:00'))
#print(getPeriodo('2021-09-13', '2021-09-16'))