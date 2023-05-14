import math
import winsound

name=input("请输入姓名：")
weight=int(input("请输入体重："))
speed=int(input("请输入速度："))
armor=float(input("请输入盔甲："))

power_level=math.log(0.5*weight*speed**2*(1+armor))

print(name,"战斗力是",power_level)

winsound.Beep (int(200*power_level),1000)
