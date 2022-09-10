'''
https://leetcode.com/problems/repeated-dna-sequences
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:


Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]

'''
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counter = {}
        for i in range(len(s) - 9):
            subStr = s[i:i+10]
            counter[subStr] = (counter[subStr] if subStr in counter else 0) + 1
        ret = []
        
        for key, value in counter.iteritems():
            if value > 1:
                ret.append(key)
        return ret