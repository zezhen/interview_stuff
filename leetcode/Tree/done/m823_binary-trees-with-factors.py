'''
https://leetcode.com/problems/binary-trees-with-factors
https://leetcode.com/articles/binary-trees-with-factors
Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node's value should be equal to the product of the values of it's children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:


Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:


Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

 

Note:


	1 <= A.length <= 1000.
	2 <= A[i] <= 10 ^ 9.

'''
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # [2, 4, 5, 8, 10]
        # 2 -> 1 (2 itself)
        # 4 -> 2 (2*2 and 4 itself)
        # 5 -> 1 (5 itself)
        # 8 -> 5 (2*1*2+1, 2*4=8, two orders, thus 2*1*2, and 8 itself)
        # 10 -> 3 (1*1*2+1, 2*5=10, two orders, thus 1*1*2, and 10 itself)
        A.sort()
        amap = dict(map(lambda t: (t[1],t[0]), enumerate(A)))
        
        mod = 10**9 + 7

        trees = [1] * len(A)
        for i in xrange(len(A)):
            for j in xrange(i):
                p, q = A[i], A[j]
                if p % q == 0 and p / q in amap:
                    trees[i] += (trees[j] * trees[amap[p / q]]) % mod
        
        return sum(trees) % mod
        

s = Solution()
print s.numFactoredBinaryTrees([2,4]) == 3
print s.numFactoredBinaryTrees([2,4,8]) == 8
print s.numFactoredBinaryTrees([2,4,5,10]) == 7
print s.numFactoredBinaryTrees([2,4,5,8,10]) == 12