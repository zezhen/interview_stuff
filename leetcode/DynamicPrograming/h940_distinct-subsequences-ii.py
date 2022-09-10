'''
https://leetcode.com/problems/distinct-subsequences-ii
https://leetcode.com/articles/distinct-subsequences-ii
Given a string S, count the number of distinct, non-empty subsequences of S .

Since the result may be large, return the answer modulo 10^9 + 7.

 

Example 1:


Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".



Example 2:


Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".



Example 3:


Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".




 

 

Note:


	S contains only lowercase letters.
	1 <= S.length <= 2000



 


 

'''
class Solution(object):
    '''
    credit to https://leetcode.com/problems/distinct-subsequences-ii/discuss/192017

    Explanation
    Init an array endswith[26]
    endswith[i] to count how many sub sequence that ends with ith character.

    Now we have N = sum(endswith) different sub sequence,
    add a new character c to each of them,
    then we have N different sub sequence that ends with c.

    With this idea, we loop on the whole string S,
    and we update end[c] = sum(end) + 1 for each character.

    We need to plus one here, because "c" itself is also a sub sequence.

    '''
    def distinctSubseqII(self, S):
        end = [0] * 26
        for c in S:
            end[ord(c) - ord('a')] = sum(end) + 1
            print end
        return sum(end) % (10**9 + 7)


s = Solution()

print s.distinctSubseqII('aaa')
print s.distinctSubseqII('abc')


# def rand_char(start=0, end=25, count=1000):
#     import random
#     a = ord('a')
#     return [chr(a+random.randint(start,end)) for _ in xrange(count)]

# print s.distinctSubseqII(rand_char(count=100))