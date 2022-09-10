'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal
https://leetcode.com/articles/construct-binary-tree-from-preorder-and-postorder-
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.


Example 1:


Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]




Note:


	1 <= pre.length == post.length <= 30
	pre[] and post[] are both permutations of 1, 2, ..., pre.length.
	It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.


'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        
        def construct(i, j, x, y):
            # if pre[i] != post[y]: return None
            if i == j and x == y: return TreeNode(pre[i])

            root = TreeNode(pre[i])

            # one child
            k = y - 1
            while k >= x and post[k] != pre[i+1]:
                k -= 1
            # if k < x: return None
            if k == y - 1: # only has right subtree
                root.right = construct(i+1, j, x, k)
            else:
                root.left = construct(i+1, i+1+k-x, x, k)
                root.right = construct(i+1+k-x+1, j, k+1, y-1)

            return root

        if len(pre) <= 0 or len(post) != len(pre): return None
        return construct(0, len(pre)-1, 0, len(post)-1)

import sys
sys.path.append('../')
import helper

s = Solution()

print helper.tree2array(s.constructFromPrePost([], [])) == []
print helper.tree2array(s.constructFromPrePost([1], [2,1])) == []
print helper.tree2array(s.constructFromPrePost([1], [1])) == [1]
print helper.tree2array(s.constructFromPrePost([1,2,3,4], [4,3,2,1])) == [1,None,2,None,3,None,4]
print helper.tree2array(s.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])) == [1,2,3,4,5,6,7]
print helper.tree2array(s.constructFromPrePost([1,2,4,5,3], [4,5,2,3,1])) == [1,2,3,4,5]
print helper.tree2array(s.constructFromPrePost([1,3,6,7], [6,7,3,1])) == [1,None,3,6,7]
print helper.tree2array(s.constructFromPrePost([1,2,4,5], [4,5,2,1])) == [1,None,2,4,5]

