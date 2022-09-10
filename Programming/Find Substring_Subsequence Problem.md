# Find Substring/Subsequence Problem
----

1.  字符串包含: 字符串B中所有字母是否都在字符串A里？
    1.  hashtable or bitmap 如果字母都是ascii码字符
    2.  如果没有重复字符, 可以将每个字符对应到一个素数上, 然后取乘积 (不考虑溢出), 看Pa % Pb 是否为0

*   扩展
    *   兄弟字符串: 如果两个字符串字符一样,但顺序不一样, 给定字典, 如何快速查找某个字符串的兄弟字符串
        *   一次性, 构建给定字符串的hashtable, 然后依次扫描字典, 每个字典字符串对照hashtable
        *   cache字典: 构建trie树, 对每个字符串排序, 加入trie树中, 即可找到所有, 也可以runtime查找

3.  [Find Substring Template](https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems)
    1.  [longest-substring-with-at-most-two-distinct-characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/): 给定字符串S, 找出最长的只包含两种字符的连续子串
        1.  import collections
        2.  def lengthOfLongestSubstringTwoDistinct(self, s):
        3.      counter = collections.Counter()                 # ch -> number map
        4.  
        5.      ans = current\_start = length = 0                
        6.  
        7.      for current\_end, ch in enumerate(s, 1):
        8.          if counter\[ch\] == 0:                        # check counter condition
        9.              length += 1
        10.          counter\[ch\] += 1                            # update counter for all ch
        11.  
        12.          while length > 2:                           # check whether substring is valid
        13.              if counter\[s\[current\_start\]\] == 1:      # try to make substring valid again
        14.                  length -= 1
        15.              counter\[s\[current\_start\]\] -= 1          
        16.              current\_start += 1
        17.          ans = max(ans, current\_end - current\_start) # update answer
        18.      return ans
    2.  [longest-substring-with-at-least-k-repeating-characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/)
    3.  [longest-substring-with-at-most-k-distinct-characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/): 如#1, 将2换成k
    4.  [subarrays-with-k-different-integers](https://leetcode.com/problems/subarrays-with-k-different-integers/description/): 包含k个integer的subarray个数
        1.  def subarraysWithKDistinct(self, A, K):
        2.      def compress(A):
        3.          count, B, c = \[\], \[\], 1
        4.          for i in xrange(1, len(A)):
        5.              if A\[i\] == A\[i-1\]:
        6.                  c += 1
        7.              else:
        8.                  B.append(A\[i-1\])
        9.                  count.append(c)
        10.                  c = 1
        11.          B.append(A\[-1\])
        12.          count.append(c)
        13.          return B, count
        
        15.      A, freq = compress(A)   # compress A, e.g. \[1,1,1,1,1\] to \[1\], \[5\]
        
        17.      counter = collections.defaultdict(int)
        18.      ans = l = size = 0
        
        20.      for i,num in enumerate(A):
        21.          if counter\[num\] == 0:
        22.              size += 1
        23.          counter\[num\] += 1
        
        25.          while size > K:     # make it valid again
        26.              counter\[A\[l\]\] -= 1
        27.              if counter\[A\[l\]\] == 0:
        28.                  size -= 1
        29.              l += 1
        
        31.          if size == K:
        32.              # when i == l, means K == 1
        33.              ans += freq\[l\] \* freq\[i\] if i != l else (freq\[i\]+1)\* freq\[i\]/2
        34.              t = l                   \# try to count valid subarray ending at position i
        35.              while counter\[A\[t\]\] > 1:
        36.                  counter\[A\[t\]\] -= 1
        37.                  t += 1
        38.                  ans += freq\[t\] \* freq\[i\] if i != t else (freq\[i\]+1)\* freq\[i\]/2
        39.              while t > l:    # reset
        40.                  counter\[A\[t-1\]\] += 1
        41.                  t -= 1
        42.      return ans
    5.  [minimum-window-substring](https://leetcode.com/problems/minimum-window-substring/description/): 给定字符串S和子串T, 检查S的包含T的最短连续子串
        1.  def minWindow(self, s, t):
        2.      counter = collections.Counter(t)
        3.  
        4.      remain\_missing = len(t)
        5.      start\_pos, end\_pos = 0, float('inf')
        6.      current\_start = 0
        
        8.      for current\_end, ch in enumerate(s, 1):
        9.          if counter\[ch\] > 0:
        10.              remain\_missing -= 1
        11.          counter\[ch\] -= 1
        
        13.          if remain\_missing == 0:
        14.              while counter\[s\[current\_start\]\] < 0:
        15.                      counter\[s\[current\_start\]\] += 1
        16.                      current\_start += 1
        17.  
        18.              if current\_end - current\_start < end\_pos - start\_pos:
        19.                  start\_pos, end\_pos = current\_start, current\_end
        20.  
        21.              remain\_missing += 1
        22.              counter\[s\[current\_start\]\] += 1
        23.              current\_start += 1
        24.      return s\[start\_pos:end\_pos\] if end\_pos != float('inf') else “”
    6.  [longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/): 找出字符串s中最长的不包含重复字符的子串
    7.  [permutation-in-string](https://leetcode.com/problems/permutation-in-string/description/): 给定字符串s和t, 查看s是否包含t的字符串排列. 
        1.  def checkInclusion(self, s1, s2):
        2.      A = \[ord(x) - ord('a') for x in s1\]
        3.      B = \[ord(x) - ord('a') for x in s2\]
        
        5.      target = \[0\] \* 26
        6.      for x in A:
        7.          target\[x\] += 1
        
        9.      window = \[0\] \* 26
        10.      for i, x in enumerate(B):
        11.          window\[x\] += 1
        12.          if i >= len(A):
        13.              window\[B\[i - len(A)\]\] -= 1
        14.          if window == target:
        15.              return True
        16.      return False
    8.  [unique-letter-string](https://leetcode.com/problems/unique-letter-string/description/): 
    9.  [substring-with-concatenation-of-all-words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/)
    10.  
4.  Subsequence
    1.  [is-subsequence](https://leetcode.com/problems/is-subsequence/description/): 给定s和t, 求t是否是s的非连续子串
    2.  [split-array-into-consecutive-subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences)
    3.  [sum-of-subsequence-widths](https://leetcode.com/problems/sum-of-subsequence-widths/description/)
    4.  [number-of-matching-subsequences](https://leetcode.com/problems/number-of-matching-subsequences)
    5.  [longest-consecutive-sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)
    6.  [stamping-the-sequence](https://leetcode.com/problems/stamping-the-sequence/description/)
5.  Others
    1.  [longest-word-in-dictionary-through-deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/): 给定字符串s以及字符串数组words, 求words中最长的s的subsequence. 上题的扩展.
    2.  [word-subsets](https://leetcode.com/problems/word-subsets/description/): 给定两个字符列表A和B, 找出A中的字符串, 使得B中所有字符串都被起包含








----

- Date: 2018-12-26
- Tags: #Interview/Programing 



