# https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head: return head

        i, p1 = 1, head
        while p1.next and i < k:
            p1 = p1.next
            i += 1
        
        if not p1.next: # p1 reach the end, i is the length of list
            k = k % i
            if k == 0: return head

            i, p1 = 1, head
            while i < k:
                p1 = p1.next
                i += 1
        
        p2 = None
        while p1.next:
            p1 = p1.next
            p2 = p2.next if p2 else head
        p1.next = head
        head = p2.next
        p2.next = None

        # printlist(head)
        return head

def array2list(array):
    if not array or len(array) <= 0: return None

    head = ListNode(array[0])
    p = head
    for i in range(1, len(array)):
        p.next = ListNode(array[i])
        p = p.next
    return head

def list2array(head):
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array

def printlist(head):
    while head:
        print head.val,
        head = head.next
    print

arr = [1,2,3,4,5,6,7]
l = array2list(arr)
assert list2array(l) == arr

s = Solution()

assert list2array(s.rotateRight(array2list([]), 3)) == []
assert list2array(s.rotateRight(array2list([1]), 19)) == [1]

assert list2array(s.rotateRight(array2list(arr), 0)) == [1,2,3,4,5,6,7]
assert list2array(s.rotateRight(array2list(arr), 1)) == [7,1,2,3,4,5,6]
assert list2array(s.rotateRight(array2list(arr), 2)) == [6,7,1,2,3,4,5]
assert list2array(s.rotateRight(array2list(arr), 3)) == [5,6,7,1,2,3,4]
assert list2array(s.rotateRight(array2list(arr), 4)) == [4,5,6,7,1,2,3]
assert list2array(s.rotateRight(array2list(arr), 5)) == [3,4,5,6,7,1,2]
assert list2array(s.rotateRight(array2list(arr), 6)) == [2,3,4,5,6,7,1]
assert list2array(s.rotateRight(array2list(arr), 7)) == [1,2,3,4,5,6,7]
assert list2array(s.rotateRight(array2list(arr), 8)) == [7,1,2,3,4,5,6]
assert list2array(s.rotateRight(array2list(arr), 9)) == [6,7,1,2,3,4,5]
assert list2array(s.rotateRight(array2list(arr), 10)) == [5,6,7,1,2,3,4]
assert list2array(s.rotateRight(array2list(arr), 11)) == [4,5,6,7,1,2,3]
assert list2array(s.rotateRight(array2list(arr), 12)) == [3,4,5,6,7,1,2]
assert list2array(s.rotateRight(array2list(arr), 13)) == [2,3,4,5,6,7,1]
assert list2array(s.rotateRight(array2list(arr), 14)) == [1,2,3,4,5,6,7]
assert list2array(s.rotateRight(array2list(arr), 15)) == [7,1,2,3,4,5,6]