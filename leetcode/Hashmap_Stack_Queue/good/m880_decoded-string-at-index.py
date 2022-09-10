'''
https://leetcode.com/problems/decoded-string-at-index
https://leetcode.com/articles/decoded-string-at-index
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:


	If the character read is a letter, that letter is written onto the tape.
	If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.


Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

 


Example 1:


Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".



Example 2:


Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".



Example 3:


Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".


 

Note:


	2 <= S.length <= 100
	S will only contain lowercase letters and digits 2 through 9.
	S starts with a letter.
	1 <= K <= 10^9
	The decoded string is guaranteed to have less than 2^63 letters.




'''
class Solution(object):
    def decodeAtIndex(self, S, K):
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
        print i, N, K
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c) # repeated string
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1  # K is in lower position

    def decodeAtIndex1(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        chars = 'abcdefghijklmnopqrstuvwxyz'
        digits = '23456789'

        start, tap = 0, ''

        while start < len(S):
            # get chars
            i = start
            while i <len(S) and S[i] in chars:
                if i - start == K - 1: return S[i]
                i += 1
            tap += S[start:i]

            times = 1
            # check digit
            while i < len(S) and S[i] in digits:
                times *= int(S[i])
                if len(tap) * times >= K:
                    return tap[(K-1) % len(tap)]
                i += 1
            
            tap *= times
            start = i

        return tap[(K-1) % len(tap)]


s = Solution()


# assert s.decodeAtIndex('ha22', 5) == 'h'
# assert s.decodeAtIndex('a2345678999999999999999', 1) == 'a'
# assert s.decodeAtIndex('a2345678999999999999999', 100) == 'a'

# assert s.decodeAtIndex('leet2code3', 1) == 'l'
# assert s.decodeAtIndex('leet2code3', 4) == 't'
# assert s.decodeAtIndex('leet2code3', 5) == 'l'
# assert s.decodeAtIndex('leet2code3', 8) == 't'
# assert s.decodeAtIndex('leet2code3', 10) == 'o'
assert s.decodeAtIndex('leet2code3', 13) == 'l'

# assert s.decodeAtIndex('a', 3) == 'a'
# assert s.decodeAtIndex('leet2code2', 100) == 't'
# assert s.decodeAtIndex('leet2', 100) == 't'

# # a2b3c4 -> aabaabaabcaabaabaabcaabaabaabcaabaabaabc
# assert s.decodeAtIndex('a2b3c4d5e6f7g8h9', 9) == 'b'
# assert s.decodeAtIndex('a2b3c4d5e6f7g8h9', 10) == 'c'
# assert s.decodeAtIndex('a2b3c4d5e6f7g8h9', 38) == 'a'
# assert s.decodeAtIndex('a2b3c4d5e6f7g8h9', 40) == 'c'

# # exceed max memory limit
# print s.decodeAtIndex("yuele72uthzyoeut7oyku2yqmghy5luy9qguc28ukav7an6a2bvizhph35t86qicv4gyeo6av7gerovv5lnw47954bsv2xruaej", 123365626)


