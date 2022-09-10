'''
https://leetcode.com/problems/decode-string

Given an encoded string, return it's decoded string.


The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.


You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].


Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

'''
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        
        def dfs(start):
            ans = []
            i = start
            while i < len(s):
                start = i

                # start with char
                while i < len(s) and s[i] in chars:
                    i += 1
                if i > start: ans.append(s[start:i])

                # check integer
                start = i
                while i < len(s) and s[i] in digits:
                    i += 1
                times = int(int(s[start:i])) if i > start else 0
                
                # nested dfs
                if i < len(s) and s[i] == '[':
                    i, res = dfs(i+1)
                    ans.append(res * times)

                # end and return
                if i >= len(s) or s[i] == ']':
                    return i+1, ''.join(ans)


        ans = []
        i = 0
        while i < len(s):
            i, res = dfs(i)
            ans.append(res)
            i += 1  # s[i] == ']'

        return ''.join(ans)

s = Solution()

print s.decodeString('') == ''
print s.decodeString('3[a]2[bc]') == 'aaabcbc'
print s.decodeString('3[a2[c]]') == 'accaccacc'
print s.decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef'
print s.decodeString('ab[a]2[bc]') == 'abbcbc'
print s.decodeString('abcd') == 'abcd'
print s.decodeString('a2[b]cd') == 'abbcd'
print s.decodeString('100[leetcode]') == 'leetcode'*100
print s.decodeString('3[a]2[b4[F]c]') == 'aaabFFFFcbFFFFc'
print s.decodeString('3[a]2[b4[F]2[c]a]') == 'aaabFFFFccabFFFFcca'