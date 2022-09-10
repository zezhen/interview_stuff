'''
https://leetcode.com/problems/palindrome-pairs/description/

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]

'''

# 1. for all words pair, check palindrome, O(k*N^2)
# 2. for each word w1, there are limit candidates that meet the palindrome cretian, so check all these candidates in input lists
#       worest case of this solution: for w1 aaaaaaaaaaa, it can have 2k candidates
# 3. based on option 2, create trie tree, search in trie tree for candidates.
        # create trie tree for the words but in reverse order
        # for every word search in the trie tree, there are two scenarios:
        # 1. long word s1 vs short word s2: s1 stop at index i, we need to check s[i+1:] is palindrome
        # 2. short word s2 vs long word s1: the search will stop at intermediate node in the trie, we need to know all words whose suffix is s2
        #    2.1. one way is continue search in trie tree until get all
        #    2.2. another way is keep all these words index in intermediate node.
import collections
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def isPalindrome(s):
            return s == s[::-1] # this works much faster!!
            for i in xrange(len(s)//2):
                if s[i] != s[-i-1]: return False
            else:
                return True

        trie = {'index':[]}
        for i, word in enumerate(words):
            node = trie
            node['index'].append(i)
            for c in reversed(word):
                if c not in node:
                    node[c] = {}
                    node[c]['index'] = []
                node = node[c]
                node['index'].append(i)
            node['word'] = i

        ans = []
        for i, word in enumerate(words):
            node = trie
            # in case there is "" in words
            if 'word' in node and isPalindrome(word) and i != node['word']:
                ans.append([i, node['word']])
            for j, c in enumerate(word):
                if c not in node: break
                node = node[c]
                # long word vs short word
                if 'word' in node and isPalindrome(word[j+1:]) and i != node['word']:
                    ans.append([i, node['word']])
            else:
                # short word vs long word
                for index in node['index']:
                    if index == i: continue
                    candidate = words[index]
                    if len(candidate) > len(word) and isPalindrome(candidate[0:len(candidate)-len(word)]):
                        ans.append([i, index])
        return ans

s = Solution()
print s.palindromePairs([]) == []
print s.palindromePairs(["a",""]) == [[0,1],[1,0]]
print s.palindromePairs(["abcd","dcba","lls","s","sssll"]) == [[0,1],[1,0],[2,4],[3,2]] 
print s.palindromePairs(["bat","tab","cat"]) == [[0,1],[1,0]]
print s.palindromePairs(["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","aaaaaaaaaaa","aaaaaaaaaaaa","aaaaaaaaaaaaa"]) == sorted([[1,0],[0,1],[2,0],[1,2],[2,1],[0,2],[3,0],[2,3],[3,1],[1,3],[3,2],[0,3],[4,0],[3,4],[4,1],[2,4],[4,2],[1,4],[4,3],[0,4],[5,0],[4,5],[5,1],[3,5],[5,2],[2,5],[5,3],[1,5],[5,4],[0,5],[6,0],[5,6],[6,1],[4,6],[6,2],[3,6],[6,3],[2,6],[6,4],[1,6],[6,5],[0,6],[7,0],[6,7],[7,1],[5,7],[7,2],[4,7],[7,3],[3,7],[7,4],[2,7],[7,5],[1,7],[7,6],[0,7],[8,0],[7,8],[8,1],[6,8],[8,2],[5,8],[8,3],[4,8],[8,4],[3,8],[8,5],[2,8],[8,6],[1,8],[8,7],[0,8],[9,0],[8,9],[9,1],[7,9],[9,2],[6,9],[9,3],[5,9],[9,4],[4,9],[9,5],[3,9],[9,6],[2,9],[9,7],[1,9],[9,8],[0,9],[10,0],[9,10],[10,1],[8,10],[10,2],[7,10],[10,3],[6,10],[10,4],[5,10],[10,5],[4,10],[10,6],[3,10],[10,7],[2,10],[10,8],[1,10],[10,9],[0,10],[11,0],[10,11],[11,1],[9,11],[11,2],[8,11],[11,3],[7,11],[11,4],[6,11],[11,5],[5,11],[11,6],[4,11],[11,7],[3,11],[11,8],[2,11],[11,9],[1,11],[11,10],[0,11],[12,0],[11,12],[12,1],[10,12],[12,2],[9,12],[12,3],[8,12],[12,4],[7,12],[12,5],[6,12],[12,6],[5,12],[12,7],[4,12],[12,8],[3,12],[12,9],[2,12],[12,10],[1,12],[12,11],[0,12]])
print s.palindromePairs(["a","abc","aba",""]) == sorted([[0,3],[3,0],[2,3],[3,2]])
