'''
https://leetcode.com/problems/add-bold-tag-in-string/description/

Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:

The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
'''

'''
option 1
for each word in dict, search index in s, get the impact range (i,j) 
    -> O(k(m+n)), k = len(dict), n = len(s), m is average word length in dict
sort and merge ranges, then apply tag to s.
	-> O(klogk)

option 2
create trie tree from dict, each tree node has a pointer to parent
	-> O(km) time, O(km) space
loop word in dict, scan from tail and get the deepest node ?

option 3
suffix tree


'''

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """


