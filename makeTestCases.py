import random
import numpy as np 
import json
import algo1 as algo1


f= open("testCases/testcase.txt","w+")
f.close()

f= open("testCases/testcase.txt","a")

for i in range(100):

    n = random.randint(0,50)
    a = list(np.random.randint(1000, size = 2*n))
    b = list(np.random.randint(1000, size = 2*n))
    ans = algo1.makeBetterHalf(a,b,n)
    #l = [n,a,b,ans]
    l = [str(n) +"\n",str(a)+"\n",str(b)+"\n",str(ans)+"\n"]
    for i in l:
        f.write(i)



f.close()
