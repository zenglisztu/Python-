# windows系统
import os

commd = input('请输入命令：')
if commd == '计算器':
    os.system('calc')
if commd == '记事本':
    os.system('notepad')
if commd == '画图':
    os.system('mspaint')
if commd == '控制台':
    os.system('cmd')
