from DescricaoNFS import getCleanDescriptionType1

docs_std_resolution = {
                        'AGV': {'NFS': (2480, 3509), 'recibo_locacao': (2550, 3300), 'mapa_faturamento': (2550, 3300),'custo_frete':(1753,1240),'fatura_duplicata': (989,1280)},
                        'GKO': {'NFS': (3175, 4150)},
                        'MOVEIDEIAS': {'NFS': (2480, 3509)},
                        'RIO': {'NFS': (2480, 3509)},
                        'RODOLOG': {'NFS': (2483,3512), 'fatura_duplicata': (2480, 3509)},
                        'RUNTEC': {'NFS': (2480, 3525)},
                        'SHIFT': {'NFS': (2480, 3509), 'nota_debito': (2481, 3509)},
                        'DIREMADI': {'NFS': (2480, 3509), 'fatura_duplicata': (1654, 1182)},
                        'DENISE': {'NFS': (2479, 3509)},
                        'LINE': {'NFS':(1240,1755), 'fatura_duplicata':(1240,1755),'custo_frete':(1753,1240)},
                        #'ANDREANI':{'fatura_duplicata':(1240,1755), 'custo_frete':(1753,1240)},
                        'ANDREANI':{'fatura_duplicata':(1653,2339), 'custo_frete':(1753,1240)},
                        'FL':{'DACTE':(1240,1753), 'custo_frete':(1753,1240),'fatura_frete':(1241,1755)},
                        None:{'fatura_frete': (1241,1755)},
                        'MULTIRIO':{'NFS':(1240,1755),'boleto':(1240,1755)},
                        'ICTSI':{'NFS':(1240,1755),'boleto':(1240,1755), 'detalhamento_notafiscal': (1653,2339)},
                        'DHL':{'nota_debito':(1240,1755),'NFS':(1240,1755)},
                        'MULTITERMINAIS':{'minuta_calculo':(1275,1650),'boleto':(1240,1755)},
                        'SENIOR': {'NFS': (2480, 3525)}
                       }

dict_document = {
                'NFS': ['CNPJ', 'con', 'vencimento', 'nome', 'PO', 'valor', 'descricao','pesoBruto',],  #'desconto'],
                'recibo_locacao': ['con', 'nome', 'PO', 'valor'],# 'contaContabil', 'centroCusto','desconto'],
                'nota_debito': ['con', 'vencimento', 'nome', 'PO', 'valor','descricao','pesoBruto'], #'descricao','desconto'],
                'mapa_faturamento': ['PO', 'con', 'valor', 'nome', 'CNPJ'],#'desconto'],
                'fatura_duplicata': ['con', 'CNPJ', 'vencimento', 'nome', 'PO', 'valor', 'descricao', 'desconto'],#'desconto','valorAPagar']
                'custo_frete':['nome', 'con','CNPJ','valor'], 
                'DACTE':['con','CNPJ','nome','valor','vencimento'],
                'fatura_frete':['CNPJ','vencimento','valor'],
                'detalhamento_notafiscal':['valor','valorSemImposto','CIF','taxa','descricao','nome','moeda', 'dataEntrada', 'dataSaida'], #'tipoServico','periodo'
                'minuta_calculo':['nome','valorCIF','valor','CNTR','descricao','periodo','dataEntrada', 'dataSaida'],#periodo = data de envio at?? data chegada
                'boleto':['valor','data','con']
                 }

