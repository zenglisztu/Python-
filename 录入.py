print("欢迎进入会员录入系统，请开始录入")
s="y"
i=0
total=0
while s== "y" :
    house=int(input("请输入房产数量："))
    if house >5 :
        print("超级会员")
    elif house >3 :
        print("高级会员")
    else :
        print("普通会员")
    i=i+1
    total=total+house
    s=input("是否继续录入？（y/n)")
print("本次共录入",i,"名会员",total,"套房产")
print("程序执行结束，再见")
