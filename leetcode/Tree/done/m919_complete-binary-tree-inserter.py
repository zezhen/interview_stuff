'''
https://leetcode.com/problems/complete-binary-tree-inserter
https://leetcode.com/articles/complete-binary-tree-inserter
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:


	CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
	CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
	CBTInserter.get_root() will return the head node of the tree.






 

Example 1:


Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]



Example 2:


Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]



 

Note:


	The initial given tree is complete and contains between 1 and 1000 nodes.
	CBTInserter.insert is called at most 10000 times per test case.
	Every value of a given or inserted node is between 0 and 5000.
 

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # support root is not null
        self.array = deque([root])
        i = 0
        while i < len(self.array):
            node = self.array[i]
            if node.left: self.array.append(node.left)
            if node.right: self.array.append(node.right)
            i += 1

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        self.array.append(node)
        i = len(self.array)
        parent = self.array[i // 2 - 1]
        if i % 2 == 0:
            parent.left = node
        else:
            parent.right = node
        return parent.val


    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.array[0]


import sys
sys.path.append('../')
import helper

root = TreeNode(1)
obj = CBTInserter(root)
assert helper.tree2array(obj.get_root()) == [1]
assert obj.insert(2) == 1
assert helper.tree2array(obj.get_root()) == [1,2]
assert obj.insert(3) == 1
assert helper.tree2array(obj.get_root()) == [1,2,3]
assert obj.insert(4) == 2
assert helper.tree2array(obj.get_root()) == [1,2,3,4]
assert obj.insert(5) == 2
assert obj.insert(6) == 3
assert obj.insert(7) == 3
assert obj.insert(8) == 4
assert obj.insert(9) == 4
assert obj.insert(10) == 5
assert obj.insert(11) == 5
assert obj.insert(12) == 6
assert obj.insert(13) == 6
assert obj.insert(14) == 7
assert obj.insert(15) == 7
assert helper.tree2array(obj.get_root()) == range(1,16)


root = helper.array2tree([1,2,3,4,5,6])
obj = CBTInserter(root)
assert helper.tree2array(obj.get_root()) == [1,2,3,4,5,6]
assert obj.insert(7) == 3
assert obj.insert(8) == 4
assert helper.tree2array(obj.get_root()) == [1,2,3,4,5,6,7,8]

