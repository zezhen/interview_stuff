'''
https://leetcode.com/problems/short-encoding-of-words
https://leetcode.com/articles/short-encoding-of-words
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:


Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].


 

Note:


	1 <= words.length <= 2000.
	1 <= words[i].length <= 7.
	Each word has only lowercase letters.

'''
class Solution(object):
def minimumLengthEncoding(self, words):
    """
    :type words: List[str]
    :rtype: int
    """
    if not words: return 0
    
    trie = {}
    for word in words:
        node = trie
        for c in word[::-1]:
            if c not in node: node[c] = {}
            node = node[c]
    
    leaves = []
    def leavesDepth(node, depth):
        if not node.keys():
            leaves.append(depth)
            return
        
        for k in node.keys():
            leavesDepth(node[k], depth+1)
    
    leavesDepth(trie, 0)
    return sum(leaves) + len(leaves)

s = Solution()
print s.minimumLengthEncoding([]) == 0
print s.minimumLengthEncoding(["time"]) == 5
print s.minimumLengthEncoding(["time", "me", "bell"]) == 10
print s.minimumLengthEncoding(["time", "me", "tame"]) == 10
print s.minimumLengthEncoding(["time", "me", "e"]) == 5
print s.minimumLengthEncoding(["time", "me", "timer"]) == 11