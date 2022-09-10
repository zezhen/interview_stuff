'''
https://leetcode.com/problems/add-two-numbers
https://leetcode.com/articles/add-two-numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:


Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        n1 = l1
        n2 = l2
        n3, carry = self.add(n1.val, n2.val, 0)
        l3 = n3
        
        while n1.next and n2.next:
            node, carry = self.add(n1.next.val, n2.next.val, carry)
            n3.next = node
            n3 = node
            
            n1 = n1.next
            n2 = n2.next
        
        re = n1.next if n1.next else n2.next
        while re and carry > 0:
            node, carry = self.add(re.val, 0, carry)
            n3.next = node
            n3 = node
            re = re.next
        
        if not re and carry > 0:
            node = ListNode(carry)
            n3.next = node
        if re and carry == 0:
            n3.next = re
        
        return l3
            
        
    def add(self, x, y, carry):
        node = ListNode((x + y + carry) % 10)
        carry = (x + y + carry) / 10
        return (node, carry) 
            