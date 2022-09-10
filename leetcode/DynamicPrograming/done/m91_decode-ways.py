'''
https://leetcode.com/problems/decode-ways/description/

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


''' =======

greedy + backtracking, notice the coding range is [1-26]


'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0 or s[0] == '0': return 0
        
        dp = [0] * len(s)

        dp[0] = 1
        for i in xrange(1, len(s)):
            if s[i] != '0':
                dp[i] = dp[i-1]

            if i > 0 and (int(s[i-1]) == 1 or int(s[i-1]) == 2 and int(s[i]) <= 6):
                dp[i] += dp[i-2] if i > 1 else 1
            
            if dp[i] == 0: return 0

        return dp[-1]
        
s = Solution()
assert s.numDecodings('1') == 1
assert s.numDecodings('12') == 2
assert s.numDecodings('226') == 3
assert s.numDecodings('0226') == 0
assert s.numDecodings('2026') == 2
assert s.numDecodings('31026') == 2

import random
code = "".join(map(str, [random.randint(0,26) for _ in xrange(10)]))
print code
# code = "19131125198232321118742368911254241912798132110511192116251685162626227142216211219263121951312201161015625171315416251632017713821101491217714101182121151932101719124"

print s.numDecodings(code)





