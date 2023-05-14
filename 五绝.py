top_5=["关羽","张飞","黄忠","马超","赵云"]
top_5a=["于禁","张辽","张郃","徐晃","乐进"]
while 1==1 :
    name=input("请输入您想查询的人物姓名：")

    if name in top_5 :
        print("他是五虎上将之一！")
    elif name in top_5a :
        print("他是五子良将之一！")
    else :
        print("他还得再练练...")
