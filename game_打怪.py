'''模拟游戏战斗系统的程序，玩家可以多次选择攻击方式，直到怪物死亡。

玩家的技能菜单：1-物理攻击，2-魔法攻击，根据编号选择技能。

玩家的物理攻击力100，魔法攻击力120，怪物的血量700，物理防御力80，魔法防御力75

伤害 = 技能攻击力 * 随机系数 - 防御力

怪物血量 = 总血量 - 伤害

其中随机系数在1~2之间，2为暴击。每次攻击后显示怪物的原始血量和剩余血量，如果发生暴击显示“暴击攻击”。'''
import random

phyatk=100 #物理伤害
magatk=120 #法术伤害

enemy_hp=700 #血量
enemy_pdef=80 #物抗
enemy_mdef=75 #魔抗


while enemy_hp > 0 :
    
    a=int(input("1-物理攻击，2-魔法攻击:")) #攻击方式
    i=random.randint(1,2) #随机系数
    
    if a==1 :
        enemy_hp=enemy_hp-(phyatk*i-80)
        if i == 2 :
            print("暴击")
        print("物理伤害",phyatk*i-80)
        print(enemy_hp,"700")
    elif a ==2 :
        enemy_hp=enemy_hp-(magatk*i-75)
        if i == 2 :
            print("暴击")
        print("魔法伤害",magatk*i-80)
        print(enemy_hp,"700")
    else :
        print("攻击方式有误")

print("敌人阵亡")
print("游戏结束")