docTypeMap = {'mapa de faturamento': 'mapa_faturamento',
                'mapa faturamento': 'mapa_faturamento',
                'recibo loca????o': 'recibo_locacao',
                'recibo locacao': 'recibo_locacao',
                'recibo de loca????o': 'recibo_locacao',
                'recibo de locacao': 'recibo_locacao',
                'nota fiscal de servi??o': 'NFS',
                'nfs-e': 'NFS',
                'nfs': 'NFS',
                'fatura duplicata': 'fatura_duplicata',
                'fatura/duplicata': 'fatura_duplicata',
                'comprovante de entrega': 'fatura_duplicata',
                'comprovante entrega': 'fatura_duplicata',
                'duplicata': 'fatura_duplicata',
                'frete cif': 'fatura_duplicata',
                'nota fiscal': 'NFS',
                'custo de frete': 'custo_frete',
                'custo frete': 'custo_frete',
                'nota de debito': 'nota_debito',
                'nota de d??bito': 'nota_debito',
                'nota d??bito': 'nota_debito',
                'nota debito': 'nota_debito',
                'dacte': 'DACTE',
                'conferencia de faturas': 'fatura_frete',
                'detalhamento dos itens da nota fiscal': 'detalhamento_notafiscal',
                'minuta de calculo':'minuta_calculo',
                'minuta calculo':'minuta_calculo',
                'Minuta de C??culo':'minuta_calculo'
                }

docHierarchy = {
                'boleto':11,
                'minuta_calculo': 10,
                'detalhamento_notafiscal': 9,
                'fatura_frete': 8,
                'nota_debito': 7,
                'DACTE': 6,
                'recibo_locacao': 5,
                'mapa_faturamento': 4,
                'custo_frete': 3,
                'fatura_duplicata': 2,
                'NFS': 1
                }
#AGV
dict_map = {}
dict_map['AGV'] = {}
dict_map['AGV']['NFS'] = {'CNPJ': (440, 760, 580, 630), 'con': (1910, 2164, 270, 320), 'vencimento': (470, 700, 1240, 1274),
                          'nome': (550, 930, 640, 690), 'PO': (310, 540, 1280, 1325), 'valor': (1300, 1575, 2144, 2188), 'descricao': (245, 2175, 1200, 1235)}

dict_map['AGV']['mapa_faturamento'] = {'CNPJ': (1050, 1400, 1790, 1845),'con': (940, 1140, 735, 800), 'nome': (1037, 1412, 1752, 1793),'PO':(440, 2330, 860, 1080) ,
                                      'valor': (1933,2480, 1445, 1505)}

dict_map['AGV']['recibo_locacao'] = {'CNPJ': (230, 450, 430, 460),'con': (1949, 2105, 830, 889), 'nome': ( 1037, 1453, 2133, 2177),'PO':(255, 537, 1225, 1300) ,
                                      'valor': (1601,2057, 1580, 1630)}

dict_map['AGV']['custo_frete'] = {'con':(333, 383, 255, 278) ,'CNPJ':(292, 475, 406, 431) ,'nome':(483, 785, 404, 431),'valor':(1465, 1595, 670, 695)}

dict_map['AGV']['fatura_duplicata'] = {'con': (150, 230, 760, 780) ,'vencimento': (683, 787, 758, 780), 'nome': (560, 720, 500, 518), 
                                    'valor': (760, 920, 410, 430), 'CNPJ': (550, 716, 570, 595), 'desconto': (440, 550, 757, 781)}

#dict_map['AGV']['nota_debito'] = {}

#GKO
dict_map['GKO'] = {}
dict_map['GKO']['NFS'] = {'CNPJ': (350, 840, 590, 650), 'con': (2650, 3050, 90, 165), 'vencimento': (420, 780, 2370, 2440), 'nome': (550, 1250, 670, 750),
                          'PO': (40, 3130, 1480, 2880), 'valor': (1780, 2120, 3020, 3100), 'descricao': (40, 3130, 1480, 2880)}
#'descricao': (40, 2600, 1550, 1900)

#dict_map['GKO']['mapa_faturamento'] = {}
#dict_map['GKO']['recibo_locacao'] = {}
#dict_map['GKO']['fatura_duplicata'] = {}
#dict_map['GKO']['nota_debito'] = {}

#SHIFT
dict_map['SHIFT'] = {}
dict_map['SHIFT']['NFS'] = {'CNPJ': ( 445, 753, 582, 619), 'con': (1919, 2159, 267, 310), 'vencimento': ( 495,715, 1580, 1614),
                          'nome': (579, 1165, 641, 679), 'PO': (641, 853, 1320, 1355), 'valor': (1310,1563, 2142, 2195), 'descricao': (249,693, 1200, 1238)}

