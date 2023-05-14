import random

#将领名单
'''general=["关羽","张飞","黄忠","马超","赵云","于禁","张辽","张郃","徐晃","乐进"]
num=int(input("请输入获奖人数："))
for a in range(num) :
    i=random.randint(0,len(general)-1)

    print("中奖者为：",general[i])



#判断交集    
a=[3,5,"a",10,9,"b"]
b=["c",4,3,"a"]
print(a,b)
print("共同元素包括：")
for i in a :
    for n in b :
        if i==n :
            print(i)




name=["关羽","张飞","黄忠","马超","赵云"]

age=[21,23,40,24,25]

weapon=["青龙偃月刀","丈八蛇矛枪","麒麟弓","长枪","银月枪"]

print(name)

print(age)

print(weapon)
for n in range(5) :
    print(name[n],age[n],weapon[n])




a=range(2,10)
b=range(0,10)


for n in a :
    for i in b :
       no=200+n*10+i
       if i!=3 and i!=5 and i!=7 and no>225 :
           print(no)



a=range(225,300)

for i in a :
    n=i%10
    if n!=5 and n!=7 and n!=3 :
        print(i)
           



names_li = ['张怀1', '李纯1', '王莽1',
            '赵兴1', '周恒1', '张怀2',
            '李纯2', '王莽2', '赵兴2',
            '周恒2', '张怀3']

s=len(names_li)

print("共，",s,"名学生")
print("3~7:",names_li[2:7])
print(names_li[8:s])



scores = [77, 81, 65, 93, 78, 67, 96, 83, 72]

ma=max(scores)

mi=min(scores)

al=sum(scores)

av=al/len(scores)
print("最高成绩是：",ma)
print("最低成绩是：",mi)
print("总成绩是：",al)
print("平均成绩是：",int(av))

a=0
for i in range(101) :
    a=a+i
print(a)

a=0
b=0
for j in range(1,101) :
    if j%2!=0 :
        a=a+j
    elif j%2==0 :
        b=b+j
print(a)
print(b)




a=range(1,10,2)
for i in a :
    print(i)

scores = [77, 81, 65, 93, 78, 67, 96, 83, 72]
print(scores[ : :2])
scores[0]=1
print(scores)
scores.append(4)
print(scores)
scores.count(77)


#创建一个空列表l用于存放所有成绩
l=[]
for n in range(5) :
    
    i=float(input("输入成绩"))

    l.append(i)

#循环结束后所有成绩从小到大排序
#然后旋转，得从大到小排序结果

l.sort()
l.reverse()

print(l)



x=['周一','Mon','周二','Tue','周三','Wed','周四',
   'Thu','周五','Fri','周六','Sat','周日','Sun']

y=x[ : :2]

z=x[1: :2]

print(y)
print(z)

import random
name=input("请输入一个姓名：")
li_1=[]
li=[]
while name!= "END" :
    li.append(name)
    name=input("请输入一个姓名：")

print("您一共输入了",len(li),"个姓名：","中奖者为：")

#for s in range(int(len(li)/2)) :
while len(li_1)<int(len(li)/2) :
    r=random.randint(0,len(li)-1)
    if li[r] not in li_1 :
        li_1.append(li[r])
for s in li_1 :
    print(s)


al=0
for i in range(1,101,2) :
    al=al+i
print(al)




li=["行政部","市场部","销售部","技术部"]

li.append("财务部")
li.append("战略发展部")


li.insert(3,"运营维护部")

print(li)

li=["张怀","李纯","王莽","赵兴","周恒"]

li.pop()
li.remove("李纯")
li.remove("王莽")

print(li)


scores = [77, 81, 65, 93, 78, 67, 96, 83, 72]
scores.sort()
print(scores)
scores.reverse()
print(scores)


scores = [77, 81, 65, 93, 78, 67, 96, 65, 72, 65, 77, 67]

a=scores.count(65)
b=scores.count(67)
print(a)
print(b)

s="甲乙丙丁一一一一二三四"

a=s.replace("一","以")
print(a)'''


s="我一个最爱的深情的相爱的亲爱的人"

c=s.find("的")

while c!=-1 :
    print(c)
    c=s.find("的",c+1)
       


    








