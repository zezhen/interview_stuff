'''
https://leetcode.com/problems/strange-printer
https://leetcode.com/articles/strange-printer

There is a strange printer with the following two special requirements:


The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.





Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.


Example 1:

Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".



Example 2:

Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.



Hint: Length of the given string will not exceed 100.'''

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        credit to https://leetcode.com/problems/strange-printer/discuss/106810

        dp[i][j] stands for the minimal turns we need for string from index i to index j.
        dp[i][i] = 1: we need 1 turn to paint a single character.
        dp[i][i + 1] = 1 if s.chartAt(i) == s.charAt(i + 1)
        dp[i][i + 1] = 2 if s.chartAt(i) != s.charAt(i + 1)

        We can further divide the substring to two parts: start -> start+k and start+k+1 -> start+len. It is something as following:
        index |start  ...  start + k| |start + k + 1 ... start + len|
        char  |  a    ...       b   | |      c       ...      b     |

        As shown above, if we have s.charAt(start + k) == s.charAt(start + len), we can make it in one turn when we print this character (i.e. b here)
        This case we can reduce our turns to dp[start][start + k] + dp[start + k + 1][start + len] - 1
        ''' 
        if not s: return 0
        n = len(s)
        dp = [[n] * n for _ in xrange(n)]

        for i in xrange(n):
            dp[i][i] = 1
            if i < n - 1:
                dp[i][i+1] = 1 if s[i] == s[i+1] else 2

        for l in xrange(2, n):
            for i in xrange(n-l):
                j = i + l
                dp[i][j] = l + 1
                for k in xrange(l):
                    tmp = dp[i][i+k] + dp[i+k+1][j]
                    if s[i+k] == s[j]:
                        tmp -= 1
                    dp[i][j] = min(dp[i][j], tmp)

        return dp[0][n-1]


    def strangePrinter_mine_complicated_but_failed(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # try dp solution, dp[0][n-1] is the answer
        # subproblem: if we already know dp[i][j]
        # scenario 1:
        #    obviously if s[j+1] == s[j], then dp[i][j+1] = dp[i][j]
        # scenario 2:
        #   if s[i] == s[j+1], e.g. 'a'X, X is a substring, we're appending 'a'
        #   no matter how X is, when we draw first 'a', we can draw last 'a' in passing
        #   thus dp[i][j+1] = dp[i][j]
        # scenario 3:
        #   if s[j+1] not exist in s[i:j+1], dp[i][j+1] = dp[i][j] + 1
        # scenario 4:
        #   if s[j+1] exist in s[i:j+1], let's say s[k] == s[j+1], i<k<j, X'a'Y'a', X, Y is string
        # scenario 4.1
        #   if any chars in Y also existing in X, e.g. the 'bbaba', then it's not free to append
        # scenario 4.2
        #   otherwise like 'bbaca', it's free to append (suppose)

        n = len(s)
        dp = [[n] * n for _ in xrange(n)]

        for i in xrange(n):
            dp[i][i] = 1

        for k in xrange(1, n):
            for i in xrange(n-k):
                j = i + k
                
                # append s[j] to s[i:j-1]
                if s[j] == s[j-1] or s[j] == s[i]:  # scenario 1, 2
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                else:
                    substr = s[i:j]
                    x = substr.rfind(s[j])
                    if x == -1: # scenario 3
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
                    elif len(set(substr[x+1:]).intersection(set(substr[:x]))) == 0: 
                        dp[i][j] = min(dp[i][j], dp[i][j-1])
                    else:
                        while x != -1:
                            x = substr.rfind(s[j], 0, x)
                            if x != -1 and len(set(substr[x+1:]).intersection(set(substr[:x]))) == 0:
                                dp[i][j] = min(dp[i][j], dp[i:x]+dp[x:j-1])
                                break
                        else:
                            dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)

                # append front s[i] to s[i+1:j]
                if s[i] == s[i+1] or s[i] == s[j]:  # scenario 1, 2
                    dp[i][j] = min(dp[i][j], dp[i+1][j])
                else:
                    substr = s[i+1:j+1]
                    x = substr.find(s[i])
                    if x == -1:     # scenario 3
                        dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                    elif len(set(substr[:x]).intersection(set(substr[x+1:]))) == 0: # scenario 4.1
                        dp[i][j] = min(dp[i][j], dp[i+1][j])
                    else:
                        while x != -1:
                            x = substr.find(s[i], x+1)
                            if x != -1 and len(set(substr[:x]).intersection(set(substr[x+1:]))) == 0:
                                dp[i][j] = min(dp[i][j], dp[i+1:x+1]+dp[x+1:j])
                                break
                        else:
                            dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                        
                if i == 0 and j == n-1:
                    print dp[i][j], dp[i+1][j], dp[i][j-1]
                    
        # print dp
        return dp[0][n-1]


s = Solution()
# print s.strangePrinter('aaabbb') == 2
# print s.strangePrinter('aba') == 2
# print s.strangePrinter('cbbaba') == 4
# print s.strangePrinter('abccbaaaabbbccc') == 5
print s.strangePrinter('ghdjcjejkbbaddaehhccbhikjhgaaagbdiigdkhdkafddhjjajaicjecfjjihgebecdcggjkhhidikheihcjdggcbbageceagace')
print s.strangePrinter('ghdjcjejkbbaddaehhccbhikjhgaaagbdiigdkhd')



