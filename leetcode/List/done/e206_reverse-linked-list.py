'''
https://leetcode.com/problems/reverse-linked-list
https://leetcode.com/articles/reverse-linked-list
Reverse a singly linked list.

Example:


Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL


Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev , current = None,head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev