'''
https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.

'''



class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        '''
        solution: greedy+backtracking

        s[i] + s[i+1] = s[i+2], s[0] and s[1] determine the whole fibonacci sequence

        s[0] start from one-digit number, increase s[1] from one-digit to multiple until find first valid s[1] and s[2], 
        then go on until reach the end, return ans. if fail then increase s[0] to two-digits number and repeat above steps.

        max length of s[0] is n/3, => O(n^2)

        submit but failed at case "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
        python can break it down into [539834657,21,539834678,539834699,1079669377,1619504076,2699173453,4318677529,7017850982,11336528511]
        as python automatically use long when 32bit number overflow.
        '''
        def search(i, a, b, ans):
            if i == len(S): return True
            if a.startswith('0') and len(a) > 1 \
                or b.startswith('0') and len(b) > 1: return False
            
            c = str(int(a) + int(b))
            # print i, a, b, c, S[i:], S[i:].startswith(c), i+len(c)
            if S[i:].startswith(c) and search(i+len(c), b, c, ans):
                ans.append(int(c))
                return True
            return False

        if len(S) < 3: return []

        ans = []
        for i in xrange(1,len(S)/2+1):
            for j in xrange(i+1, len(S)):
                a = S[:i]
                b = S[i:j]
                # print a, b
                if search(j, a, b, ans):
                    ans.append(int(b))
                    ans.append(int(a))
                    ans.reverse()
                    return ans

        return []


s = Solution()
assert s.splitIntoFibonacci("") == []
assert s.splitIntoFibonacci("12") == []
assert s.splitIntoFibonacci("123") == [1,2,3]
assert s.splitIntoFibonacci("0123") == []
assert s.splitIntoFibonacci("0000") == [0,0,0,0]
assert s.splitIntoFibonacci("17522") == [17,5,22]
assert s.splitIntoFibonacci("1752177") == [175,2,177]
assert s.splitIntoFibonacci("175555555501755555555") == [1755555555,0,1755555555]
assert s.splitIntoFibonacci("123456579") == [123,456,579]
assert s.splitIntoFibonacci("11235813") == [1,1,2,3,5,8,13]
assert s.splitIntoFibonacci("112358130") == []
assert s.splitIntoFibonacci("1101111") == [11, 0, 11, 11]

import random
for i in xrange(100):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    S = [a, b]
    for j in xrange(random.randint(1,10)):
        S.append(S[-1] + S[-2])
    res = s.splitIntoFibonacci("".join(map(str, S)))
    assert len(res) > 0

