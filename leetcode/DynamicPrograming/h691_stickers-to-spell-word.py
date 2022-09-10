'''
https://leetcode.com/problems/stickers-to-spell-word
https://leetcode.com/articles/stickers-to-spell-word

We are given N different types of stickers.  Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target?  If the task is impossible, return -1.


Example 1:
Input:
["with", "example", "science"], "thehat"


Output:
3


Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.


Example 2:
Input:
["notice", "possible"], "basicbasic"


Output:
-1


Explanation:
We can't form the target "basicbasic" from cutting letters from the given stickers.


Note:
stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual.  It is expected that a 50 sticker test case can be solved within 35ms on average.
'''
from collections import Counter
import heapq
import copy
class Solution(object):
    # I use counter to do the subtraction
    # but counter to tuple takes a lot of time
    # the fastest solution use string and replace directly
    # runtime 4808ms vs 100ms
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        ss = set()
        for st in stickers:
            ss.update(st)
        ts = set(target)
        if len(ts - ss) > 0:
            return -1

        
        scounter = []
        for st in stickers:
            sc = Counter()
            for ch in st:
                if ch in ts: sc.update({ch:1})
            if sc:
                scounter.append(sc)
        
        self.minSticker = 0
        tcounter = Counter(target)
        heap = []
        seen = set()
        for sc in scounter:
            target = tcounter - sc
            t = tuple(target.elements())
            if t not in seen: 
                heapq.heappush(heap, (1, sum(target.values()), target))
                seen.add(t)

        while heap:
            count, elem, target = heapq.heappop(heap)
            if not target:
                return count
            for sc in scounter:
                new_target = target - sc
                t = tuple(new_target.elements())
                if t not in seen:
                    heapq.heappush(heap, (count + 1, sum(new_target.values()), new_target))
                    seen.add(t)

    def minStickers_fastest(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        stickers.sort(key = lambda x:len(x),reverse = True)
        temp = []
        for s in stickers:
            temp1 = {}
            for i in s:
                temp1[i] = temp1.get(i,0)+1
            temp.append(temp1)
        stickers = temp
        memo = {'':0}
        def dfs(target):
            if target in memo:
                return memo[target]
            res = float('inf')
            for stick in stickers:
                if target[0] not in stick:
                    continue
                targetnew = target
                for s in stick:
                    targetnew = targetnew.replace(s,'',stick[s])
                if targetnew=='':
                    res = 1
                    break
                elif targetnew!=target:
                    res = min(res,1+dfs(targetnew))
            memo[target] = res
            return res
        res = dfs(target)
        if res==float('inf'):
            return -1
        return res

s = Solution()
print s.minStickers(["with", "example", "science"], "thehat") == 3
print s.minStickers(["notice", "possible"], "basicbasic") == -1

print s.minStickers(["notice", "possible"], "bsicbsic")
