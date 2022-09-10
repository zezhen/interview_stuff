'''
https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
'''
import collections
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """

        # refer to https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP
        count = [0] * 26
        _ord = {}
        for i in range(26):
        	_ord[chr(i + ord('a'))] = i

        acc = 0
        for j in xrange(len(p)):
        	if j > 0 and (ord(p[j]) - ord(p[j-1]) == 1 \
        		or p[j] == 'a' and p[j-1] == 'z'):
        		acc += 1
        	else:
        		acc = 1
        	count[_ord[p[j]]] = max(count[_ord[p[j]]], acc)

        return sum(count)

s = Solution()
assert s.findSubstringInWraproundString('cac') == 2