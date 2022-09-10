'''
https://leetcode.com/problems/count-the-repetitions/description/

Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, "abc" can be obtained from "abdbec" based on our definition, but it can not be obtained from "acbbe".

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 <= n1 <= 106 and 1 <= n2 <= 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2

'''
class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        # 6095ms
        
        if len(set(s2) - set(s1)) > 0 or len(s2) * n2 > len(s1) * n1: return 0

        # tried to match s1 and s2 only, then infer M based on t1 vs t2 and n1 vs n2
        # but there are always some corner cases cannot make it works, use ugely way
        def match(s1, n1, s2, n2, early_stop):
            i = j = 0
            t1 = t2 = 0
            while t1 < n1:
                i = s1.find(s2[j], i)
                if i == -1:
                    t1 += 1
                    # match in a pattern or reach count limit
                    if early_stop and j == 0 or t1 == n1:
                        break
                    i = s1.find(s2[j])

                i += 1
                j += 1
                if j == len(s2):
                    t2 += 1
                    j = 0

            return t1, t2

        t1, t2 = match(s1, n1, s2, n2, True)

        # print t1, t2, n1, n2
        if t1 < n1:
            x2 = n1 / t1 * t2 / n2
            x1 = x2 * n2 * t1 / t2
            # print x1, x2, n1 - x1
            # print match(s1, n1 - x1, s2, n2, False)
            return x2 + match(s1, n1 - x1, s2, n2, False)[1] / n2
        else:
            return t2 / n2

    def getMaxRepetitions_fastest(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        # amazing, use seen and rep to keep the repeating index and length
        # rather than my always checking x = 0 and y = 0, this is much faster.
        # 20ms

        s1, s2 = list(s1), list(s2)
        l1, l2 = len(s1), len(s2)
        seen, rep = {}, []
        index1, index2, count1 = 0, 0, 0
        while count1 < n1:
            if s1[index1] == s2[index2]:
                index2 += 1
                if index2 == l2:
                    if index1 in seen:
                        rep.append(index1 + count1 * l1)
                        break
                    seen[index1] = len(rep)
                    rep.append(index1 + count1 * l1)
                    index2 = 0
            index1 += 1
            if index1 == l1:
                index1 = 0
                count1 += 1
        if count1 == n1: #### break and do not find any repeat
            return len(rep) / n2
        
        before_index = seen[index1]
        before_len = rep[before_index] + 1
        repeat_len = rep[-1] - rep[before_index]
        count2 = len(rep) - before_index - 1
        total_len = l1 * n1
        
        before_count = before_index + 1
        repeat_count_s1, after_len = divmod(total_len - before_len, repeat_len)
        repeat_count = repeat_count_s1 * count2
        after_count = 0
      
        for index in range(before_index + 1, len(rep)-1):
            if rep[index] - rep[before_index] >   after_len:
                break
            after_count += 1
            
        return (before_count + repeat_count + after_count) / n2

s = Solution()
print s.getMaxRepetitions('abc', 4, 'ab', 2) == 2
print s.getMaxRepetitions('abc', 4, 'ab', 3) == 1
print s.getMaxRepetitions('ab', 4, 'abba', 2) == 0
print s.getMaxRepetitions('ab', 8, 'abba', 2) == 1
print s.getMaxRepetitions('a', 8, 'aa', 2) == 2
print s.getMaxRepetitions('abc', 16, 'aabbcc', 2) == 2
print s.getMaxRepetitions('abc', 16, 'da', 2) == 0
print s.getMaxRepetitions('abc', 16, 'a', 2) == 8
print s.getMaxRepetitions('aaa', 3, 'aa', 1) == 4
print s.getMaxRepetitions('aaaaa', 3, 'aaa', 1) == 5
print s.getMaxRepetitions("bacaba", 3, "abacab", 1) == 2

print s.getMaxRepetitions("phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenzkycxf", 1000000, "xtlsgypsfadpooefxzbcoejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknly", 100)