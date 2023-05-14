while True :
    number=int(input("请输入需要判断的数字："))

    rema=number%2

    if number==0 or rema==0 :
        print("偶数")
    else :
        print("奇数")

