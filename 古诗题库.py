import random

questions=["白日依山尽，黄河入海流",
           "大漠孤烟直，长河落日圆",
           "会当凌绝顶，一览众山小",
           "举头望明月，低头思故乡"]

authors=["王之涣","王维","杜甫","李白"]
while 1==1 :
    n= random.randint (0,len(questions)-1)

    i=input("请输入"+questions[n]+"的作者:")

    if i == authors[n] :
        print("恭喜你，答对了")
    else :
        print("哎，诗人死不瞑目啊...... 再来一个吧")

           
