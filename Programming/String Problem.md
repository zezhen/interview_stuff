# String Problem
----



1.  [[字符串包含 Find Substring.md|字符串包含 Find Substring]]
2.  [[字符串表达式 Expression_Calculator.md|字符串表达式 Expression/Calculator]]
3.  [[回文问题.md|回文问题]][[Palindrome Problem|Palindrome Problem]]
4.  [[字符串匹配String Matching.md|字符串匹配String Matching]]
5.  合法括号系列
    1.  [valid-parenthesis-string](https://leetcode.com/problems/valid-parenthesis-string/description/): 给定包含(, ) 或 \* 的字符串, \* 可以表示成(, )或空, 判断是否valid
        1.  第一次简单想法是错的, 需要记录到目前为止最少/最多要处理的( 或者 pair.
    2.  [generate-parentheses](https://leetcode.com/problems/generate-parentheses/description/): 给定n对(), 构建所有可能的合法组合
        1.  回溯法, 第一个字符肯定是(, 当(数量大于)可以增加), 否则只能添加(
    3.  [minimum-add-to-make-parentheses-valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid): 任意位置添加 ( 或 ) 使其变得合法, 求最少添加数.
        1.  计数left和right, 如果right > left, 需要立马修正, 否则延到最后.
    4.  [longest-valid-parentheses](https://leetcode.com/problems/longest-valid-parentheses/description/): 给定只包含’(‘和’)’的字符串, 找到最长的合法的子串
        1.  def longestValidParentheses(self, s):
        2.      # DP problem, use count\[i\] keep the max count ending by index i
        3.      # if s\[i\] = (, count\[i\] = 0
        4.      # if s\[i\] = ), s\[i-1\] = (, it's a pair, count\[i\] = count\[i-2\] + 2
        5.      #              s\[i-1\] = ) and s\[i-1-count\[i-1\]\] = (,  count\[i\] = count\[i-1\] + 2 + count\[i-2-count\[i-1\]\]
        6.      ans, count = 0, \[0\] \* len(s)
        7.      for i in xrange(1, len(s)):
        8.          if s\[i\] == ')':
        9.              if s\[i-1\] == '(':
        10.                  count\[i\] = (count\[i-2\] if i >= 2 else 0) + 2
        11.              elif i-1-count\[i-1\] >= 0 and s\[i-1-count\[i-1\]\] == '(':
        12.                  count\[i\] = count\[i-1\] + 2
        13.                  if i-2-count\[i-1\] >= 0:
        14.                      count\[i\] += count\[i-2-count\[i-1\]\]
        15.              ans = max(ans, count\[i\])
        16.      return ans
    5.  r[emove-invalid-parentheses](https://leetcode.com/problems/remove-invalid-parentheses): Remove the minimum number of invalid parentheses in order to make the input string valid, return all possible results.
        1.  def removeInvalidParentheses(self, s, pars=\['(', ')'\]):
        2.      # scan s from left to right, count number of ( and )
        3.      # if there is extra ')' at position i, we will know immediately
        4.      #     we have multiple choice to remove either one ), after removal we can recursively call next
        5.      #     one thing important is that we need to record the scan position and remove position for next recursion
        6.      #     scan position guarantees we don't need to scan the position we already checked
        7.      #     remove position states the next possible remove position in next recursion to avoid duplicated check.
        8.      # if there is extra '(' error, we can know until reach end
        9.      #     then look back, same as scan left to right but need reverse the ( and )
        10.      # how about characters?  no impact on the parentheses valid
        11.  
        12.      ans = \[\]
        13.      def remove(s, remove\_i, scan\_i, pars):
        14.          count = 0
        15.          for i in xrange(scan\_i, len(s)):
        16.              if s\[i\] == pars\[0\]:
        17.                  count += 1
        18.              elif s\[i\] == pars\[1\]:
        19.                  count -= 1
        20.  
        21.              if count < 0:
        22.                  for j in xrange(remove\_i, i+1):
        23.                      if s\[j\] == pars\[1\] and (j == remove\_i or s\[j-1\] != pars\[1\]):
        24.                          remove(s\[:j\]+s\[j+1:\], j, i, pars)
        25.                  return
        26.          if count == 0:
        27.              ans.append(s if pars\[0\] == '(' else s\[::-1\])
        28.          if count > 0 and pars\[0\] == '(':
        29.              remove(s\[::-1\], 0, 0, \[')', '('\])
        30.      remove(s, 0, 0, \['(', ')'\])
        31.      return ans
    6.  加括号计数问题 -> [[String Expression_Calculator|String Expression/Calculator]]
6.  字符串拆分
    
    1.  Decode
        1.  [decode-ways](https://leetcode.com/problems/decode-ways/description/): 26个字符一次编码成1到26, 给定一个数字, 求decode可能性. 
            1.  dp\[i\]记录到\[0:i\]的编码数量, dp\[-1\]即为所求
        2.  [decode-ways-ii](https://leetcode.com/problems/decode-ways-ii/description/): 在#1的基础上增加\* (可代表1-9). 
            1.  在1) 的基础上多增加判断, 
            2.  更好的方法是预先build可能的几种cases.
        3.  [length-of-longest-fibonacci-subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/): 给定数组, 求最长的fibonacci数组. 
            1.  dp\[n\]\[m\]表示以a\[m\], a\[n\]结尾的fibonacci数组长度, 对于dp\[i\], 左右扫描l, r是的a\[l\]+a\[r\] = a\[i\], dp\[i\]\[r\] = dp\[r\]\[l\] + 1, 以此找到最大的dp
            2.  hashset保存数字, i, j (j>i)两指针遍历, 查看 A\[i\] + A\[j\]是否存在, 存在则move forward在判断
        4.  [split-array-into-fibonacci-sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/): 将字符串解码成fibonacci sequence. 
            1.  i, j (j>i) 两指针开始, 找到第一二个数字, 然后依次判断后续.
        5.  [restore-ip-addresses](https://leetcode.com/problems/restore-ip-addresses/description/): 给定未分割的ipv4字符串, 将其分割成合法ip地址. 类似4), 合理ip地址的判断条件为4个区间在\[0-255\]的数字
    2.  Word Break: 给定字符串S以及字符串字典, , 2是, 3稍微变形是; 刚开始简单以为backtracking是解法, 后来发现有很多重叠解空间, 适合DP, 尝试backtracking才发现原来是Memo; 最后看3的最快解才发现, 简单做str slice in set即可 (这不是算法的优势, 而是Python库的高效, 比起自己申请O(n)的空间, 然后依次处理, python slice只是[copy referrence](https://stackoverflow.com/questions/5131538/slicing-a-list-in-python-without-generating-a-copy), 相当高效, 但算法层面就很低效了)
        1.  [word-break](https://leetcode.com/problems/word-break/description/): 判断S能否由字典中的词组成.
            1.  dp\[i\]记录S\[:i\]是否可以由字典中的词组成, j: i -> 0, dp\[i\] = True if S\[j:i\] in dict and dp\[j-1\] == True
            2.  或者BT+memo, 其实速度挺快的
    
    1.  [word-break-ii](https://leetcode.com/problems/word-break-ii/description/): #1的基础上找出所有可能的解
        1.  backtracking + memo
    2.  [concatenated-words](https://leetcode.com/problems/concatenated-words): 在字典中找出可由其他字串组成的字符串
        1.  对每个词, 执行#1, 如果True, 则加入ans中
        2.  order words by their length in desc order, build the trie tree, for word w, check through the trie tree, if node contains 'word', it means prefix is a word, (there is no duplicates, don't need count for words number), we need to choose continue current path down or restart from root, thus we need a candidate nodes queue for next step, start can be always be root. what's the complexity?
            1.  comment: tried but more complicated, there is no reuse of scanned part
    
7.  字符串相似/搜索
    1.  [similar-string-groups](https://leetcode.com/problems/similar-string-groups): 给定多个字符串, 如果w1交换自己不同位置的两个字符即可得w2, 则w1和w2相似, 求有多少个相似的group.
        1.  此题的基本思路为 1) 根据word之间的相似性建立图, 2) 再图上用dfs或者union-find统计连通图个数. 其中1)为性能瓶颈, 2) 的复杂度为O(N)
        2.  思路1: 两两计算word之间的mismatch情况, 如果正好为2, 则相似, 复杂度为O(kN^2), k为word的长度
        3.  思路2: 对每一个word的每一个位置和不同位置进行交换, 查看新的word’ 是否存在于wordlist中, 复杂度为O(Nk^3), 其中生成新的word’ 需要O(k)时间.
        4.  如果N < k^2时, 思路1更快, 否则思路2更快.
        5.  def numSimilarGroups(self, A):
        6.      def similar(w1, w2):
        7.          mm = 0
        8.          for i, ch in enumerate(w1):
        9.              if ch != w2\[i\]:
        10.                  mm += 1
        11.                  if mm > 2: return False
        12.          return mm == 2
        13.  
        14.      def swapTwo(word, w\_idx):
        15.          k = len(word)
        16.          sim\_idx = \[\]
        17.          for i in range(k-1):
        18.              for j in range(i+1, k):
        19.                  word\_sim = word\[:i\] + word\[j\] + word\[i+1:j\] + word\[i\] + word\[j+1:\]
        20.                  if word\_sim in w\_idx: sim\_idx.append(w\_idx\[word\_sim\])
        21.          return sim\_idx
        22.  
        23.      def connect(edges, visited, i):
        24.          if visited\[i\]: return
        25.          visited\[i\] = True
        26.          for neighbor in edges\[i\]:
        27.              if visited\[neighbor\]: continue
        28.              connect(edges, visited, neighbor)
        
        30.      A = list(set(A))
        31.      n\_words, n\_letters = len(A), len(A\[0\])
        32.      edges = collections.defaultdict(list)
        33.      if n\_words >= n\_letters \*\* 2:
        34.          w\_idx = {A\[i\]:i for i in range(n\_words)}
        35.          for i in range(n\_words-1):
        36.              sim\_idxes = swapTwo(A\[i\], w\_idx)
        37.              for j in sim\_idxes:
        38.                  edges\[i\].append(j)
        39.                  edges\[j\].append(i)
        40.      else:
        41.          for i in xrange(n\_words):
        42.              for j in xrange(i+1, n\_words):
        43.                  if similar(A\[i\], A\[j\]):
        44.                      edges\[i\].append(j)
        45.                      edges\[j\].append(i)
        46.  
        47.      ans = 0        
        48.      visited = \[False\] \* n\_words
        49.      for i in xrange(n\_words):
        50.          if visited\[i\]: continue
        51.          connect(edges, visited, i)
        52.          ans += 1
        53.      return ans
    2.  [word-ladder](https://leetcode.com/problems/word-ladder/description/): 如果w1只改变一个字符即可得w2, 说明两个可以transformable, 给定beginWord, endWord以及wordlist, 看能否从beginWord transform to endWord.
    3.  [word-ladder-ii](https://leetcode.com/problems/word-ladder-ii/description/): 在上例基础上找出所有最短transform的路劲.
        1.  基本思路为 1) 建立word之间关系建立transformable graph, 2) BFS从beginWord到endWord看是否可达, 或者所有最短路劲.
        2.  步骤1) 
            1.  思路1: 两两计算word间是否可达, 检查mismatch是否为1即可. 复杂度为O(kN^2)
            2.  思路2: 对word的每个字符, 用a-z (排除自己) 替换, 检查是否存在于wordlist中. 复杂度为O(N\*26\*k^2), 组成新字符串需要O(k) time.
            3.  思路3: 从wordlist构建trie tree, 在trie tree上搜索并可允许跳过某一层, 找出所有叶子节点的word. 复杂度为O(Nk + Nkx), x <= 26
        3.  步骤2)
            1.  采用基本BFS可解
            2.  采用bi-direction BFS速度更快
    4.  [word-squares](https://leetcode.com/problems/word-squares): 给定等长wordlist, 从中找出一组word组成一个square, 第i行=第i列
        1.  backtracking, 第i+1行的candidate取决于第i列的prefix
    5.  [word-search-ii](https://leetcode.com/problems/word-search-ii): 在二维字符矩阵中找匹配的words
        1.  trie tree + DFS
8.  DP on string:
    1.  [interleaving-string](https://leetcode.com/problems/interleaving-string/description/)
    2.  [concatenated-words](https://leetcode.com/problems/concatenated-words)
    3.  [stickers-to-spell-word](https://leetcode.com/problems/stickers-to-spell-word)
9.  Tree 
    1.  [construct-binary-tree-from-string](https://leetcode.com/problems/construct-binary-tree-from-string/description/)
    2.  [scramble-string](https://leetcode.com/problems/scramble-string/description/)
    3.  [replace-words](https://leetcode.com/problems/replace-words)
10.  Decode String
    1.  [decode-string](https://leetcode.com/problems/decode-string)
    2.  [decoded-string-at-index](https://leetcode.com/problems/decoded-string-at-index)
11.  [unique-word-abbreviation](https://leetcode.com/problems/unique-word-abbreviation)
12.  [minimum-unique-word-abbreviation](https://leetcode.com/problems/minimum-unique-word-abbreviation)
13.  [word-abbreviation](https://leetcode.com/problems/word-abbreviation/description/)
14.  [guess-the-word](https://leetcode.com/problems/guess-the-word)
15.  [integer-to-english-words](https://leetcode.com/problems/integer-to-english-words/description/)
16.  
17.  [longest-word-in-dictionary-through-deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/)
18.  [substring-with-concatenation-of-all-words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/)
19.  
20.  Subsequence
    1.  [split-array-into-consecutive-subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences)
    2.  [sum-of-subsequence-widths](https://leetcode.com/problems/sum-of-subsequence-widths/description/)
    3.  [number-of-matching-subsequences](https://leetcode.com/problems/number-of-matching-subsequences)
    4.  [longest-consecutive-sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)
    5.  [stamping-the-sequence](https://leetcode.com/problems/stamping-the-sequence/description/)
21.  字符排列
    1.  [k-similar-strings](https://leetcode.com/problems/k-similar-strings): 给定字符串A和B, 将A中的字符交换位置使得等于B, 求最小交换次数.
        1.  
    2.  [reorganize-string](https://leetcode.com/problems/reorganize-string/description/): 重排字符串字符, 使得相同字符间隔至少为1, 求新字符串.
        1.  对每个字符计数, 加入到最大堆
        2.  每次选取频率最大的字符ch
            1.  如果该字符ch在上次刚选过, 则选择第二个
            2.  选中字符频率减一, 重新插入最大堆, 直到全部选完
    3.  [rearrange-string-k-distance-apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/description/): #1升级, 至少为k, 求新字符串.
        1.  对每个字符计数, 加入到最大堆中maxHeap
        2.  申请长度为k的链表 buffer
        3.  每次从maxHeap中取出最大频率字符, 加入新字符尾以及buffer尾部, 频率减一
        4.  不同与#1, 立马放回maxHeap, 字符先加入buffer尾部, 等buffer size > k, 从头部取出元素, 加回maxHeap
        5.  直到全部选完
    4.  [task-scheduler](https://leetcode.com/problems/task-scheduler/description/): 类似#1, 可以添加idel使得满足间隔至少为k, 求task总时长.
        
        *   首先需要看most common字符, 它构成了基本的格局, 比如task=ACCCEEE, n=2 => frame is CE\_CE\_CE, most common数量是3, tie的数量是C和E, 为2, frame的长度为 CE\_CE\_ + CE => (mc - 1) \* (n+1) + tie\_ct, 然后将剩余元素依次插入到chunk之后, 比如”CE\_”为一个chunk, 有空格就替换, 没有就插入, 以下两种可能性:
            1.  ACCCEEE => CEACE\_CE
            2.  AABCCCDEEEFG => CEADCEAFCEBG
        *   最后的size即为max(len(tasks), (mc-1)\*(n+1) + tie\_ct)
        *   
        
        1.  def leastInterval(self, tasks, n):
        2.      c = collections.Counter(tasks)
        3.      mc, tie\_ct = c.most\_common(1)\[0\]\[1\], 1
        4.      for k, v in c.most\_common()\[1:\]:
        5.          if v == mc:
        6.              tie\_ct += 1
        7.          else:
        8.              break
        
        10.      return max(len(tasks), (mc-1)\*(n+1) + tie\_ct)
22.  [旋转字符串](https://wizardforcel.gitbooks.io/the-art-of-programming-by-july/content/01.01.html): 要求把字符串前面的若干个字符移动到字符串的尾部, 如abcdef -> cdefab, T:O(n), S:O(1)
    *   三步翻转: 把数组分成两部分XY, 分别翻转X和Y, 然后做一次翻转, 即rev(rev(X)+rev(Y)) = YX
    *   扩展:
        *   单词翻转: 单词内字符顺序不变, 单词间反序 [reverse-words-in-a-string](https://leetcode.com/problems/reverse-words-in-a-string), [reverse-words-in-a-string-ii](https://leetcode.com/problems/reverse-words-in-a-string-ii), [reverse-words-in-a-string-iii](https://leetcode.com/problems/reverse-words-in-a-string-iii)
        *   单链表旋转
23.  转换成整数/浮点数 atoi/atof: 提问: 1) 字符范围 - 正负号/浮点号/其他非法字符 2) 溢出问题
    1.  [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi)




----

- Date: 2012-09-10
- Tags: #note #Interview/Programing 



