import random
import numpy as np 


n = random.randint(10,50)
a = np.random.randint(1000, size = 2*n)
b = np.random.randint(1000, size = 2*n)


print(n)


c = []
betterHalf = []

for i in range(2*n):
    c.append((a[i]-b[i],i))
    betterHalf.append(0)

c.sort()

# c[i][1] gives the index of the orignal position of the element in a or b 

for i in range(2*n):
    if(i<n):
        betterHalf[c[i][1]] = b[c[i][1]]   # first n elements of c from b 
    else:
        betterHalf[c[i][1]] = a[c[i][1]]   # last n elements of c from a 


for j in range(len(a)):
    print(f"{a[j]} {b[j]} {betterHalf[j]}")
