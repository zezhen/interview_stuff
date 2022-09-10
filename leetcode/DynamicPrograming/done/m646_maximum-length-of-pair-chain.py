'''
https://leetcode.com/problems/maximum-length-of-pair-chain
https://leetcode.com/articles/maximum-length-of-pair-chain

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.



Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion. 



Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.



Example 1:

Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]



Note:

The number of given pairs will be in the range [1, 1000].

'''

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        '''
        solution 1 is DP, but O(n^2) time complixity
        
        below solution is order the pairs by end time, s1<e1<e2, s2<e2
        (s1, e1) is ahead because e1<e2, it has more chance to generate longer chain.
        '''

        cur, res = float('-inf'), 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]: cur, res = p[1], res + 1
        return res