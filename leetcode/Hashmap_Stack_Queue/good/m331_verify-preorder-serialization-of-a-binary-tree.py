'''
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.


     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #


For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:


Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example 2:


Input: "1,#"
Output: false


Example 3:


Input: "9,#,#,1"
Output: false
'''
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == '#':
            return True
        
        stack = []
        
        arr = preorder.split(',')
        _len = len(arr)
        i = 0
        while i < _len:
            c = arr[i]
            if c != '#':
                stack.append(0)
            elif len(stack) <= 0:
                return False
            else:
                while len(stack) > 0 and stack[-1] == 1:
                    stack.pop()
                if len(stack) > 0:
                    stack[-1] = 1
            i += 1
            if len(stack) == 0:
                break
        
        return len(stack) == 0 and i == _len