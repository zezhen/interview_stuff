'''
https://leetcode.com/problems/sentence-screen-fitting/description/

Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 <= rows, cols <= 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
'''

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        wordLen = len(sentence)
        # dp[i] = (length, j, round) means start from word i, the max length of
        # sequence can fit the screen by word j (inclusive)
        # round means how many round it already went through
        dp = [(0,0,0)] * (wordLen)

        for i in xrange(wordLen):
            if len(sentence[i]) > cols: return 0

            acc, j, rd = -1, i - 1, 0
            if i > 0:
                acc, j, rd = dp[i-1]
                acc -= len(sentence[i-1]) + 1
            
            while acc + len(sentence[(j+1) % wordLen]) + 1 <= cols:
                j = (j + 1) % wordLen
                if j == wordLen - 1: rd += 1
                
                acc += len(sentence[j]) + 1
            
            dp[i] = (acc, j, rd)
        
        i, count = 0, 0
        for r in xrange(rows):
            _, j, rd = dp[i]
            count += rd
            i = (j + 1) % wordLen
        
        return count

            
s = Solution()
assert s.wordsTyping(rows = 2, cols = 8, sentence = ["hello", "world"]) == 1
assert s.wordsTyping(rows = 3, cols = 6, sentence = ["a", "bcd", "e"]) == 2
assert s.wordsTyping(rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]) == 1
assert s.wordsTyping(rows = 4, cols = 4, sentence = ["I", "had", "apple", "pie"]) == 0

assert s.wordsTyping(rows = 3, cols = 6, sentence = ["1", "12345", "2", "12345", "3"]) == 0
assert s.wordsTyping(rows = 5, cols = 6, sentence = ["1", "12345", "2", "12345", "3"]) == 1
assert s.wordsTyping(rows = 8, cols = 6, sentence = ["1", "12345", "2", "12345", "3"]) == 1
assert s.wordsTyping(rows = 9, cols = 6, sentence = ["1", "12345", "2", "12345", "3"]) == 2

s.wordsTyping(rows = 10, cols = 7, sentence = ["1", "1", "1"]) == 10

# import random
# def randWord(length):
# 	return 
# sentence = ["".join(['a']*random.randint(1,100)) for _ in xrange(10)]
# print sentence


