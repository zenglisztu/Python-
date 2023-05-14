import random

ans = random.randint(0,5)

n=0
while 1==1:
    guess=int(input("请猜测一个0-5之间的数字:"))
    if guess < ans or guess > ans:
        print("对不起，猜错了！")
        
    else :
        print("恭喜你，答对了！")
        print("答案是：",ans)
        break
    n=n+1

    if n == 3 :
        print("很遗憾，您的机会用完了")
        print("答案是：",ans)
        break
    
print("游戏结束")
    
