
import random 

def partialSort(arr, l, r, k):
    n = r - l + 1
    if (k > 0 and k <= r - l + 1):
        a = 0
        medians = []
        for i in range(0, n//5 , 5):
            medians.append(getMedian(arr, l + i, 5))	#Dividing the array into groups of 5 and finding their respective medians
            a += 1
        if (a * 5 < n):					#Last group may have less than 5 elements
            medians.append(getMedian(arr, a*5+l, n%5))
            a += 1


        if (a == 1):					#Recursively finding the median of medians obtained from the groups
            m = medians[0]
        else:
            m = partialSort(medians, 0, a-1, a//2) 

        pos = Partition(arr, l, r, m) 			#Partitioning the array using this median of medians as pivot

        if (pos - l == k - 1): 
            return
        if (pos - l > k - 1): 
            return partialSort(arr, l, pos - 1, k) 
        return partialSort(arr, pos + 1, r, k - pos + l - 1) 

    return 999999999999

def swap(arr, a, b): 
	temp = arr[a] 
	arr[a] = arr[b] 
	arr[b] = temp

def getMedian(arr, l, n):
    temp = []
    mid = n//2
    for i in range(l, l+n):
        temp.append(arr[i])
    temp.sort()
    return temp[mid]

def Partition(arr, l, r, x): 
    for i in range(l, r):
        if arr[i] == x:
            swap(arr, r, i)
            break
    x = arr[r][0]
    i = l 
    for j in range(l, r): 
        if (arr[j][0] <= x): 
            swap(arr, i, j) 
            i += 1
    swap(arr, i, r) 
    return i


# this is an worst case O(n) algo, using partial sort gives us the sorted list such that the nth smallest element is in the correct pos 

n = 4
a = [8,5,3,6,2,5,8,9]
b = [4,3,6,8,5,4,6,3]

c = []
betterHalf = []

for i in range(2*n):
    c.append((a[i]-b[i],i))
    betterHalf.append(0)

partialSort(c,0,2*n -1 ,n)
# c[i][1] gives the index of the orignal position of the element in a or b 

for i in range(2*n):
    if(i<n):
        betterHalf[c[i][1]] = b[c[i][1]]   # first n elements of c from b 
    else:
        betterHalf[c[i][1]] = a[c[i][1]]   # last n elements of c from a 


print(betterHalf)