#dict_map['SHIFT']['mapa_faturamento'] = {}
#dict_map['SHIFT']['recibo_locacao'] = {}
#dict_map['SHIFT']['fatura_duplicata'] = {}
dict_map['SHIFT']['nota_debito'] = {'con': ( 557, 703, 853, 893), 'vencimento': (1763, 1973, 850, 899),
                          'nome': (167, 1485, 213, 285), 'PO': (617, 855, 1960, 2020), 'valor': (1947,2191, 2801, 2860), 'descricao': (167, 1147, 2012, 2104)}

#RUNTEC
dict_map['RUNTEC'] = {}
dict_map['RUNTEC']['NFS'] = {'CNPJ': (577, 890, 750, 790), 'con': (1790, 1980, 210, 280), 'vencimento': ( 143,420, 1650, 1730),
                          'nome': ( 737, 1400, 600, 650), 'PO': (551, 751, 1473, 1511), 'valor': (687,890, 2583, 2630), 'descricao': (49, 2043, 1399, 1439)}

#dict_map['RUNTEC']['mapa_faturamento'] = {}
#dict_map['RUNTEC']['recibo_locacao'] = {}
#dict_map['RUNTEC']['fatura_duplicata'] = {}
#dict_map['RUNTEC']['nota_debito'] = {}

#MOVEIDEIAS
dict_map['MOVEIDEIAS'] = {}
dict_map['MOVEIDEIAS']['NFS'] = {'CNPJ': (930, 1320, 380, 420), 'con': (340, 680, 227, 300), 'vencimento': (343, 465, 977, 1007),
                          'nome': (720, 2230, 330, 380), 'PO': (640, 800, 915, 940), 'valor': (1010, 1200, 1730, 1790), 'descricao': (250, 1330, 950, 975)}

#dict_map['MOVEIDEIAS']['mapa_faturamento'] = {}
#dict_map['MOVEIDEIAS']['recibo_locacao'] = {}
#dict_map['MOVEIDEIAS']['fatura_duplicata'] = {}
#dict_map['MOVEIDEIAS']['nota_debito'] = {}

#RIO
dict_map['RIO'] = {}
dict_map['RIO']['NFS'] = {'CNPJ': (730, 1090, 670, 720), 'con': (2050, 2250, 220, 260), 'vencimento': (10, 20, 10, 20),
                          'nome': (880, 1520, 730, 780), 'PO': (10, 20, 10, 20), 'valor': (2060, 2360, 2720, 2780), 'descricao': (97, 2370, 2510, 2620)}

#dict_map['RIO']['mapa_faturamento'] = {}
#dict_map['RIO']['recibo_locacao'] = {}
#dict_map['RIO']['fatura_duplicata'] = {}
#dict_map['RIO']['nota_debito'] = {}

#RODOLOG
dict_map['RODOLOG'] = {}
dict_map['RODOLOG']['NFS'] = {'CNPJ': (1429, 1687, 540, 571), 'con': (2107, 2261, 798, 834), 'vencimento': (1149, 1351, 735, 780),
                          'nome': (893, 1571, 361, 399), 'PO': (10, 20, 10, 20), 'valor': (2030, 2313, 2881, 2930), 'descricao': (187, 2247, 1484, 1518)}

#dict_map['RODOLOG']['mapa_faturamento'] = {}
#dict_map['RODOLOG']['recibo_locacao'] = {}
dict_map['RODOLOG']['fatura_duplicata'] = {'con': (225, 365, 2005, 2050) ,'vencimento': (2015, 2230, 682, 730), 'nome': (337, 1231, 375, 420), 
                                           'PO': (10, 20, 10, 20) , 'valor': (2185, 2357, 1540, 1580), 'descricao': (120, 945, 1770, 1820), 'desconto': (2050, 2370, 1430, 1490)}
#dict_map['RODOLOG']['nota_debito'] = {}

#DIREMADI
dict_map['DIREMADI'] = {}
dict_map['DIREMADI']['NFS'] = {'CNPJ': (720, 1025, 579, 620), 'con': (1915, 2165, 265, 310), 'vencimento': (10, 20, 10, 20),
                          'nome': (853, 1549, 635, 681), 'PO': (374, 599, 1237, 1273), 'valor': (1311, 1570, 2140, 2188), 'descricao': (245, 2000, 1196, 1500)}

