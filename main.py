import random
import numpy as np 
import json
import algo3 as algo3


f= open("testCases/testcase.txt","r")

#f2 = open("testCases/falsetestcase.txt","a")

contents = f.readlines()
#print(contents)


for i in range(int(len(contents)/4)):

    n = json.loads(contents[i*4 + 0])
    a = json.loads(contents[i*4 + 1])
    b = json.loads(contents[i*4 + 2])
    ans = json.loads(contents[i*4 + 3])

    #print(type(n),type(a),type(b),type(ans))

    ans2 = algo3.makebetterhalf(a,b,n)

    print(( ans == ans2 , sum(ans) == sum(ans2)))

    # if (ans != ans2):
    #     print(n,'\n',a,'\n',b,'\n',ans,'\n',ans2)
    #     l = [str(n) +"\n",str(a)+"\n",str(b)+"\n",str(ans)+"\n",str(ans2)+'\n']
    #     for i in l:
    #         f2.write(i)
    #     c = []
    #     for i in range(len(a)):
    #         c.append(a[i]-b[i])
    #     c.sort()
    #     print(c)


f.close()
#f2.close()