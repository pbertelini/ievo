import pandas as pd

file_name = 'sug_ievo_m20190421_sample.txt'

df = pd.read_csv(file_name, sep=';', header=None)
df.drop(df.head(1).index, inplace=True)

print(df.columns)
print(df.head(3))

