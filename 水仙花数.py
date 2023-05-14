for a in range(1,10) :
    for b in range(0,10) :
        for c in range(0,10) :
            a1=a**3
            b1=b**3
            c1=c**3
            sum_1=a1+b1+c1
            
            sum_2=a*100+b*10+c
            if sum_1==sum_2 :
                print(sum_1)
