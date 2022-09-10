'''
https://leetcode.com/problems/construct-binary-tree-from-string/description/

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:

Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:

There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        digits = set(map(str, range(10)))
        node, _ = self._str2tree(s, 0, digits)
        return node
        
    def _str2tree(self, s, i, digits):
        if i >= len(s): return (None, i)
        while s[i] == '(': i += 1

        j = i
        while j < len(s) and (s[j] == '-' or s[j] in digits):
            j += 1

        root = TreeNode(int(s[i:j]))
        
        if j < len(s) and s[j] == '(':
            node, j = self._str2tree(s, j+1, digits)
            root.left = node
            if j < len(s) and s[j] == '(':
                node, j = self._str2tree(s, j+1, digits)
                root.right = node

        if j < len(s) and s[j] == ')': 
            return (root, j+1)

        return (root, j+1)

def preorder(node):
    ans, queue = [], []
    while len(queue) > 0 or node:
        while node:
            ans.append(node.val)
            queue.append(node)
            node = node.left

        if len(queue) > 0:
            node = queue.pop()
            node = node.right
    # print ans
    return ans


s = Solution()

assert preorder(s.str2tree("")) == []
assert preorder(s.str2tree("4")) == [4]
assert preorder(s.str2tree("(4)")) == [4]
assert preorder(s.str2tree("4(2(3)(1))(6(5))")) == [4,2,3,1,6,5]
assert preorder(s.str2tree("4(2(3(6(5)))(1))")) == [4,2,3,6,5,1]
