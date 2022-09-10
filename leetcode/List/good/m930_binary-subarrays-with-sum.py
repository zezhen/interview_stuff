'''
https://leetcode.com/problems/binary-subarrays-with-sum/description/

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
 

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.

'''
from collections import Counter
class Solution(object):

    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        c = Counter({0: 1})
        psum = res = 0
        for i in A:
            psum += i
            res += c[psum - S]
            c[psum] += 1
        return res


s = Solution()
print s.numSubarraysWithSum([1,0,1,0,1], 2) == 4
print s.numSubarraysWithSum([1,0,1,0,1,1,0,1,0,1], 2) == 12


