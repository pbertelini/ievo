import pandas as pd

df = pd.DataFrame(columns=['codempresa','codfilial','chapa','DataAtend','QtdeDias','CID','NomeProfissional','MAIL','REGRA'])

df.loc[len(df)]=[
    row['codempresa'],
    row['codfilial'],
    row['chapa'],
    row['DataAtend'],
    row['QtdeDias'],
    row['CID'],
    row['NomeProfissional'],
    row['Emasil'],
    'REGRA']

print(df)

#                         codempresa.append()
#                         codfilial.append()    
#                         chapa.append()    
#                         DataAtend.append(row['DataAtend'])    
#                         QtdeDias.append(row['QtdeDias'])    
#                         CID.append(row['CID'])    
#                         NomeProfissional.append(row['NomeProfissional'])
#                         MAIL.append(row['Emasil'])
#                         REGRA.append('NODE #01')