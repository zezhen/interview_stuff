'''
https://leetcode.com/problems/implement-magic-dictionary
https://leetcode.com/articles/implement-magic-dictionary

Implement a magic directory with buildDict, and search methods.



For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.



For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.


Example 1:

Input: buildDict(["hello", "leetcode"]) == Null
Input: search("hello") == False
Input: search("hhllo") == True
Input: search("hell") == False
Input: search("leetcoded") == False



Note:

You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

'''
from collections import deque
class MagicDictionary(object):

    
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def buildDict(self, _dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i,word in enumerate(_dict):
            t = self.trie
            for c in word:
                if c not in t: t[c] = {}
                t = t[c]
            t['word'] = word # add word in leaf node

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        queue = deque([(self.trie, 0)])
        for i, c in enumerate(word):
            size = len(queue)
            if size == 0: return False
            while size > 0:
                t, modified_time = queue.popleft()
                size -= 1
                
                if c in t:
                    queue.append((t[c], modified_time))
                if modified_time == 0:
                    for k,v in t.iteritems():
                        if k == 'word' or k == c: continue
                        queue.append((v, 1))
        
        return len(filter(lambda t: t[1] == 1 and 'word' in t[0], queue)) > 0


d = MagicDictionary()
d.buildDict(["hello", "leetcode"])

print d.search("hello") == False
print d.search("hhllo") == True
print d.search("hell") == False
print d.search("leetcoded") == False


d.buildDict(["hello","hallo","leetcode"])
print d.search("hello") == True
print d.search("hhllo") == True
print d.search("hell") == False
print d.search("leetcoded") == False

d.buildDict([])

print d.search("hallo") == False
print d.search("hell") == False
print d.search("leetcodd") == False
print d.search("ggdge") == False
print d.search("guggg") == False

d.buildDict([])
print d.search("hello") == False
print d.search("hallo") == False
print d.search("hell") == False
print d.search("leetcodd") == False
print d.search("ggdge") == False
print d.search("guggg") == False