'''
https://leetcode.com/problems/minimum-factorization
https://leetcode.com/articles/minimum-factorization

Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.

If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

Example 1
Input:

48 
Output:
68
Example 2
Input:

15
Output:
35
'''

class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a < 10: return a

        ans = []
        for i in xrange(9, 1, -1):
            while a % i == 0:
                a //= i
                ans.append(i)

        if a != 1: return 0
        return int(''.join(map(str, reversed(ans))))

s = Solution()
print s.smallestFactorization(15)