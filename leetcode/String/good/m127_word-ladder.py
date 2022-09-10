'''
https://leetcode.com/problems/word-ladder/description/

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import deque

class Solution(object):
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        trie = self.create_trie(wordList)
        endIndex = self.search(trie, endWord)
        if len(endIndex) == 0: return 0
        endIndex = endIndex[0]
        
        candidate = deque([-1])
        dist = {-1:1}
        
        while len(candidate) > 0:
            size = len(candidate)
            while size > 0:
                pos = candidate.popleft()
                d = dist[pos]
                word = wordList[pos] if pos >= 0 else beginWord
                for i in range(len(word)):
                    res = self.search(trie, word, skip_level=i)
                    for index in res:
                        if index not in dist: 
                            dist[index] = d + 1
                            candidate.append(index)
                        if index == endIndex:
                            return dist[index]
                size -= 1
    
        return 0
                
    def search(self, trie, word, skip_level=-1):
        queue = deque([trie])
        for i, c in enumerate(word):
            size = len(queue)
            while size > 0:
                t = queue.popleft()
                if i == skip_level:
                    for n in t.values():
                        queue.append(n)
                elif c in t:
                    queue.append(t[c])
                size -= 1
        return map(lambda t:t['i'], queue)
    
    def create_trie(self, wordList):
        trie = {}
        for i,word in enumerate(wordList):
            t = trie
            for c in word:
                if c not in t: t[c] = {}
                t = t[c]
            t['i'] = i
        return trie