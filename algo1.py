n = 4
a = [8,5,3,6,2,5,8,9]
b = [4,3,6,8,5,4,6,3]

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

print(betterHalf)