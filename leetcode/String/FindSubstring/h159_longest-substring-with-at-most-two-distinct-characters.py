'''
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

'''
import collections
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter()

        ans = 0
        current_start = 0
        length = 0

        for current_end, ch in enumerate(s, 1):
            if counter[ch] == 0:
                length += 1
            counter[ch] += 1

            while length > 2:
                if counter[s[current_start]] == 1:
                    length -= 1

                counter[s[current_start]] -= 1
                current_start += 1
            ans = max(ans, current_end - current_start)

        return ans
