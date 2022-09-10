'''
https://leetcode.com/problems/replace-words
https://leetcode.com/articles/replace-words

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.




Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.



You need to output the sentence after the replacement.



Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"




Note:

The input will only have lower-case letters.
 1 <= dict words number <= 1000 
 1 <= sentence words number <= 1000  
 1 <= root length <= 100 
 1 <= sentence words length <= 1000 

'''

class Solution(object):
    def replaceWords(self, _dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = self.create_trie(_dict)
        ans = map(lambda w: self.search_trie(trie, w), sentence.split(' '))
        return ' '.join(ans)
        
    def search_trie(self, trie, word):
        t = trie
        for c in word:
            if c not in t: return word
            t = t[c]
            if 'word' in t: return t['word']
        return word
    
    def create_trie(self, words):
        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t: t[c] = {}
                t = t[c]
            t['word'] = word
        return trie