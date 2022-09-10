# Palindrome Problem
----

1.  回文子串判断
    1.  以i为中心向两边扫描, 考虑奇偶情况 T: O(n^2)
    2.  Manacher算法 O(n)

*   先将字符串abc转换成@#a#b#c#$, 插入#将奇偶判断合并为一, @$作为终止符减少边界判断
*   一次扫描转换后的数组S, 记录回文半径为P\[i\], 同时增加辅助变量: mx: 当前回文最远触及的位置, 以及id=mx-P\[id\]
*   如下图所示, 当前检测位置为i<mx, 则P\[i\] >= min(P\[j\], mx-i), j为以id为中心的对称点, 所以P\[i\]至少有P\[j\]的长度, 或许更多, 如此就不需要重复扫描这部分了, 对于超出mx的部分, 则继续扫描, 如果对称则拓展mx, i就变成新的id
*   如果i>mx, 则是全新的领域, 综合算法复杂度O(n)
*   ![[Archive/面试资料/Programming/_resources/Palindrome_Problem.resources/unknown_filename.1.png]]
*   ![[Archive/面试资料/Programming/_resources/Palindrome_Problem.resources/unknown_filename.png]]

1.  def manachers(S):
2.      A = '@#' + '#'.join(S) + '#

----

- Date: 2018-12-25
- Tags: #Interview/Programing 




3.      P = \[0\] \* len(A)
4.      center = right = 0
5.      for i in xrange(1, len(A) - 1):
6.          if i < right:
7.              P\[i\] = min(right - i, P\[2 \* center - i\])
8.          while A\[i + P\[i\] + 1\] == A\[i - P\[i\] - 1\]:
9.              P\[i\] += 1
10.          if i + P\[i\] > right:
11.              center, right = i, i + P\[i\]
12.      return P

