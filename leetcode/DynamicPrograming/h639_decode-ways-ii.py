'''

https://leetcode.com/problems/decode-ways-ii/description/

A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.

'''

''' ======

greedy + backtracking, notice the coding range is [1-26]

'''

class Solution(object):
    '''
    my solution pass, but can make it efficient by compiling if condition into dict, e.g.
        single = collections.defaultdict(int, {'*': 9})
        double = collections.defaultdict(int, {'**': 15, '1*': 9, '2*': 6})
    and dp is not necessary, but prev(dp[i-1]) and prevprev (dp[i-2])
    '''
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0 or s[0] == '0': return 0
        
        mod = 10**9 + 7

        dp = [0] * len(s)
        dp[0] = 1 if s[0] != '*' else 9
        for i in xrange(1, len(s)):
            if s[i] == '*':
                dp[i] = (dp[i-1] * 9) % mod
            elif s[i] != '0': 
                dp[i] = dp[i-1]
 
            if i > 0:
                base = dp[i-2] if i > 1 else 1
                if s[i-1] == '*':
                    dp[i] += (15 if s[i] == '*' else 2 if int(s[i]) <= 6 else 1) * base
                elif int(s[i-1]) == 1:
                    dp[i] += (9 if s[i] == '*' else 1) * base
                elif int(s[i-1]) == 2:
                    dp[i] += (6 if s[i] == '*' else 1 if int(s[i]) <= 6 else 0) * base
                dp[i] %= mod

            if dp[i] == 0: return 0
        # print dp
        return dp[-1]
        
s = Solution()
assert s.numDecodings('1') == 1
assert s.numDecodings('12') == 2
assert s.numDecodings('226') == 3
assert s.numDecodings('0226') == 0
assert s.numDecodings('2026') == 2
assert s.numDecodings('31026') == 2


assert s.numDecodings('*') == 9
assert s.numDecodings('1*') == 18
assert s.numDecodings('*0') == 2
assert s.numDecodings('*00') == 0
assert s.numDecodings('3*') == 9
assert s.numDecodings('1*') == 18
assert s.numDecodings('**') == 96
assert s.numDecodings('2**02*6') == 510
assert s.numDecodings('1*72*') == 285

# import random
# code = "".join(map(str, [random.randint(0,26) for _ in xrange(10)]))
# print code
# code = "19131125198232321118742368911254241912798132110511192116251685162626227142216211219263121951312201161015625171315416251632017713821101491217714101182121151932101719124"
# print s.numDecodings(code)

# print s.numDecodings('*'* 10**5)