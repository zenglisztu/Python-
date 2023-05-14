#九九重阳数
for a in (1,10) :
    for b in (0,10) :
        for c in (0,10) :
            for d in (0,10) :
                for e in (0,10) :
                    for f in (0,10) :
                        for g in (0,10) :
                            for h in (0,10) :
                                for i in (0,10) :
                                    sum_1=a**9+b**9+c**9+d**9+e**9+f**9+g**9+h**9+i**9
                                    sum_2=a*100000000+b*10000000+c*1000000+d*100000+e*10000+f*1000+g*100+h*10+i
                                    if sum_1==sum_2 :
                                        print(sum_1)
print("over")
