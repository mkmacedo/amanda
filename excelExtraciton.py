import sys
import pandas as pd


def getRow(filename, cif):
    xls = pd.ExcelFile(filename)
    df = pd.read_excel(xls, 'RG')
    cols = ['DT REC', 'DT ENT', 'Peso bruto', 'Peso líquido', 'CIF R$', 'Valor a pagar']
    
    df = df[cols]

    for i in range(len(df)):
        if str(cif) == str(df.loc[i, 'CIF R$']):
            a,b,c,d,e,f =  df.loc[i,['DT REC', 'DT ENT', 'Peso bruto', 'Peso líquido', 'CIF R$', 'Valor a pagar']]
            return (str(a),str(b),str(c),str(d),str(e),str(f))



#print(df.head())