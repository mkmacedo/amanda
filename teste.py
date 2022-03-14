a = '1.003,92'

b = a.replace('.', '').replace(',','')

c = b[:-2]+'.'+b[-2:]

print(c)