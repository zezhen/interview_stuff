'''

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

'''
import collections
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
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

            while length > k:
                if counter[s[current_start]] == 1:
                    length -= 1

                counter[s[current_start]] -= 1
                current_start += 1
            ans = max(ans, current_end - current_start)

        return ans