dict_map['DIREMADI']['fatura_duplicata'] = {'con': (370, 510, 400, 450) ,'vencimento': (1000, 1170, 400, 450), 'nome': (70, 700, 250, 290), 
                                           'PO': (523, 790, 495, 540) , 'valor': (600, 750, 400, 450), 'descricao': (300, 1577, 610, 760), 'desconto': (440, 590, 460, 495)}

#dict_map['DIREMADI']['mapa_faturamento'] = {}
#dict_map['DIREMADI']['recibo_locacao'] = {}
#dict_map['DIREMADI']['fatura_duplicata'] = {}
#dict_map['DIREMADI']['nota_debito'] = {}

#DENISE
dict_map['DENISE'] = {}
dict_map['DENISE']['NFS'] = {'CNPJ': (432, 800, 560, 640), 'con': (1903, 2200, 261, 311), 'vencimento': (10, 20, 10, 20),
                          'nome': (575, 1183, 635, 678), 'PO': (317, 583, 1311, 1359), 'valor': (1327, 1565, 2140, 2185), 'descricao': (245, 2229, 1194, 2079)}

#dict_map['DENISE']['mapa_faturamento'] = {}
#dict_map['DENISE']['recibo_locacao'] = {}
#dict_map['DENISE']['fatura_duplicata'] = {}
#dict_map['DENISE']['nota_debito'] = {}

#LINE
dict_map['LINE'] = {}
dict_map['LINE']['NFS'] = {'CNPJ': (379, 535, 370, 393), 'con': (862, 927, 220, 240), 'vencimento': (10, 20, 10, 20),
                          'nome': (237, 683,290, 309), 'PO': (91, 1132, 686, 1101), 'valor': (991, 1100, 1285, 1310), 'descricao': (91, 1132, 686, 1101)}
dict_map['LINE']['fatura_duplicata'] = {'con': (254, 319, 251, 278) ,'vencimento': (930, 1041, 251, 277), 'nome': (295,790, 86, 112), 'PO': (207, 1170,318, 387) , 
                                        'valor': (395, 505, 252,277), 'descricao': (207, 1170,318, 387), 'desconto':(559,636,250,278),'valorAPagar':(673,777,250,278)}
dict_map['LINE']['custo_frete'] = {'con':(333, 383, 255, 278) ,'CNPJ':(292, 475, 406, 431) ,'nome':(483, 785, 404, 431),'valor':(1465, 1595, 670, 695)}
#dict_map['LINE']['mapa_faturamento'] = {}
#dict_map['LINE']['recibo_locacao'] = {}
#dict_map['LINE']['nota_debito'] = {}

#ANDREANI
dict_map['ANDREANI'] = {}
#dict_map['ANDREANI']['NFS'] = {}
#dict_map['ANDREANI']['fatura_duplicata'] = {'con': (175, 260, 170, 190) ,'vencimento': (57, 139, 175, 195), 'nome': (56, 282, 103, 125), 
#                                        'valor': (485, 645, 175, 199), 'CNPJ': (373, 488, 365, 381)}
dict_map['ANDREANI']['fatura_duplicata'] = {'con': (230, 400, 226, 270) ,'vencimento': (70, 210, 226, 270), 'nome': (380, 720, 405, 438), 
                                        'valor': (650, 900, 226, 270), 'CNPJ': (400, 650, 473, 520), 'desconto': (10,20,10,20)}
dict_map['ANDREANI']['custo_frete'] = {'con':(333, 383, 255, 278) ,'CNPJ':(292, 475, 406, 431) ,'nome':(483, 785, 404, 431),'valor':(1465, 1595, 670, 695)}

#dict_map['ANDREANI']['mapa_faturamento'] = {}
#dict_map['ANDREANI']['recibo_locacao'] = {}
#dict_map['ANDREANI']['nota_debito'] = {}

