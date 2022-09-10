'''
https://leetcode.com/problems/merge-k-sorted-lists/description/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import sys
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return []
        
        # can use min heap or loser tree
        # min heap is up to bottom, each time parent need to compare with two children
        # loser tree is bottom to up, each time child need to compare with parent only once.
        MIN, MAX = - sys.maxint, sys.maxint
        K = len(lists)

        value, tree = [], [K] * K

        def get_next(i):
            if lists[i] == None:
                return MAX

            res = lists[i].val
            lists[i] = lists[i].next
            return res

        def adjust_tree(s):
            t = (s + K) / 2
            while t > 0:
                if value[s] > value[tree[t]]:
                    tree[t], s = s, tree[t]
                t /= 2
            tree[0] = s
        
        for i in xrange(K):
            value.append(get_next(i))
        value.append(MIN)   # index K contains the minimum value
        
        ans = []
        for i in range(K)[::-1]:
            adjust_tree(i)

        while value[tree[0]] != MAX:
            ans.append(value[tree[0]])
            value[tree[0]] = get_next(tree[0])
            adjust_tree(tree[0])

        return ans

def array2list(array):
    if not array or len(array) <= 0: return None
    head = ListNode(array[0])
    p = head
    for i in range(1, len(array)):
        p.next = ListNode(array[i])
        p = p.next
    return head

s = Solution()
print s.mergeKLists([array2list([1,2,3]),array2list([4,5,6]),array2list([7,8,9])])
