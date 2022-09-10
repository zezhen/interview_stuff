'''
https://leetcode.com/problems/arithmetic-slices
https://leetcode.com/articles/arithmetic-slices
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic. 1, 1, 2, 5, 7 


A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
    A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A. 


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
'''

class Solution(object):
    # the solution is correct, gap array is not necessary. 
    # counter * (counter - 1) can be done by add
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2: return 0
        
        total, gap = 0, A[1] - A[0]
        l = 0
        for r in xrange(1, len(A)-1):
            if A[r+1] - A[r] != gap:
                total += (r - l) * (r - l - 1) / 2 if r - l >= 2 else 0
                gap = A[r+1] - A[r]
                l = r
        else:
            r = r + 1 if A[r+1] - A[r] == gap else r
            total += (r - l) * (r - l - 1) / 2 if r - l >= 2 else 0

        return total

    def numberOfArithmeticSlices1(self, A):
        if len(A) <= 2: return 0
        
        gap = [ A[i+1] - A[i] for i in range(len(A) - 1) ]
        total = 0
        
        previous, counter = gap[0], 1
        for i in range(len(gap) - 1):
            if gap[i+1] == previous:
                counter += 1
            else:
                if counter >= 2:
                    total += counter * (counter - 1) / 2
                counter = 1
                previous = gap[i+1]
        
        if counter >= 2:
            total += counter * (counter - 1) / 2
        
        return total

s = Solution()

# nums = [70, 98, 71, 44, 15, 19, 47, 50, 94, 38]
# print s.numberOfArithmeticSlices(nums), s.numberOfArithmeticSlices1(nums)

import random

for i in xrange(1000):
    nums = [random.randint(0,100) for _ in xrange(100)]
    if not (s.numberOfArithmeticSlices(nums) == s.numberOfArithmeticSlices1(nums)):
        print nums
        break




