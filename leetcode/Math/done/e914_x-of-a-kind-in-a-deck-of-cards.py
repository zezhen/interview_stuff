'''
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards
https://leetcode.com/articles/x-of-a-kind-in-a-deck-of-cards
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:


	Each group has exactly X cards.
	All the cards in each group have the same integer.


 

Example 1:


Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]



Example 2:


Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.



Example 3:


Input: [1]
Output: false
Explanation: No possible partition.



Example 4:


Input: [1,1]
Output: true
Explanation: Possible partition [1,1]



Example 5:


Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]







Note:


	1 <= deck.length <= 10000
	0 <= deck[i] < 10000






 




'''
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        
        count = {}
        
        for d in deck:
            count[d] = (count[d] if d in count else 0) + 1
        
        _, divisor = count.popitem()
        if divisor == 1: return False
        
        for k,v in count.iteritems():
            if v == 1: return False
            if v % divisor == 0: continue
            else:
                divisor = self.gcd(divisor, v)
                if divisor == 1: 
                    return False
        return True
        
    def gcd(self, n, m):
        while m != 0:
            n, m = m, n % m
        return n
        