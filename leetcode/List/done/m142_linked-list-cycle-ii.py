'''
https://leetcode.com/problems/linked-list-cycle-ii
https://leetcode.com/articles/linked-list-cycle-ii

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.



Note: Do not modify the linked list.


Follow up:
Can you solve it without using extra space?
'''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        initNode = ListNode(None)
        initNode.next = head
        slow, fast = initNode, initNode
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                while initNode != slow:
                    initNode, slow = initNode.next, slow.next
                return(slow)
            
        return(None)