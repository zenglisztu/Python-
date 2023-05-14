#主菜单：1-添加学生信息 2-修改学生信息 3-清空学生信息 4-打印学生信息 5-退出程序
print("主菜单：1-添加学生信息\
      2-修改学生信息\
      3-清空学生信息\
      4-打印学生信息\
      5-退出程序")
sum_1=0
op=int(input("请选择主菜单："))
while sum_1==0 and op==1 :
    #if op==1 :
           name=input("请输入学生姓名：")
           class_1=input("请输入学生班级：")
           print("1-文科成绩 2-理科成绩 3-退出")
           op1=int(input("请选择："))
           if op1==1 :

                   his=input("请输入历史成绩：")
                   pol=input("请输入政治成绩：")
                   geo=input("请输入地理成绩：")
                   sum_1=his+pol+geo
                   print(name,class_1)
                   print("历史:",his,"政治",pol,"地理",geo)
           elif op1==2 :
                   physics=input("请输入物理成绩：")
                   chemistry=input("请输入化学成绩：")
                   biology=input("请输入生物成绩：")
                   sum_1=physics+chemisty+biology
                   print(name,class_1)
                   print("物理:",his,"化学",pol,"生物",geo)
           elif op1==3 :
               sum_1=99999999

op=int(input("请选择主菜单："))
           


