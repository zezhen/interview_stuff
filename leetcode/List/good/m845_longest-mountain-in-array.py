'''
https://leetcode.com/problems/longest-mountain-in-array/description/

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
'''

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # if two pass, we can keep scan up[i] by i and down[i] start from u
        # then max(up[i]+down[i]+1) will be the answer
        # if one pass and O(1) space, then reset up and down when not meet conditions.

        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down: res = max(res, up + down + 1)
        return res



s = Solution()
# assert s.longestMountain([1]) == 0
# assert s.longestMountain([1,2]) == 0
# assert s.longestMountain([2,1]) == 0

# assert s.longestMountain([1,2,3,4,5]) == 0
# assert s.longestMountain([1,1,1,1,2,3,4,5]) == 0
# assert s.longestMountain([5,4,3,2,1]) == 0
# assert s.longestMountain([5,4,3,2,1,1,1,1]) == 0
# assert s.longestMountain([1,1,1,1,1]) == 0
# assert s.longestMountain([5,4,3,2,1,2,3,4,5]) == 0

# assert s.longestMountain([1,1,1,2,3,4,5,4,3,2,1,1,1]) == 9
# assert s.longestMountain([4,5,4,3,2,3,2,2,1]) == 5
# assert s.longestMountain([4,5,4,3,2,7,6,5,4,2,2,1]) == 6
# assert s.longestMountain([4,4,5,7,3,2,3,2,1]) == 5

# assert s.longestMountain([0,1,2,3,4,5,4,3,2,1,0]) == 11
assert s.longestMountain([2,3,3,2,0,2]) == 0

# import random 
# A = [random.randint(0, 10000) for _ in xrange(10000)]
# print s.longestMountain(A)

