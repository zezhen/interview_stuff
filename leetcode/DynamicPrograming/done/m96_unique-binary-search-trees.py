'''
https://leetcode.com/problems/unique-binary-search-trees
https://leetcode.com/articles/unique-binary-search-trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:


Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = [0]*(n+1)
        counter[0] = 1
        
        for i in range(1, n+1):
            _sum = 0
            for j in range(0, i):
                _sum += counter[j] * counter[i-1-j]
            counter[i] = _sum
        
        return counter[n]