#FLBRASIL
dict_map['FL'] = {}
dict_map['FL']['fatura_duplicata'] = {'con': (553, 640, 148, 167) ,'vencimento': (653, 757, 148, 168), 'nome': (192, 395, 80, 189), 
                                        'valor': (1038, 1212, 846,872), 'CNPJ': (67, 190, 235, 255), 'desconto': (10,20,10,20)}

dict_map['FL']['custo_frete'] = {'con':(330,402, 254,276) ,'CNPJ':(333,476, 405,430) ,'nome':(483,725, 407,430),'valor':(1470,1624, 592,615)}
dict_map['FL']['DACTE'] = {'con': (553, 640, 148, 167) ,'vencimento': (653, 757, 148, 168), 'nome': (192, 395, 80, 189), 
                                        'valor': (1038, 1212, 846,872), 'CNPJ': (67, 190, 235, 255)}

dict_map['FL']['fatura_frete'] = {'CNPJ':(322,440,102,113), 'vencimento':(1060,1168,128,142), 'valor':(1057,1133,268,282)}
dict_map[None] = {}
dict_map[None]['fatura_frete'] = {'CNPJ':(322,440,102,113), 'vencimento':(1060,1168,128,142), 'valor':(1,5,1,5)}#(1057,1133,268,282)}
#dict_map['FL']['mapa_faturamento'] = {}
#dict_map['FL']['recibo_locacao'] = {}
#dict_map['FL']['nota_debito'] = {}

#MULTI RIO
dict_map['MULTIRIO'] = {}
dict_map['MULTIRIO']['NFS'] = {'CNPJ': (213,365,295,313), 'con': (939,1050,135,157), 'vencimento': (898,1005,182,205),
                          'nome': (278,618,320,339), 'PO': (115,1089,601,1066), 'valor': (639,810,1076,1098), 'descricao': (115,1089,601,1066)}

#dict_map['MULTIRIO']['fatura_duplicata'] = {}
#dict_map['MULTIRIO']['custo_frete'] = {}
#dict_map['MULTIRIO']['mapa_faturamento'] = {}
#dict_map['MULTIRIO']['recibo_locacao'] = {}
#dict_map['MULTIRIO']['nota_debito'] = {}

#ICTSI
dict_map['ICTSI'] = {}
dict_map['ICTSI']['NFS'] = {'CNPJ': (359,510,293,313), 'con': (957,1082,135,158), 'vencimento': (918,1030,181,202),
                          'nome': (425,700,320,338), 'PO': (122,1111,1063,1231), 'valor': (650,785,1071,1092), 'descricao': (122,1111,600,1063)}
#dict_map['ICTSI']['fatura_duplicata'] = {}
#dict_map['ICTSI']['custo_frete'] = {}
#dict_map['ICTSI']['mapa_faturamento'] = {}
#dict_map['ICTSI']['recibo_locacao'] = {}
#dict_map['ICTSI']['nota_debito'] = {}
dict_map['ICTSI']['detalhamento_notafiscal'] = {'CIF':(650,830,835,890),'taxa':(1300,1500,835,890),'descricao':(62,1195,100,1395),'tipoServico':(60,1170,1525,1725),
                                                'nome':(40,400,45,150),'moeda':(995,1105,670,689),'periodo':(62,145,898,919),'valor':(10,20,10,20),'valorSemImposto':(10,20,10,20), 'dataEntrada': (1120, 1260, 440, 495), 'dataSaida': (1320,1440, 120, 175)}

#DHL
dict_map['DHL'] = {}
dict_map['DHL']['NFS'] = {'CNPJ': (361,571,249,267), 'con': (970,1042,54,73), 'vencimento': (960,1058,152,168),
                          'nome': (445,795,266,298),'valor': (355,465,1330,1345), 'descricao': (23,1209,593,1219)}

#dict_map['DHL']['fatura_duplicata'] = {}
#dict_map['DHL']['custo_frete'] = {}
#dict_map['DHL']['mapa_faturamento'] = {}
#dict_map['DHL']['recibo_locacao'] = {}
dict_map['DHL']['nota_debito'] = {'con': (1089,1155, 21, 40), 'vencimento': (865,945,171,190),
                          'nome': (267,600,45,77), 'valor': (969,1200,1423,1445),'descricao':(22,1201,533,1153)}