4.  整串回文: 左右扫描即可
    1.  [valid-palindrome](https://leetcode.com/problems/valid-palindrome)/[valid-palindrome-ii](https://leetcode.com/problems/valid-palindrome-ii)
    2.  [palindrome-number](https://leetcode.com/problems/palindrome-number)/[prime-palindrome](https://leetcode.com/problems/prime-palindrome)/[largest-palindrome-product](https://leetcode.com/problems/largest-palindrome-product): 与数学相关, 意思不大
    3.  其他数据结构
        1.  [palindrome-linked-list](https://leetcode.com/problems/palindrome-linked-list)
        2.  stack?
5.  回文排列等
    1.  [palindrome-permutation](https://leetcode.com/problems/palindrome-permutation): 给定字符串, 判断其某种排列是否可能为回文. 
        *   计算各字符数量, 奇数项最多为1
    2.  [palindrome-permutation-ii](https://leetcode.com/problems/palindrome-permutation-ii): 给定字符串, 找出所有回文排列.
        *   首先如1检查各字符数量, mid=奇数次字符, 全偶数为’’
        *   各字符数量减半, 构造有重复字符字符串, 添加mid以及另一半即可.
    3.  [longest-palindrome](https://leetcode.com/problems/longest-palindrome): 给定一些字符构造最长回文. 
        *   偶数字符全进, 大于1的字符减1, 保留一个奇数
6.  数字回文
    1.  [find-the-closest-palindrome](https://leetcode.com/problems/find-the-closest-palindrome/description/): (hard)给定数字n, 找到离它最近的回文数字.
        *   参考[awice](https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/Python-Simple-with-Explanation), 首先定位可能的回文数字
            1.  给定长度为3的数字, ’99’或’101’是最低边界, ‘999’或’1001’是最高边界
            2.  数字123, 开头到中间部分12, 起上下边界为11,13, 对应的回文数字为111, 131, 其他情况肯定大很多
        *   找出两种可能数字, 依次判断距离即可, amazing!!
    2.  [super-palindromes](https://leetcode.com/problems/super-palindromes/description/): (hard) 在指定范围内寻找回文数字.  
        *   (与#3类似, 需要快速确定下一个回文, 而不是暴力求解)
        *   如3213的下一个回文, 可能是9999, 3223(half is 32 and reversed half), 3333 (half+1 is 33, plus reversed half), choose the min one
7.  hard题目(各种虐)
    1.  [palindrome-pairs](https://leetcode.com/problems/palindrome-pairs/description/): 给定字符串数组, 找出所有word\[i\]+word\[j\]是回文的组合. 
        *   构建trie数帮助搜索, 然后需要处理三种情况: 长字符+短字符, 短字符+长字符, 以及空字符情况.
    2.  [palindromic-substrings](https://leetcode.com/problems/palindromic-substrings/description/): 给定字符串S, 统计所有回文子串的个数. 
        *   1) DP方法, dp\[i\]为以i结尾的回文, 求dp\[i+1\]只需要遍历dp\[i\]中的回文即可; 
        *   2) manachers如上, P\[i\]为以i为中心的回文子串半径r, (r+1)/2即为以i为中心的回文子串个数. 
    3.  [longest-palindromic-substring](https://leetcode.com/problems/longest-palindromic-substring): 求给定字符串s的最长回文子串. 
        *   1) manacher方法, 
        *   2) 类似DP, 当前i位置, 已知max\_len, 我们就求以i为结尾的回文即可, 长度可以是max\_len+1(奇数)或max\_len+2(偶数), 小于max\_len情况就不用考虑了, 回文判断 s == s\[::-1\]非常快.
    4.  [palindrome-partitioning](https://leetcode.com/problems/palindrome-partitioning): 给定字符串s, 将其分解成回文的字符串数组,返回所有可能性. 
        *   DFS, 一次判断s\[:i\]是否为回文, 然后在继续搜索s\[i+1:\]
    5.  [palindrome-partitioning-ii](https://leetcode.com/problems/palindrome-partitioning-ii/description/): 给定字符串s, 将其分解成回文字符串数组的最小cut.  
        *   1) DP思路不难, 一下子没想到. cut\[i\] is the minimum of cut\[j - 1\] + 1 (j <= i), if \[j, i\] is palindrome. If \[j, i\] is palindrome, \[j + 1, i - 1\] is palindrome, and c\[j\] == c\[i\].
        *   2) [O(n)空间算法](https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198)
    6.  [longest-palindromic-subsequence](https://leetcode.com/problems/longest-palindromic-subsequence): 给定字符串, 找出最长回文子串(非连续)
        *   经典DP方法, dp\[i\]\[j\] 表示s\[i:j+1\]中最长非连续回文子串
        *   if s\[i\] == s\[j\], dp\[i\]\[j\] = dp\[i+1\]\[j-1\] + 2, else dp\[i\]\[j\] = max(dp\[i+1\]\[j\], dp\[i\]\[j-1\]), dp\[0\]\[n-1\]即为答案
    7.  [shortest-palindrome](https://leetcode.com/problems/shortest-palindrome/description/): 在字符串s前加入字符使其变成回文. 
        *   即寻找以第一个字符开头的最长回文. KMP based solution, construct new string l = s + ‘#’ + s\[::-1\], run kmp and get the jump array p, p\[-1\] point to the end of the palindrome start from beginning. (amazing!!)
    8.  [count-different-palindromic-subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences/description/): 给定字符串, 统计不同的回文可能子串(非连续)
        *   参考自[kay\_deep](https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109509), 记录26个字符的位置, 依次处理每个字符, 比如a, 最左和最右的位置i和j, 如果i != j, 则可以有aa的情况, 本身有a的情况, 所以数量加2, 
        *   然后同样方法检查子串s\[i+1:j\], 这个时候假设已经有了aa在外层, 所以就不会有重复情况.
        *   amazing!!



----

- Date: 2018-12-25
- Tags: #Interview/Programing 



