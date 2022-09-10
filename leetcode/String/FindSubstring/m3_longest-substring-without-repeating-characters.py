'''
https://leetcode.com/problems/longest-substring-without-repeating-characters
https://leetcode.com/articles/longest-substring-without-repeating-characters
Given a string, find the length of the longest substring without repeating characters.


Example 1:


Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 



Example 2:


Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.



Example 3:


Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.




'''
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        
        _dict = {}
        _max = 1
        start = 0
        for i, c in enumerate(s):
            if c not in _dict or _dict[c][-1] < start:
                _dict[c] = [i]
                _max = max(_max, i - start + 1)
            else:
                _max = max(_max, i - start)
                start = max(start, _dict[c][-1] + 1)
                _dict[c].append(i)
        return _max