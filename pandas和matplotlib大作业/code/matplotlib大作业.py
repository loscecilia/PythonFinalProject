import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'simhei'

df = pd.read_excel('../超市销售记录数据.xls')
df = df.groupby(by='商品名称')['数量'].sum()
df.sort_values(ascending=False, inplace=True)
res = df.head(10)

plt.figure(figsize=(9, 8))
res.plot(kind='bar')
plt.xticks(rotation=30)
plt.ylabel('数量')
plt.title('前10名商品销量统计')

plt.show()
