import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'simhei'
df = pd.read_excel('../.archivetemp营业额数据.xlsx')
df.loc[df.交易额 > 3000, '交易额'] = 3000
df.loc[df.交易额 < 200, '交易额'] = 200
df.drop_duplicates(inplace=True)
df['交易额'].fillna(df['交易额'].mean(), inplace=True)
df_group = pd.crosstab(df.姓名, df.柜台, df.交易额, aggfunc='mean').apply(round)
df_group.plot(kind='bar')
plt.xlabel('员工不同柜台业绩平均分布值')
plt.legend(labels=['化妆品', '日用品', '蔬菜水果', '食品'], loc='upper right')
plt.show()
