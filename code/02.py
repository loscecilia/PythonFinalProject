import xlrd
df = xlrd.open_workbook(r'../.archivetemp某班某科目成绩.xlsx')
table = df.sheets()[0]
score = table.col_values(1)
del score[0]
num = 0
for i in score:
    if i >= 70:
        num += 1
print('成绩为70分以上的人数占比为：{:.2%}'.format(num/len(score)))
