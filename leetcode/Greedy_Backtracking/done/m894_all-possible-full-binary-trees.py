'''
https://leetcode.com/problems/all-possible-full-binary-trees
https://leetcode.com/articles/all-possible-full-binary-trees
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:


Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:



 

Note:


	1 <= N <= 20

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    cache = {}
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0: return []

        if N in self.cache: return self.cache[N]
        if N == 1: 
            self.cache[1] = [TreeNode(0)]
            return self.cache[1]

        ans = []
        for i in xrange(2, N, 2):
            print i, N
            left_nodes = self.allPossibleFBT(i-1)
            right_nodes = self.allPossibleFBT(N-i)
            for ln in left_nodes:
                for rn in right_nodes:
                    root = TreeNode(0)
                    root.left = ln
                    root.right = rn
                    ans.append(root)
        self.cache[N] = ans
        return ans

import sys
sys.path.append('../')
import helper

s = Solution()
ans = s.allPossibleFBT(5)
for tree in ans:
    print helper.tree2array(tree)