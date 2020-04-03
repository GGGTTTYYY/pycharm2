import xlrd
import pandas as pd
import matplotlib.pyplot as plt
nir = pd.read_excel("大米蛋白粉.xlsx")  # 默认导入第一个表格
data = nir.head()
# print(data)
lihua = pd.read_excel("大米蛋白粉.xlsx",sheet_name="理化值")
data2 = lihua.head()
# print(data2)
# print(type(nir))
y = nir['波长（nm）'].values  # 读取表头为‘波长’的列
# print(y)
# y1 = nir.ix[1]
# print(y1)
x = nir.ix[:,1:]  # 读取所有行 2到最后一列
print(x)
plt.figure()
plt.plot(y,x)
plt.show()