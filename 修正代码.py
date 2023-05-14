import random

res = random.randint(0, 5)  # 答案
in_num = 0  # 用户输入的值
err_num = 0  # 猜错的次数
level = 1  # 关卡序号
add = 0  # 难度控制
score = 0  # 得分

while 1==1:
    print('\n当前关卡：', level)
    print('您当前的得分是：', score)

    n == int(input(f'请猜测一个数（0~(5 + add)）：'))

    if in_num == res :
        print('恭喜您，答对了！')
        print('您输入的是：', in_num)
        print('正确答案是：', res)
        score + 10
        level + 1
        flag = 1 # 通关标志
    else :
        err_num += 1
        print('对不起，您答错了。')
        if err_num < 3 :
            print(f'您还有{3 - err_num}次机会，请重新输入。')
        else:
            print('正确答案是：', res)
            print('您没有机会了。')
        flag = 2
    # 进入下一关
    if flag == 2 :
        # 增加难度
        add += 2
        res = random.randint(0, 5 + add)
        err_num = 0  # 重置错误次数
    else:
        if err_num == 3:
            print('游戏结束。')
            break
