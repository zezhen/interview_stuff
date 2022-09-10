'''
https://leetcode.com/problems/hand-of-straights
https://leetcode.com/articles/hand-of-straights
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 




Example 1:


Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:


Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

 

Note:


	1 <= hand.length <= 10000
	0 <= hand[i] <= 10^9
	1 <= W <= hand.length

'''
import heapq
from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        
        if len(hand) % W != 0: return False
        queue = Counter(hand).most_common()
        waitList = []
        heapq.heapify(queue)
        print queue
        
        for x in xrange(len(hand) / W):
            if not queue: return False
            start, count = heapq.heappop(queue)
            if count > 1:
                waitList.append((start, count-1))
            for i in xrange(1, W):
                if not queue: return False
                value, count = heapq.heappop(queue)
                if value != start + i: return False
                if count > 1:
                    waitList.append((value, count-1))
            while waitList:
                heapq.heappush(queue, waitList.pop())
            
        return True
        
        

s = Solution()
# print s.isNStraightHand([1,2,3,6,2,3,4,7,8], 3) == True
# print s.isNStraightHand([1,2,3,6,2,3,4,7,8], 4) == False
# print s.isNStraightHand([1,2,2,3,3,3,4,4,5], 3) == True
# print s.isNStraightHand([1,2,2,3,3,4,40,41,42], 3) == True
# print s.isNStraightHand([1,2,2,3,3,4,40,41,43], 3) == False

print s.isNStraightHand([1,1,2,2,3,3], 2) == False