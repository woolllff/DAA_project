
import random 

def partialSort(arr, l, r, k): 
	
	if (k > 0 and k <= r - l + 1): 
		
		pos = selectPartition(arr, l, r) 

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

def MOM(arr,s,e):

    if(e-s +1 <= 5):
        temp = arr[s:e+1]
        temp.sort()
        return temp[int((len(temp)-1)/2)]
    else:
        m = []
        l = range(s,e - e%5,5)
        for i in l:
            temp = arr[i:i+5]
            temp.sort()
            #print(temp,i)
            m.append(temp[2])
        i = l[len(l) -1]
        if ( i+5 <= e):
            temp = arr[i+5:e+1]
            temp.sort()
            #print(temp)
            m.append(temp[int((len(temp)-1)/2)])

        #print(m)
        return MOM(m,0,len(m)-1)


def selectPartition(arr, l, r):
    m = MOM(arr,l,r)
    for i in range(l, r):
        if arr[i] == m:
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

def makebetterhalf(a,b,n):
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
	return betterHalf


if(__name__ == "__main__"):
	n = 4
	a = [8,5,3,6,2,5,8,9]
	b = [4,3,6,8,5,4,6,3]

	ans = makebetterhalf(a,b,n)
	print(ans)
