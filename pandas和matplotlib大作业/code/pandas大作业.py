import pandas as pd

df = pd.read_excel('../超市销售记录数据.xls')
df = df.groupby(by='商品名称')['数量'].sum()
df.sort_values(ascending=False, inplace=True)

print(df)
