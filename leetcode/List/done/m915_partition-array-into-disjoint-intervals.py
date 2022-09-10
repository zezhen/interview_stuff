'''
https://leetcode.com/problems/partition-array-into-disjoint-intervals
https://leetcode.com/articles/parition-array-into-disjoint-intervals
Given an array A, partition it into two (contiguous) subarrays left and right so that:


	Every element in left is less than or equal to every element in right.
	left and right are non-empty.
	left has the smallest possible size.


Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:


Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]



Example 2:


Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


 


Note:


	2 <= A.length <= 30000
	0 <= A[i] <= 10^6
	It is guaranteed there is at least one way to partition A as described.



 

'''
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        left_max = [0 for i in range(len(A) - 1)] # left_max[i] = max(0...i)
        right_min = [0 for i in range(len(A) - 1)] # right_min[i] = min(i+1, n-1)
        
        left_max[0] = A[0]
        for i in xrange(1, len(A)-1):
            left_max[i] = max(left_max[i-1], A[i])
        
        right_min[-1] = A[-1]
        for i in xrange(len(A) - 3, -1, -1):
            right_min[i] = min(right_min[i+1], A[i+1])
        
        for i in xrange(len(left_max)):
            if left_max[i] <= right_min[i]:
                return i+1