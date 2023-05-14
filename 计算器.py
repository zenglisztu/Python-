while 1==1 :
    a=int(input("请输入参数a："))
    b=int(input("请输入参数b："))
    c=int(input("请输入参数c："))
    De=b**2-(4*a*c)
    if De > 0 :
        print((-b+De*(1/2))/2*a)
        print((-b-De*(1/2))/2*a)
    else :
        print("该方程无实数解")
