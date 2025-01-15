You are given an array and you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in geometric progression for a given common ratio r and i < j < k.

**Example**
 
arr = [1,4,16,64]

There are [1,4,16] and [4,16,64] at indices (0,1,2) and (1,2,3). Return 2.

**Function Description**

Complete the countTriplets function in the editor below.

countTriplets has the following parameter(s):

* int arr[n]: an array of integers
* int r: the common ratio

**Returns**

* int: the number of triplets

**Input Format**

The first line contains two space-separated integers n and r, the size of arr and the common ratio.

The next line contains  space-seperated integers arr[i].