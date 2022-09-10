'''
https://leetcode.com/problems/card-flipping-game
https://leetcode.com/articles/card-flipping-game
On a table are N cards, with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card. 

If the number X on the back of the chosen card is not on the front of any card, then this number X is good.

What is the smallest number that is good?  If no number is good, output 0.

Here, fronts[i] and backs[i] represent the number on the front and back of card i. 

A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

Example:


Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.

 

Note:


	1 <= fronts.length == backs.length <= 1000.
	1 <= fronts[i] <= 2000.
	1 <= backs[i] <= 2000.

'''
class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        
        nums = set(fronts + backs)
        exclude = set()
        for i in xrange(len(fronts)):
            if fronts[i] == backs[i]:
                exclude.add(fronts[i])
        
        # print nums
        # print exclude
        res = nums - exclude
        return min(res) if res else 0
        

s = Solution()
print s.flipgame([1,2,4,4,7], [1,3,4,1,3]) == 2
print s.flipgame([1,2,4], [1,2,4]) == 0
print s.flipgame([2], [1]) == 1
print s.flipgame([1,2,3,4,5], [3,4,5,6,7]) == 1
















