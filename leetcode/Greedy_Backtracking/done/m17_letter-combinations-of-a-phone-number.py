'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:


Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        self.map = [' ', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.ret = []
        self._combine(digits, 0, [])
        return self.ret
    
    def _combine(self, digits, i, queue):
        if i == len(digits):
            self.ret.append("".join(queue))
            return
        
        letters = self.map[int(digits[i])]
        for letter in letters:
            queue.append(letter)
            self._combine(digits, i+1, queue)
            queue.pop()
        
        