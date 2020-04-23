# DAA_project

## Problem [Better Half](https://algomuse.net/archivecontest?contest_number=20)

### Utkarsh Agarwal(IMT2018082), Neetha Reddy(IMT2018050)


### Psudo Code Algo-1
<p>
C<sub>i</sub> = (A<sub>i</sub> - B<sub>i</sub> , i )
<br>
Sort C WRT the diffrence 
<br>
Then the first n elements are taken from B referencing through C[i][1] and the next n elements are taken from A.

</p>

### Proof
<p>

The diffrence array C tells us if we take the element in A instead of B at the same index, then by how much the sum  will increase.

So we just find the n greatest elements in the C array, that will give us the index of the elements we have to take from A and the rest will be taken from B. 

</p>