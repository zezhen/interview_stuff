'''
https://leetcode.com/problems/number-of-matching-subsequences
https://leetcode.com/articles/number-of-matching-subsequences
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.


Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".


Note:


	All words in words and S will only consists of lowercase letters.
	The length of S will be in the range of [1, 50000].
	The length of words will be in the range of [1, 5000].
	The length of words[i] will be in the range of [1, 50].

'''
import bisect

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        self.ans = 0
        # solution 1:
        # search sequence S in trie tree
        # loc_seq keep all letters' location, in increasing order lists
        # loc = self.loc_seq(S)
        # trie = self.create_trie(words)
        # self.search_trie(trie, S, loc, 0)
        
        # there is no necessary to use trie
        ans = 0
        letter_loc = self.loc_seq(S)
        for word in words:
            anchor = 0
            for c in word:
                if c not in letter_loc: break
                
                locs = letter_loc[c]
                j = bisect.bisect_left(locs, anchor)
                if j >= len(locs): break
                
                anchor = locs[j] + 1
                
            else:
                ans += 1
                
        return ans
    
    def search_trie(self, node, S, seqloc, i):
        if 'count' in node: self.ans += node['count']

        if i >= len(S): return

        children = node.keys()
        for child in children:
            if child not in seqloc: continue
            
            # find the nearest position
            locs = seqloc[child]
            j = bisect.bisect_left(locs, i)
            if j >= len(locs): continue
                
            sindex = locs[j]
            self.search_trie(node[child], S, seqloc, sindex+1)
    
    def loc_seq(self, S):
        loc = {}
        for i, c in enumerate(S):
            if c not in loc: loc[c] = []
            loc[c].append(i)
        return loc
    
    def create_trie(self, words):
        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t: t[c] = {}
                t = t[c]
            if 'count' not in t: t['count'] = 0
            t['count'] += 1
            
        return trie