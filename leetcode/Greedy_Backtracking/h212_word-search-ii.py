'''
https://leetcode.com/problems/word-search-ii
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:


Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]


Note:
You may assume that all inputs are consist of lowercase letters a-z.'''

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # similar to word-search but this time there are multiple words
        # so use trie to speed the search

        trie = self.create_trie(words)
        starts = self.identify_start(board, trie)
        
        visited = [[False for _ in xrange(len(board[0]))] for _ in xrange(len(board))]
        ans = []
        for pos in starts:
            res = self.search_next(pos, board, visited)
            ans.extend(res)
        
        return list(set(ans))
        
        
    def identify_start(self, board, trie):
        starts, chars = [], trie.keys()
        for r in xrange(len(board)):
            for c  in xrange(len(board[0])):
                if board[r][c] in chars:
                    starts.append((r, c, trie[board[r][c]]))
        return starts
    
    def search_next(self, pos, board, visited):
        ans = []
        r, c, node = pos
        visited[r][c] = True
        chars = node.keys()
        
        if 'word' in node: ans.append(node['word'])
        
        if r > 0 and not visited[r-1][c] and board[r-1][c] in chars:
            res = self.search_next((r-1, c, node[board[r-1][c]]), board, visited)
            ans.extend(res)
        if r < len(board) -1 and not visited[r+1][c] and board[r+1][c] in chars:
            res = self.search_next((r+1, c, node[board[r+1][c]]), board, visited)
            ans.extend(res)
        if c > 0 and not visited[r][c-1] and board[r][c-1] in chars:
            res = self.search_next((r, c-1, node[board[r][c-1]]), board, visited)
            ans.extend(res)
        if c < len(board[0]) -1 and not visited[r][c+1] and board[r][c+1]  in chars:
            res = self.search_next((r, c+1, node[board[r][c+1]]), board, visited)
            ans.extend(res)

        visited[r][c] = False
        return ans
        
    
    def create_trie(self, words):
        trie = {}
        
        for word in words:
            t =  trie
            for c in word:
                if c not in t: t[c] = {}
                t = t[c]
            t['word'] = word
        
        return trie