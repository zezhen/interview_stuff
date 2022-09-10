'''
https://leetcode.com/problems/word-search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:


board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        # find all start char and BFS with visited flag
        start_pos = self.identify_start(board, word)
        if len(start_pos) == 0: return False
        print start_pos
        
        visited = [[False for _ in xrange(len(board[0]))] for _ in xrange(len(board))]
        for pos in start_pos:
            if self.search_next(pos, board, word, 1, visited): return True
            
        return False
        
    def identify_start(self, board, word):
        if len(word) <= 0: return []
        pos = []
        first_char = word[0]
        for r in xrange(len(board)):
            for c  in xrange(len(board[0])):
                if board[r][c] == first_char:
                    pos.append((r,c))    
        return pos
    
    def search_next(self, pos, board, word, i, visited):
        if i >= len(word): return True
        
        r, c = pos
        char = word[i]
        
        print pos, char, i, len(word), visited[r][c+1], board[r][c+1]
        
        if r > 0 and visited[r-1][c] and board[r-1][c] == char:
            visited[r-1][c] = True
            if self.search_next((r-1, c), board, word, i+1, visited):
                return True
            visited[r-1][c] = False
        elif r < len(board) -1 and visited[r+1][c] and board[r+1][c] == char:
            visited[r+1][c] = True
            if self.search_next((r+1, c), board, word, i+1, visited):
                return True
            visited[r+1][c] = False
        elif c > 0 and visited[r][c-1] and board[r][c-1] == char:
            visited[r][c-1] = True
            if self.search_next((r, c-1), board, word, i+1, visited):
                return True
            visited[r][c-1] = False
        elif c < len(board[0]) -1 and visited[r][c+1] and board[r][c+1] == char:
            visited[r][c+1] = True
            if self.search_next((r, c+1), board, word, i+1, visited):
                return True
            visited[r][c+1] = False
        
        return False
        