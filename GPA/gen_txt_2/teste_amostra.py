# -*- coding: utf-8 -*-

import pandas as pd

arquivo = 'amostra.xlsx'
df = pd.read_excel(arquivo)

a = df.groupby(['LOJA', 'PLU'])[['EMBAL']].sum()

print(a)
#for i in a.index:
#    print(' ' + ' ' + '' + str(a[i]))