#MULTITERMINAIS
dict_map['MULTITERMINAIS'] = {}
#dict_map['MULTITERMINAIS']['NFS'] = {}
#dict_map['MULTITERMINAIS']['fatura_duplicata'] = {}
#dict_map['MULTITERMINAIS']['custo_frete'] = {}
#dict_map['MULTITERMINAIS']['mapa_faturamento'] = {}
#dict_map['MULTITERMINAIS']['recibo_locacao'] = {}
#dict_map['MULTITERMINAIS']['nota_debito'] = {}
dict_map['MULTITERMINAIS']['minuta_calculo'] = {'nome':(190,450,160,230),'valorCIF':(925,1095,402,425),'valor':(965,1091,969,1000),'CNTR':(365,427,510,550),'descricao':(160,530,735,850),'periodo':(670,870,600,640), 'dataEntrada':(895,975, 780, 810), 'dataSaida':(985,1070,780,810)}

#SENIOR
dict_map['SENIOR'] = {}
dict_map['SENIOR']['NFS'] = {'CNPJ': (730, 1030, 452, 510), 'con': (2000, 2360, 220, 280), 'vencimento': (10, 20, 10, 20),
                          'nome': (620, 1180, 210, 270), 'PO': (105, 2360, 1040, 2230), 'valor': (1420, 2360, 2740, 2800), 'descricao': (105, 2360, 1040, 2230)}

companies = ['AGV LOGISTICA SA', 
            'RODOLOG TRANSPORTES MULTIMODAIS LTDA', 
            'DIREMADI MARKETING E SERVICOS LTDA', 
            'SHIFT GESTAO DE SERVICOS LTDA', 
            'RUNTEC INFOMATICA LTDA', 
            'DENISE DOS ANJOS PINTO LUCENA',
            'GKO INFORMATICA LTDA',
            'MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA',
            'RIO LOPES TRANSPORTES LTDA',
            'LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA',
            'ANDREANI LOGISTICA LTDA',
            'FL BRASIL HOLDING LOGISTICA E TRANSPORTE LTDA',
            'MULTI RIO OPERACOES PORTUARIAS S/A',
            'ICTSI RIO BRASIL TERMINAL 1 SA',
            'DHL GLOBAL FORWARDING (BRAZIL) LOGISTICS LTDA',
            'MULTITERMINAIS LOGISTICA INTEGRADA',
            'SENIOR SISTEMAS'
            ]

listaCNPJ = [
            '05.214.772/0001-40', # - rodolog ok
            '02.905.424/0066-76', # - agv ko
            '21.026.581/0001-00', # - moveideias
            '29.519.838/0001-14', # - rio
            '04.134.548/0001-85', # - runtec
            '24.936.646/0001-43', # - Denise
            '08.709.969/0001-48', # - Shift
            '31.334.600/0001-10', # - GKO
            '35.905.090/0001-44', # - Diremadi
            '18.233.211/0015-35', # - FL
            '04.887.927/0015-41', # - Andreani
            '07.117.576/0001-82', # - Line
            '02.887.283/0002-60', #MULTIRIO
            '10.228.777/0008-38', #DHL
            '02.373.517/0001-51', #ICTSI
            '80.680.093/0030-16'
            ]

mapNameCNPJ = {
            '05.214.772/0001-40': 'RODOLOG TRANSPORTES MULTIMODAIS LTDA',
            '02.905.424/0066-76': 'AGV LOGISTICA SA',
            '21.026.581/0001-00': 'MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA',
            '29.519.838/0001-14': 'RIO LOPES TRANSPORTES LTDA',
            '04.134.548/0001-85': 'RUNTEC INFOMATICA LTDA',
            '24.936.646/0001-43': 'DENISE DOS ANJOS PINTO LUCENA',
            '08.709.969/0001-48': 'SHIFT GESTAO DE SERVICOS LTDA',
            '31.334.600/0001-10': 'GKO INFORMATICA LTDA',
            '35.905.090/0001-44': 'DIREMADI MARKETING E SERVICOS LTDA',
            '18.233.211/0015-35': 'FL BRASIL HOLDING LOGISTICA E TRANSPORTE LTDA',
            '04.887.927/0015-41': 'ANDREANI LOGISTICA LTDA',
            '07.117.576/0001-82': 'LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA',
            '02.887.283/0002-60': 'MULTI RIO OPERACOES PORTUARIAS S/A',
            '10.228.777/0008-38': 'DHL GLOBAL FORWARDING (BRAZIL) LOGISTICS LTDA',
            '02.373.517/0001-51': 'ICTSI RIO BRASIL TERMINAL 1 SA',
            '80.680.093/0030-16': 'SENIOR SISTEMAS'
            }

