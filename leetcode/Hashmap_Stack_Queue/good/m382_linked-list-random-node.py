'''
https://leetcode.com/problems/linked-list-random-node
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?


Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import random
class Solution(object):

    # there are multiple solution for get one random number
    # 1. copy linked list numbers to a array, random select from array
    # 2. because linked list size is large, so scan list and get size n, random select number from [1,n], scan link again.
    # 3. reservior sampling. very good explanation in below link, good to sampling k numbers, this is k = 1 problem.
    #    https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        node = self.head
        ans = node.val
        i = 1
        while node.next:
            node = node.next
            if random.randint(i+1) == i:
                ans = node.val
            i += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()