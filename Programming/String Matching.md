# String Matching
----

1.  [regular-expression-matching](https://leetcode.com/problems/regular-expression-matching/description/)
    
    *   '.' Matches any single character.
    *   '\*' Matches zero or more of the preceding element.
    *   The matching should cover the entire input string (not partial).
    
    1.  def isMatch(self, s, p):
    2.      MAX = len(p)
    3.      \# compile pattern string
    4.      i, rules = 0, \[\]
    5.      min\_len = 0
    6.      while i < len(p):
    7.          c = p\[i\]
    8.          if i + 1 < len(p) and p\[i+1\] == '\*':
    9.              if not rules or rules\[-1\] != (c, 0):    # dedupe contiguous c\*
    10.                  rules.append((c, 0))
    11.              i += 1
    12.          else:
    13.              rules.append((c, 1))
    14.              min\_len += 1
    15.          i += 1
    16.  
    17.      if len(s) < min\_len: return False
    18.  
    19.      i, j, stack = 0, 0, \[\]
    20.      while min\_len > 0 or j < len(s):
    
    22.          if i < len(rules) and j < len(s) and (rules\[i\]\[0\] == '.' or rules\[i\]\[0\] == s\[j\]):
    23.              if rules\[i\]\[1\] == 1:
    24.                  i += 1
    25.                  min\_len -= 1
    26.              else:
    27.   # cp can match arbitrary times,
    28.   # backup the scenario that if cp stop match here
    29.                  if i < len(rules) - 1:
    30.                      stack.append((i+1, j, min\_len))  \# don't have to match now
    31.                      stack.append((i+1, j+1, min\_len)) \# match then move forward
    32.              j += 1
    33.          elif i < len(rules) and rules\[i\]\[1\] == 0:
    34.              i += 1
    35.          elif len(stack) > 0:
    36.              # restore another scenario
    37.              i, j, min\_len = stack.pop()
    38.          else:
    39.              return False
    40.      return True
    41.  
    42.  def isMatch\_dfs(self, s, p):
    43.      if not p: return not s
    44.      if len(p) == 1:
    45.          if len(s) != 1: return False
    46.          return s == p
    47.  
    48.      if s and (p\[0\] == '.' or p\[0\] == s\[0\]):
    49.          if p\[1\] == '\*':
    50.              return self.isMatch(s\[1:\], p) or self.isMatch(s, p\[2:\])
    51.          elif p\[1\] == '+':
    52.              return self.isMatch(s\[1:\], p\[2:\])
    53.          else:
    54.              return self.isMatch(s\[1:\], p\[1:\])
    55.      return p\[1\] == '\*' and self.isMatch(s, p\[2:\])
    
2.  [wildcard-matching](https://leetcode.com/problems/wildcard-matching/description/)
    1.  similar to #1, one diff is '?' Matches any single character.
3.  旋转匹配: 判断字符串s能够从另一个字符串t旋转得到, 比如s = abcd, t = bcda
    1.  判断t是否是s+s的子串
4.  [repeated-substring-pattern](https://leetcode.com/problems/repeated-substring-pattern): 判断字符串s能够由子串重复多次得到, 比如s = abcabcabc
    1.  return (s + s)\[1:-1\].find(s) != -1
5.  [word-pattern-ii](https://leetcode.com/problems/word-pattern-ii): 给定pattern和str, 检查是否math. e.g. pattern = "abab", str = "redblueredblue"
    1.  def wordPatternMatch(self, pattern, str):
    2.      if not pattern: return str == ''
    3.      if not str: return pattern == ''
    
    5.      # check repeat
    6.      i = (pattern + pattern)\[1:-1\].find(pattern)
    7.      if i != -1: # there is repeated substring
    8.          subpattern = pattern\[:i+1\]
    9.          times = len(pattern) / len(subpattern)
    10.          if len(str) % times != 0: return False
    11.          substr = str\[:len(str)/times\]
    12.          if substr \* times != str: return False
    13.          pattern, str = subpattern, substr
    14.  
    15.      # backtracking check pattern vs str
    16.      def dfs(pattern, str, dict):
    17.          if len(pattern) == 0 and len(str) > 0: return False
    18.          if len(pattern) == len(str) == 0: return True
    19.          for end in range(1, len(str)-len(pattern)+2): # len(s) - end >= len(pattern) - 1
    20.              # print end, len(str), len(pattern)
    21.              if pattern\[0\] not in dict and str\[:end\] not in dict.values():
    22.                  dict\[pattern\[0\]\] = str\[:end\]
    23.                  if dfs(pattern\[1:\], str\[end:\], dict): return True
    24.                  del dict\[pattern\[0\]\]
    25.              elif pattern\[0\] in dict and dict\[pattern\[0\]\] == str\[:end\]:
    26.                  if dfs(pattern\[1:\], str\[end:\], dict): return True
    27.          return False
    28.  
    29.      return dfs(pattern, str, {})
6.  Boyer-Moore (BM)
    1.  字符串S和搜索词P, 搜索S从左往右, 而比较P则从右往左, 如果尾部字符不匹配, 只需要比较一次即可, 详见[阮一峰博文](http://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)
    2.  (无论是KMP还是BM, 关键点都在于当字符匹配不上的时候, 如何移动进行下一次匹配, BM中引入了怀字符和好后缀两个概念)
    3.  坏字符移动规则
        1.  后移位数 = 坏字符的位置(在P中) - 搜索词中的上一次出现位置
            *   程序实现时只用最后的位置, 当在搜索词中多次出现, 可能走回头路的情况, 当同时也说明有好后缀的情况, 可以用好后缀来cover
        2.  如下所示, 字符P是怀字符, 对应E作为位置为6, 字符P在搜索词中的位置为4, 所以移动2步. (如果字符P不存在与搜索词, 则从起后一位开始即可, 即位置为-1)
        3.  ![[Archive/面试资料/Programming/_resources/String_Matching.resources/unknown_filename.png]]
    4.  好后缀移动规则
        1.  后移位数 = 好后缀的位置 - 搜索词中的上一次出现位置
            *   好后缀的位置以最后一个字符为准, 即搜索词的尾部
            *   好后缀位置:
                *   最长好后缀, 如下的MPLE, 如果在搜索词走出现多次, 则移动到最后的那一个
                *   如果最长好后缀只出现一次, 则看其他好后缀, 如PLE, LE和E, 如果有, 则他们肯定出现在头部, 下例只有E满足条件, 所以E的上一次位置为0
        2.  当比较到如下所示, 根据坏字符规则只移动2步, 而根据好后缀, 移动位数为6 - 0 = 6, 取两者最大.
        3.  ![[Archive/面试资料/Programming/_resources/String_Matching.resources/unknown_filename.1.png]]
    5.  BM算法类似KMP需要对搜索词P进行预处理, 记录BadChar和GoodSuffix规则, BC\[c\]数组记录字符c最后出现的位置, GS\[i\]记录以i为结尾的后缀和搜索词P的公共后缀长度
    6.  实现可参考[博文](http://www.cnblogs.com/lanxuezaipiao/p/3452579.html), 文中实现BC是看到到尾部的距离, 其实是等价的, 还有GS的优化实现.
7.  Sunday
    1.  https://vinoit.me/2016/11/13/single-string-match-KMP-BM-Sunday/
8.  Rabin-Karp: 模式P长度为m, m大小的滑动窗口作用于长度为n的字串T上, 分别将长度为m字符串转换成十进制数, 如下图所示, 若某个m长字串与P所得的数不相等, 则肯定不匹配; 相等还存在伪命中问题, 需要线性比较m才能真正确定,所以时间复杂度为O(mn),但命中毕竟少, 期望的匹配时间为O(n)
    1.  ![[Archive/面试资料/Programming/_resources/String_Matching.resources/unknown_filename.2.png]]
9.  KMP



----

- Date: 2019-02-11
- Tags: #Interview/Programing 



