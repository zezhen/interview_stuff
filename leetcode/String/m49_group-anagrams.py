'''
https://leetcode.com/problems/group-anagrams
https://leetcode.com/articles/group-anagrams
Given an array of strings, group anagrams together.

Example:


Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:


	All inputs will be in lowercase.
	The order of your output does not matter.

'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        _dict = {}
        
        for str in strs:
            key = ''.join(sorted(str))
            if key not in _dict:
                _dict[key] = []
            
            _dict[key].append(str)
        
        return _dict.values()