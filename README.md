# DAA_project

## Problem [Better Half](https://algomuse.net/archivecontest?contest_number=20)


### Solution Description:
<p>

The difference array C gives us the amount by which the sum will increase if we take the element in A instead of that in B at the same index.

So we just find the n greatest elements in the C array,  that will give us the index of the n elements we have to take from A and the other n elements will be taken from B.

Here if we use the sort function we end up with time complexity of O(nlog(n)), so we cannot use sort.

We instead use partial sort which sorts the array such that any element preceding k will be smaller than the element at k, and any element succeeding k will be greater than the element at k. This can be done using the partitioning technique of the quicksort method, but in this case, the worst-case takes O(n^2) time. To reduce this, we can use the median of medians technique to find a suitable pivot such that we only need work on a ratio of the array each time and this will ensure that we get worst-case O(n).

</p>

### Pseudo Codes:
##### Algo1
<p>
    
    Make an array C such as.
    C[i] = (A[i] - B[i] , i )
    Sort C WRT the diffrence 
    Then the first n elements are taken from B referencing through C[i][1] and the next n elements are taken from A.
</p>

##### Algo2
<p>

    partialSort(arr, l, r, k)
        n = r - l + 1
        if k > 0 and k <= n
            pos = randomPartition(arr, l, r)
            #Partitions the array about a randomly chosen pivot
            if pos-l == k-1
                return
            if pos-l > k-1
                return partialSort(arr, l, pos-1, k)
            else
                return partialSort(arr, pos+1, r, k-pos+l-1)

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
            if pos-l == k-1     
                return
            if pos-l > k-1      
                return partialSort(arr, l, pos-1, k)
            else    
                return partialSort(arr, pos+1, r, k-pos+l-1)


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
algo2 - O(n) Average , O(n^2) Worst-case 
<br>
algo3 - O(n) Worst-case
<br>
Median of medians is a recursive algorithm, which has a time complexity of

    n + n/5 + n/25 + ...... 1 = n (1 + 1/5 + 1/25 + ....  ) = 5n/4 = O(n)

Partition is a linear algorithm. It compares each element of the array to the pivot and partitions the array which takes O(n) time.

<br>
Partial sort is a recursive algorithm. By using median of medians algorithm, we can eliminate atleast a fraction of the orignal array (Here r > 1)

    n + n/r + n/r^2 + ...... 1 = n( 1 + 1/r + 1/r^2 + .... ) = n/(1-1/r) = O(n)
</p>

#### Proof Of Correctness:
<p>
Let us say that the answer is some half-set and given that sum(ans) is maximum.
<br>
Now if we subtract a constant from every half-set we still have sum(ans) as maximum.<br>
Let us take the constant to be sum(B)<br>
So the maximum sum is given by, sum(ans) - sum(B) == sum(ans[i] - B[i]).<br>
This in turn is sum(n0's + nC[i])<br>
So we need to find the n greatest C[i].
</p>

### Data-structures used:
Array/List(Python). 

### Notable Defects / Side Effects: 
One defect that we have encountered is that, if more than one solution exists, our answer will depend on the initial arrangement of the input array.

### How to run the code:
Run main.py using python3.6 (or above). It outputs a tuple which states if the answer given by algo3 is equal to answer by algo1 and if the sum of both the answer is same or not. The makeTestCases.py file is to generate random test cases and answers using algo1 which takes O(nlog(n)) time. The testcase.txt file stores the test cases as a bunch of 4 lines containing n, A, B, answer respectively.

### Sources referred:
https://www.youtube.com/watch?v=fcf56RTbkHc&feature=youtu.be for median of medians.<br>
Referred class notes for Quick Sort.
### Contributions:
##### Utkarsh Agarwal(IMT2018082): Proof of correctness, documentation, test cases and implementation of codes, Time Complexity calculation.
##### Neetha Reddy(IMT2018050): Pseudo codes and documentation
