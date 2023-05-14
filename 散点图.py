import matplotlib.pyplot as plt

#plt.rcParams['font.sans-serif']=['fangsong']

mane=['关羽','张飞','黄忠','马超','赵云']

atk=[80,85,50,70,30]

q=[]

color=['c','r','y','b','g']

for a in atk :
    q.append(a*a/10)

plt.grid()
plt.title('五虎上将')
plt.xlabel('将领')
plt.ylabel('战力')
plt.scatter(mane,atk)

plt.show()
