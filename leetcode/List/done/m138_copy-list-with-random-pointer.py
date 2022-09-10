'''
https://leetcode.com/problems/copy-list-with-random-pointer
https://leetcode.com/articles/copy-list-with-random-pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.



Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    # use a map to keep random pointer works better, but O(n) space

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None

        # copy node and use next to connect original and new nodes
        p = head
        while p:
            q = RandomListNode(p.label)
            q.next = p.next
            p.next = q
            p = q.next

        p = head
        q = ans = head.next

        # set random pointers
        while p:
            if p.random:
                q.random = p.random.next
            p = q.next
            if p:
                q = p.next

        # reset next pointers
        p = head
        q = ans
        while p:
            p.next = q.next
            if q.next:
                q.next = q.next.next
            p = p.next
            q = q.next

        return ans

import random
def array2list(array):
    if not array or len(array) <= 0: return None

    listarray = map(lambda v: RandomListNode(v), array)
    for i in xrange(len(listarray)):
        node = listarray[i]
        if i < len(listarray)-1:
            node.next = listarray[i+1]

        j = random.randint(0,len(listarray)-1)
        node.random = listarray[j]

    return listarray[0]

def printlist(head):
    while head:
        print head.label, head.random.label if head.random else ''
        head = head.next

l = array2list(range(0))

printlist(l)

s = Solution()
ll = s.copyRandomList(l)
printlist(ll)