# DAA_project

## Problem [Better Half](https://algomuse.net/archivecontest?contest_number=20)


### Solution Discription:
<p>

The diffrence array C tells us if we take the element in A instead of B at the same index, then by how much the sum  will increase.

So we just find the n greatest elements in the C array, that will give us the index of the elements we have to take from A and the rest will be taken from B.

Now if we use the sort function we end up with O(nlog(n)), so we can't use sort.

We instead use partial sort which will sort such that any element before a specified k wll be smaller than the element at k, and any element after k will be greater than the element at k. This can be done using the partition technique of the quicksort method, but the worst case becomes O(n^2), to reduce that we will use the median of median technique to find a suitable pivot such that we only work on a ratio of the array each time and that will insure we get worst case O(n).

</p>

### Psudo Codes:
##### Algo1
<p>
Make an array C such as.
C<sub>i</sub> = (A<sub>i</sub> - B<sub>i</sub> , i )
<br>
Sort C WRT the diffrence 
<br>
Then the first n elements are taken from B referencing through C[i][1] and the next n elements are taken from A.
</p>

##### Algo2
<p>

    partialSort(arr, l, r, k)
    n = r - l + 1
    if k > 0 and k <= n
        pos = randomPartition(arr, l, r)
        #Partitions the array about a randomly chosen pivot
        if pos-l == k-1     return
        if pos-l > k-1      return partialSort(arr, l, pos-1, k)
        else    return partialSort(arr, pos+1, r, k-pos+l-1)

    make_better_half(a, b, n)
    #Here c is a new list
    for i from 0 to 2*n-1
        c[i].difference = a[i] - b[i]
        c[i].index = i

    partialSort(c, 0, 2*n -1, n)
    #Here we are sorting the c upto (n-1)th index term and then
    #assigning the first n terms from b and the other n terms from
    #a to betterHalf
    for i from 0 to 2*n -1
        if i < n
            betterHalf[c[i].index] = b[c[i].index]
        else
            betterHalf[c[i].index] = a[c[i].index]
</p>

##### Algo3 
<p>

    partialSort(arr, l, r, k)
    n = r - l + 1
    if k > 0 and k <= n
        pos = selectionPartition(arr, l, r)
        #Partitions the array about the median of the given array
        if pos-l == k-1     return
        if pos-l > k-1      return partialSort(arr, l, pos-1, k)
        else    return partialSort(arr, pos+1, r, k-pos+l-1)


    medianofMedians(arr, l, r)
    median = []
    #Dividing the array into groups of 5 and storing the medians
    #of these groups in median array
    
    #Recursively finding the median of medians
    if r-l < 5
        m = median[0]
    else
        m = medianofMedians(median, 0, len(median)-1)
    return m


</p>

#### Time complexity:
<p>
algo1 - O(nlog(n))
<br>
algo2 - O(n) Average , O(n^2) worst 
<br>
algo3 - O(n) worst
<br>
medianOfmedian is a recursive algo, so it goes like

    n + n/5 + n/25 + ...... 1 = n (1 + 1/5 + 1/25 + ....  ) = 5n/4 = O(n)

partition is a linear algo. compares each element to pivot and makes partition. =O(n).

<br>
Partialsort is a recursive algo. by using Median of median we can eliminate atleast a fraction of the orignal array. r>1

    n + n/r + n/r^2 + ...... 1 = n( 1 + 1/r + 1/r^2 + .... ) = n/(1-1/r) = O(n)
</p>

#### Proof Of Corretness:
<p>
Lets say the ans is some halfset, and given sum(ans) is max.
<br>
now if we subtract a constant from every halfset we still have sum(ans) as max.<br>
Lets take the constant as sum(B)<br>
so the max becomes, sum(ans) - sum(B) == sum(ans[i] - B[i]).<br>
which in turn is sum(n0's + nC[i])<br>
so we need to take the sum of n greatest C[i].
</p>

### Data-structures used:
Array/List(python). 

### Notable Defects / Side Effects: 
One defect that we have encountered is if more than one solution exists, our algo will depend on the arrangement of the array.

### How to run the code:
Run main.py using python3.6 >, it shows a tupple as output which states if the ans by algo3 = to ans by algo1, and if the sum of both the ans are same or not . The makeTestCases.py file is to generate randon testcases and answers using algo1 which takes O(nlog(n)) time. the testcase.txt file stores the testcases as a bunch of 4 lines containing resp n ,A, B ,ans.

### Sourses referred:
https://www.youtube.com/watch?v=fcf56RTbkHc&feature=youtu.be for median of median.
Class notes for Quick Sort.
### Contributions:
##### Utkarsh Agarwal(IMT2018082), Neetha Reddy(IMT2018050)