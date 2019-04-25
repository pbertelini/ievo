# import pandas as pd
# 
# df1 = pd.DataFrame()
# df1['nome'] = ['diego','laila','ethan','lara','nathan']
# df1['sexo'] = ['M','F','M','F','M']
# df1['cpf']  = [111,222,333,444,555]
# 
# # print(df1)
# # print()
# 
# df2 = pd.DataFrame()
# df2['idade'] = ['34','29','-2']
# df2['idade'] = ['34','29','-2']
# df2['desc1'] = ['1','1','1']
# df2['desc2'] = ['2','2','2']
# df2['cpf']  = [111,222,333]

# print(df2)

# merge = pd.merge(df1, df2, how='inner', left_on=['cpf'], right_on=['cpf'])
# print(merge)

# from libs.ana_class_atest_util import day_of_the_week
# 
# print(day_of_the_week(string=True))

# from libs.ana_class_atest_source import empregados_to_pandas, atestados_to_pandas
# 
# 
# e = empregados_to_pandas()
# 
# print(len(e))
# print(e['CPF'].describe)

from libs.ana_class_atest_util import days_ago

print(days_ago('2019-04-20 00:00:00'))