import os
import time
import random
i=0
while i <8 :
    i=random.randint (1,7)
    fname = "start c:/基本音级单音/"+str(i)+".mp3"
    os.system(fname)
    time.sleep(1/random.randint(1,2))
    print(i)
    