mapLongShort = {'AGV': 'AGV LOGISTICA SA', 
                'RODOLOG': 'RODOLOG TRANSPORTES MULTIMODAIS LTDA', 
                'DIREMADI': 'DIREMADI MARKETING E SERVICOS LTDA', 
                'SHIFT': 'SHIFT GESTAO DE SERVICOS LTDA', 
                'RUNTEC': 'RUNTEC INFOMATICA LTDA', 
                'DENISE': 'DENISE DOS ANJOS PINTO LUCENA',
                'GKO': 'GKO INFORMATICA LTDA',
                'MOVEIDEIAS': 'MOVEIDEIAS CONSULTORIA E INTEGRACAO DE NEGOCIOS LTDA',
                'RIO': 'RIO LOPES TRANSPORTES LTDA',
                'LINE': 'LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA',
                'LINEX': 'LINE EXPRESS TRANSPORTES E DISTRIBUICAO LTDA',
                'ANDREANI': 'ANDREANI LOGISTICA LTDA',
                'FL': 'FL BRASIL HOLDING LOGISTICA E TRANSPORTE LTDA',
                'FLBRASIL': 'FL BRASIL HOLDING LOGISTICA E TRANSPORTE LTDA',
                'MULTI': 'MULTI RIO OPERACOES PORTUARIAS S/A',
                'ICTSI': 'ICTSI RIO BRASIL TERMINAL 1 SA',
                'DHL': 'DHL GLOBAL FORWARDING (BRAZIL) LOGISTICS LTDA',
                'MULTITERMINAIS': 'MULTITERMINAIS LOGISTICA INTEGRADA',
                'SENIOR': 'SENIOR SISTEMAS'
                }

field_validation = {
                    'nome': r'(?:[a-zA-Z]+| |\(|\)|[0-9])+',
                    'valor': r'(?:[0-9]+\.?)+(?:,[0-9][0-9])?',
                    'vencimento': r'[0-9][0-9]/[0-9][0-9]/(?:[0-9][0-9][0-9][0-9]|[0-9][0-9])',
                    'con': r'(?:[a-z]*[A-Z]*[0-9]+|/|-)+',
                    'CNPJ': r'[0-9][0-9]\.[0-9][0-9][0-9]\.[0-9][0-9][0-9]/[0-9][0-9][0-9][0-9]-[0-9][0-9]',
                    'PO': r'[0-9][0-9]+',
                    'CNTR': r'[0-9][0-9]',
                    'dataEntrada': r'[0-9][0-9](?:-|/)[0-9][0-9](?:-|/)[0-9][0-9][0-9][0-9]',
                    'dataSaida': r'[0-9][0-9](?:-|/)[0-9][0-9](?:-|/)[0-9][0-9][0-9][0-9]'
                    }

manyPagesDocList = ['custo_frete', 'fatura_frete', 'fatura_duplicata', None]

descriptionByNFSType = {
            'DENISE': lambda x: getCleanDescriptionType1(x),
            'DIREMADI': lambda x: getCleanDescriptionType1(x),
            'AGV': lambda x: getCleanDescriptionType1(x),
            }

# NFS DENISE servicoPrestado:(170,1038,1085) , GKO servicoPrestado:(28,1240,1306), RIO servicoPrestado:(85,2450,2624)
# NFS AGV servicoPrestado(243,2200,2304), SHIFT servicoPrestado:(170,1035,1085)