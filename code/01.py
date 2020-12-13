li = [10, 3, 6, 8, 9, 7, 9, 4, 12, 5, 14, 13]
maxPos = li.index(max(li))
minPos = li.index(min(li))
li[0], li[maxPos] = li[maxPos], li[0]
li[len(li) - 1], li[minPos] = li[minPos], li[len(li) - 1]
print("交换后的销售额列表为:", li)
