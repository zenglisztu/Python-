name = age = cla = ''
histy = polic = geopy = ''
phycs = biogy = chery = ''

while True:
    num = input('1-添加学生信息 2-修改学生信息 3-清空学生信息 4-打印学生信息 5-退出程序：')
    if num == '1':
        name = input('-->请输入学生的姓名：')
        age = input('-->请输入学生的年龄：')
        cla = input('-->请输入学生的班级：')
        while True:
            temp = input('1-文科成绩 2-理科成绩 3-退出：')
            if temp == '1':
                histy = input('---->请输入历史成绩：')
                polic = input('---->请输入政治成绩：')
                geopy = input('---->请输入地理成绩：')
                print('历史：' + histy + ' ' + '政治：' + ' ' + polic + ' ' + '地理：' + geopy)
            elif temp == '2':
                phycs = input('---->请输入物理成绩：')
                biogy = input('---->请输入生物成绩：')
                chery = input('---->请输入化学成绩：')
                print('物理：' + phycs + ' ' + '生物：' + ' ' + biogy + ' ' + '化学：' + chery)
            elif temp == '3':
                break
            else:
                print('输入有误，请重新输入！')
    elif num == '2':
        while True:
            temp = input('1-文科成绩 2-理科成绩 3-退出：')
            if temp == '1':
                histy = input('---->请修改历史成绩：')
                polic = input('---->请修改政治成绩：')
                geopy = input('---->请修改地理成绩：')
                print('历史：' + histy + ' ' + '政治：' + ' ' + polic + ' ' + '地理：' + geopy)
            elif temp == '2':
                phycs = input('---->请修改物理成绩：')
                biogy = input('---->请修改生物成绩：')
                chery = input('---->请修改化学成绩：')
                print('物理：' + phycs + ' ' + '生物：' + ' ' + biogy + ' ' + '化学：' + chery)
            elif temp == '3':
                break
            else:
                print('输入有误，请重新输入！')
    elif num == '3':
        name = age = cla = ''
        histy = polic = geopy = ''
        phycs = biogy = chery = ''
        print('学生成绩已经被清空')
    elif num == '4':
        print('学生信息：')
        print('姓名：' + name + ' ' + '年龄：' + ' ' + age + ' ' + '班级：' + cla)
        print('历史：' + histy + ' ' + '政治：' + ' ' + polic + ' ' + '地理：' + geopy)
        print('物理：' + phycs + ' ' + '生物：' + ' ' + biogy + ' ' + '化学：' + chery)
    elif num == '5':
        print('程序退出')
        break
    else:
        print('输入有误，请重新输入！')
