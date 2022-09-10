'''
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 <= P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k >= 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -2^31 and 2^31-1 and 0 <= N <= 1000. The output is guaranteed to be less than 2^31-1.


Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
'''
import collections, math
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2: return 0

        # the idea of my solution at beginning is close but I keep the sequence length to the cache[i][diff]
        # then compute the total count at last, which cannot solve the duplicated scenario.
        #
        # here keep the combination count in cache[i][diff], where cache[i] is the all combination ending at i
        # check j < i one by one, if diff match, then add how many combination endby (i, j), which is cache[i][diff]
        # new combination number of j will be c1 + c2 +1 for next elements to check, c1/c2 might be greater than 1 due to duplication
        # credit to https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/92822
        cache = [{} for _ in xrange(len(A))]
        ans = 0
        for j in xrange(len(A)):
            for i in xrange(j):
                diff = A[j] - A[i]
                c1 = cache[j][diff] if diff in cache[j] else 0
                c2 = cache[i][diff] if diff in cache[i] else 0
                ans += c2
                cache[j][diff] = c1 + c2 + 1

        return ans



s = Solution()
print s.numberOfArithmeticSlices([2, 2, 2, 2, 2]) == 16
print s.numberOfArithmeticSlices([2, 2, 2, 2, 2, 4, 6, 8]) == 27
print s.numberOfArithmeticSlices([2, 4, 6, 8, 10]) == 7
