
from datetime import datetime
from matplotlib import pyplot as plt

f=open('d:/dome/文本文档/明清.txt','r',encoding='utf-8')

date=f.readlines()

print(date)

name=[]
brith_date=[]


for s in date :
    i=s.replace('\n','')
    x=i.split(',')
    detal=datetime.strptime(x[2],'%Y年%m月%d日')-datetime.strptime(x[1],'%Y年%m月%d日')
    year=int(detal.days/365)
    print(x[0],f'享年{year}')
    name.append(x[0])
    brith_date.append(year)

plt.grid()

plt.title('明清皇帝寿命')

plt.xlabel('皇帝')

plt.ylabel('寿命')

plt.bar(name,brith_date,width=0.3)

plt.show()
