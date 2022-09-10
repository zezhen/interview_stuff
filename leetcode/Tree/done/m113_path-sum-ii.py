'''
https://leetcode.com/problems/path-sum-ii
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,


      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1


Return:


[
   [5,4,11,2],
   [5,8,4,5]
]

'''

# recursion(DFS) is most simple, but we can use stack to reach that,
# or use queue to make BFS

