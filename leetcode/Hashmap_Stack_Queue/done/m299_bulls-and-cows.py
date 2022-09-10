'''
https://leetcode.com/problems/bulls-and-cows
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:


Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

Example 2:


Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.'''
class Solution(object):

    # revision: build a map of digit -> count for secret
    # scan guess: if guess[i] == secret[i]: A++, dict[guess[i]]-=1 , else if dict[guess[i]] > 0: count --

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = cows = 0
        s_counter = [0 for i in range(10)]
        g_counter = [0 for i in range(10)]
        
        l = len(secret)
        for i in range(l):
            s = secret[i]
            g = guess[i]
            if s == g:
                bulls += 1
            else:
                s_counter[int(s)] += 1
                g_counter[int(g)] += 1
        for i in range(10):
            cows += min(s_counter[i], g_counter[i])
        return "%dA%dB" % (bulls, cows)