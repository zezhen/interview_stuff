'''
https://leetcode.com/problems/backspace-string-compare/description/

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

'''
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i, j = len(S) - 1, len(T) - 1

        while i >= 0 and j >= 0:

            i = self.search_next_valid(S, i)
            j = self.search_next_valid(T, j)
            # print i, j, S[i], T[j]
            if (i >= 0) ^ (j >= 0) or i >= 0 and S[i] != T[j]: return False

            i -= 1
            j -= 1
        
        i = self.search_next_valid(S, i)
        j = self.search_next_valid(T, j)
        
        if i >= 0 or j >= 0: return False

        return True

    def search_next_valid(self, S, i):
        del_i = 0    
        while i >= 0:
            if S[i] == '#':
                del_i += 1
            elif del_i > 0:
                del_i -= 1
            else:
                return i
            i -= 1

        return i

s = Solution()
assert s.backspaceCompare("ca##", "") == True
assert s.backspaceCompare("a#b", "b") == True
assert s.backspaceCompare("##ab#c", "ad#c") == True
assert s.backspaceCompare("ab##", "c#d#") == True
assert s.backspaceCompare("a##c", "#a#c") == True

assert s.backspaceCompare("bxj##tw", "bxo#j##tw") == True
assert s.backspaceCompare("bxj##tw", "bxj###tw") == False
assert s.backspaceCompare("ca#b", "b") == False
assert s.backspaceCompare("##aca##", "") == False