'''
https://leetcode.com/problems/sort-characters-by-frequency
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.



Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.



Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''
import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # hashmap to keep char -> count
        # order by count and print chars

        # python: collections.Counter can make it in two line
        return ''.join(map(lambda t: t[0]*t[1], collections.Counter(s).most_common()))

s = Solution()
print s.frequencySort('tree') 
print s.frequencySort('cccaaa') 
print s.frequencySort('Aabb') 