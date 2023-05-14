goal=int(input("请输入学生的成绩："))
all=0
n=0
while goal != 0 :
    all=all+goal
    n=n+1
    goal=int(input("请输入学生的成绩："))
print("总共登记",n,"名学生")
print("总成绩为：",all) 
