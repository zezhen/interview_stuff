'''
https://leetcode.com/problems/encode-string-with-shortest-length

Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:

k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
 

Example 1:

Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
 

Example 2:

Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
 

Example 3:

Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
 

Example 4:

Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
 

Example 5:

Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".

'''

class Solution(object):
    def encode_dfs(self, s, memo={}):
        """
        :type s: str
        :rtype: str
        """
        # Either don't encode s at all, or encode it as one part k[...] or encode it as multiple parts (in which case we can somewhere split it into two subproblems). Whatever is shortest.
        if not s: return ''
        if s not in memo:
            n = len(s)
            i = (s + s).find(s, 1)
            one = '%d[%s]' % (n / i, self.encode(s[:i])) if i < n else s
            multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in xrange(1, n)]
            memo[s] = min([s, one] + multi, key=len)
        return memo[s]

    def encode(self, s):
        # DP solution, credit to https://leetcode.com/problems/encode-string-with-shortest-length/discuss/95599
        # dp[i][j] = string from index i to index j in encoded form.
        # dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]) or if we can find some pattern in string from i to j which will result in more less length.
        if not s: return ''

        dp = [[''] * len(s) for _ in xrange(len(s))]

        for l in xrange(len(s)):
            for i in xrange(len(s)-l):
                j = i + l
                substr = dp[i][j] = s[i:j+1]
                if j - i >= 4:
                    # Loop for trying all results that we get after dividing the strings into 2 and combine the   results of 2 substrings
                    for k in xrange(i, j):
                        if len(dp[i][k]) + len(dp[k+1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k+1][j]
                    
                    # Loop for checking if string can itself found some pattern in it which could be repeated.
                    for k in xrange(len(substr)):
                        repeatStr = substr[:k+1]
                        if repeatStr and len(substr) % len(repeatStr) == 0 and len(substr.replace(repeatStr,'')) == 0:
                            ss = "%d[%s]" % (len(substr) / len(repeatStr), dp[i][i+k])
                            if len(ss) < len(dp[i][j]):
                                dp[i][j] = ss

        return dp[0][-1]

    def encode_mine_not_work_for_all(self, s):
        if not s: return ''

        def to_string(chars, counts):
            res = []
            for i, ch in enumerate(chars):
                s = '%d[%s]' % (counts[i], ch)
                if len(s) > len(ch) * counts[i]:
                    res.append(ch * counts[i])
                else:
                    res.append(s)

            return ''.join(res)
        
        memo = {}
        def encode0(chars, counts):
            # print chars, counts
            ans = to_string(chars, counts)
            for k in range(2, len(chars) / 2 + 1):
                print k, len(chars), chars, counts
                compress = []
                times = []
                i = 0
                while i < len(chars) - k:
                    if chars[i:i+k] == chars[i+k:i+2*k] and counts[i] >= counts[i+k] and counts[i+1:i+k] == counts[i+k+1:i+2*k]:
                        j = i + k
                        while chars[j:j+k] == chars[j+k:j+2*k] and counts[j:j+k] == counts[j+k:j+2*k]:
                            j += k
                        freq = (j - i) / k + 1
                        if counts[i] > counts[i+k]:
                            compress.append(chars[i])
                            times.append(counts[i] - counts[i+k])
                        embed = to_string(chars[i+k:i+2*k], counts[i+k:i+2*k])
                        compress.append(embed)
                        times.append(freq)
                        i = j + k
                    else:
                        compress.append(chars[i])
                        times.append(counts[i])
                        i += 1

                if i < len(chars):
                    compress.extend(chars[i:])
                    times.extend(counts[i:])

                if len(compress) < len(chars):
                    res = encode0(compress, times)
                else:
                    res = to_string(compress, times)
                
                print k, len(chars), res
                if not ans or len(res) < len(ans):
                    ans = res
                    

            return ans

        chars = [s[0]]
        counts = [1]
        for i in xrange(1, len(s)):
            if s[i] == chars[-1]:
                counts[-1] += 1
            else:
                chars.append(s[i])
                counts.append(1)

        return encode0(chars, counts)

s = Solution()
print s.encode("") == ''
print s.encode("a") == 'a'
print s.encode("aaa") == 'aaa'
print s.encode("aaaa") == 'aaaa'
print s.encode("aaaaabb") == '5[a]bb'
print s.encode("aabcaabcd") == '2[aabc]d'
print s.encode("aaaaabbbbaaaabbbb") == 'a2[aaaabbbb]'
print s.encode("abcabcabcaaaaa") == '3[abc]5[a]'
print s.encode("abbbabbbcabbbabbbc") == "2[2[abbb]c]"
print s.encode("aaaaaaaaaabbbaaaaabbb") == "5[a]2[5[a]bbb]"
print s.encode("abcdefabcdefffffffffffffedcbafedcba") == '2[abcdef]11[f]2[fedcba]'