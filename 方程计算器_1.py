from math import sqrt

a = int(input('请输入a的值：'))

b = eval(input('请输入b的值：'))

c = eval(input('请输入c的值：'))

if pow(b,2) - 4 * a * c >= 0 :
    
    x1 = (-b + sqrt(pow(b,2) - 4 * a * c)) / (2 * a)

    x2 = (-b - sqrt(pow(b,2) - 4 * a * c)) / (2 * a)
    

#x1 = (-b + (b^2 - 4 * a * c) ** 0.5) / (2 * a)

#x2 = (-b - (b^2 - 4 * a * c) ** 0.5) / (2 * a)
    

    print(f'x1 = {x1}',f'x2 = {x2}')

else :
    print('无实数解')
