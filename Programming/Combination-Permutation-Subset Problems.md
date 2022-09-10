# Combination-Permutation-Subset Problems
----

\# ==Subsets==

1.  [subsets](https://leetcode.com/problems/subsets): Given a set of distinct integers, nums, return all possible subsets (the power set).
    
    *   不重复元素, 所以递归遍历即可, for循环里从不同的位置开始
    
    1.  def subsets(self, nums):
    2.      ans = \[\]
    3.      def dfs(queue, start, n):
    4.          ans.append(list(queue))
    5.          for i in xrange(start, n):
    6.              queue.append(nums\[i\])
    7.              dfs(queue, i + 1, n)
    8.              queue.pop()
    9.      dfs(deque(), 0, len(nums))
    10.      return ans
2.  [subsets-ii](https://leetcode.com/problems/subsets-ii): Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
    
    *   有重复元素, 就需要考虑去重, 如下黑体所示, 首先排序, 然后如果已经有相同元素作为start, 则忽略
    
    1.  def subsetsWithDup(self, nums):
    2.      ans = \[\]
    3.   nums.sort()
    4.      def dfs(queue, start, n):
    5.          ans.append(list(queue))
    6.          for i in xrange(start, n):
    7.              if i > start and nums\[i\] == nums\[i-1\]: continue
    8.              queue.append(nums\[i\])
    9.              dfs(queue, i + 1, n)
    10.              queue.pop()
    11.      dfs(deque(), 0, len(nums))
    12.      return ans


\# ==Permutation==

*   全排列

1.  递归算法: 从集合中依次选出每一个元素，作为排列的第一个元素，然后对剩余的元素进行全排列
2.  邻位对换: 下一个排列总是上一个排列某相邻两位对换得到的, 可以总是从最末尾开始, 依次与左侧对换, 如此往复
    1.  TODO
3.  字典序排列: 从当前排列生成字典序刚好比它大的下一个排列, 以21543为例子
    *   从右端开始, 找到第一个x\_i<x\_i+1，x\_i = 1
    *   找到i位右边比x\_i大的数的最小值x\_j，x\_j = 3
    *   交换x\_i, x\_j, 得到23541
    *   把第(i+1)位到最后的部分翻转, 得到23145

1.  [next-permutation](https://leetcode.com/problems/next-permutation/description/): rearranges numbers into the lexicographically next greater permutation of numbers.
    1.  def nextPermutation(self, nums):
    2.      n = len(nums)
    3.      i = n - 1
    4.      while i > 0 and nums\[i\] <= nums\[i - 1\]:    # find the first number i that greater than i-1
    5.          i -= 1
    6.      self.reverse(nums, i, n - 1)    # reverse in-place
    7.      for j in range(i,n):
    8.          if nums\[j\] > nums\[i-1\]:       # find the first one from the tail than greater than i-1, or stop at 0
    9.              self.swap(nums,i-1,j)
    10.              break
    11.  
    12.  def reverse(self,nums,i,j):
    13.      for k in range(i,(i+j)/2+1):
    14.          self.swap(nums,k,i+j-k)
    15.  def swap(self,nums,i,j):
    16.      nums\[i\],nums\[j\] = nums\[j\],nums\[i\]
2.  [permutations](https://leetcode.com/problems/permutations): 给定数组, 返回所有排列
    1.  执行n!次如上的nextPermutation
    2.  递归算法: python列表操作很方便, 否则得用used标识
        1.  def permute(self, nums):
        2.      res = \[\]
        3.      def bt(nums,path):
        4.          if len(nums) == 0:
        5.              res.append(path)
        6.          for i in range(len(nums)):
        7.              bt(nums\[:i\]+nums\[i+1:\],path + \[nums\[i\]\])
        8.      bt(nums,\[\])
        9.      return res
3.  [permutations-ii](https://leetcode.com/problems/permutations-ii): 数组有重复情况
    
    *   排序, 然后与前一个元素比较
    
    1.  class Solution(object):
    2.      def permuteUnique(self, nums):
    3.          res = \[\]
    4.   nums.sort()
    5.          def bt(nums,path):
    6.              if len(nums) == 0:
    7.                  res.append(path)
    8.              for i in range(len(nums)):
    9.                  if i > 0 and nums\[i\] == nums\[i-1\]: continue
    10.                  bt(nums\[:i\]+nums\[i+1:\],path + \[nums\[i\]\])
    11.          bt(nums,\[\])
    12.          return res
4.  [di-string-match](https://leetcode.com/problems/di-string-match): 给定包含D(decrease)和I(increase)的字符串S, 如果S\[i\] = “I”, 则A\[i\] < A\[i+1\], "D”则A\[i\] > A\[i+1\], 从\[0,N\]产生任意permutation, 如IDID => \[0,4,1,3,2\]
    
    *   We track high (h = N - 1) and low (l = 0) numbers within \[0 ... N - 1\]. When we encounter 'I', we insert the current low number and increase it. With 'D', we insert the current high number and decrease it. In the end, h == l, so we insert that last number to complete the permutation. credit to [votrubac](https://leetcode.com/problems/di-string-match/discuss/194906/C++-4-lines-high-low-pointers)
    
    1.  def diStringMatch(self, S):
    2.      ans = \[\]
    3.      l, h = 0, len(S)
    4.      for i in xrange(len(S)+1):
    5.          if i == len(S) or S\[i\] == 'I':
    6.              ans.append(l)
    7.              l += 1
    8.          else:
    9.              ans.append(h)
    10.              h -= 1
    11.      return ans
5.  [find-permutation](https://leetcode.com/problems/find-permutation): 如#4一样的DI字符串, 返回最小的数字
    
    *   [stefanPochamnn](https://leetcode.com/problems/find-permutation/discuss/96624/1-liner-and-5-liner-visual-explanation): If it's all just I, then the answer is the numbers in ascending order. And if there are streaks of D, then just reverse the number streak under each
    *   ![[Archive/面试资料/Programming/_resources/Combination-Permutation-Subset_Problems.resources/unknown_filename.png]]
    
    1.  class Solution(object):
    2.      def findPermutation(self, s):
    3.          a = range(1, len(s) + 2)
    4.          for m in re.finditer('D+', s):
    5.              i, j = m.start(), m.end() + 1
    6.              a\[i:j\] = a\[i:j\]\[::-1\]
    7.          return a
6.  [valid-permutations-for-di-sequence](https://leetcode.com/problems/valid-permutations-for-di-sequence/description/): #4,5的扩展, 给定字符串返回有多少种可能性
    
    *   dp\[i\]\[j\] means the number of possible permutations of first i + 1 digits, where the i + 1th digit is j + 1th smallest in the rest of digits. credit to [lee215](https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/168278/C++JavaPython-DP-Solution-O(N2))
    *   ![[Archive/面试资料/Programming/_resources/Combination-Permutation-Subset_Problems.resources/unknown_filename.1.png]]
    
    1.  def numPermsDISequence(self, S):
    2.      dp = \[1\] \* (len(S) + 1)
    3.      for c in S:
    4.          if c == "I":
    5.              dp = dp\[:-1\]
    6.              for i in range(1, len(dp)):
    7.                  dp\[i\] += dp\[i - 1\]
    8.          else:
    9.              dp = dp\[1:\]
    10.              for i in range(len(dp) - 1)\[::-1\]:
    11.                  dp\[i\] += dp\[i + 1\]
    12.      return dp\[0\] % (10\*\*9 + 7)
7.  [increasing-subsequences](https://leetcode.com/problems/increasing-subsequences): 给定数组, 找出所有长度至少为2的递增序列
    1.  subset方式, 修改去重条件
        
        1.  def findSubsequences(self, nums):
        
        1.      ans = \[\]
        2.  
        3.      def dfs(queue, start):
        4.          if len(queue) >= 2:
        5.              ans.append(list(queue))
        6.   used = set()
        7.          for i in xrange(start, len(nums)):
        8.   if nums\[i\] in used: continue
        9.              if not queue or nums\[i\] >= queue\[-1\]:
        10.                  queue.append(nums\[i\])
        11.   used.add(nums\[i\])
        12.                  dfs(queue, i+1)
        13.                  queue.pop()
        14.      dfs(deque(), 0)
        15.      return ans
    2.  略有DP思想, 保留每一步的candidates, credit to [stefanPochamnn](https://leetcode.com/problems/increasing-subsequences/discuss/97127), 实现方式很精妙
        1.  def findSubsequences0(self, nums):
        2.      subs = {()}
        3.      for num in nums:
        4.          subs |= {sub + (num,)
        5.                   for sub in subs
        6.                   if not sub or sub\[-1\] <= num}
        7.      return \[list(sub) for sub in subs if len(sub) >= 2\]
8.  [beautiful-arrangement](https://leetcode.com/problems/beautiful-arrangement):
    1.  def countArrangement(self, N):
    2.      candidates = set()
    3.      for i in xrange(1, N+1):
    4.          candidates.add(i)
    5.  
    6.      self.ans = 0
    7.      def dfs(candidates, N, i):
    8.          if i > N:
    9.              self.ans += 1
    10.              return
    11.          for n in candidates:
    12.              if (n % i == 0) or (i % n == 0):
    13.                  candidates.remove(n)
    14.                  dfs(candidates, N, i+1)
    15.                  candidates.add(n)
    16.  
    17.      dfs(candidates, N, 1)
    18.      return self.ans
9.  [permutation-sequence](https://leetcode.com/problems/permutation-sequence): find kth permutation sequence in lexicographical order
    1.  def getPermutation(self, n, k):
    2.      nums = range(1, n+1)
    3.      fact = \[1\]\*(n)
    4.   for i in range(1, n):
    5.   fact\[i\] = fact\[i-1\]\*nums\[i-1\]    # good to pre-calculate, which reduce runtime
    6.      result = \[\]
    7.      k -= 1
    8.      for i in range(1,n+1):
    9.          index = k/fact\[n-i\]
    10.          result.append(str(nums\[index\]))
    11.          del nums\[index\]
    12.          k = k%fact\[n-i\]
    13.      return ''.join(result)
10.  



\# ==Combination==

1.  [combinations](https://leetcode.com/problems/combinations): 从\[1,n\]的数字中找出k个数的组合.
    1.  与subsets基本一致, 只是选择k长度的subset而已
    2.  def combine(self, n, k):
    3.      ans = \[\]
    4.      def dfs(start, n, k, queue):
    5.   if len(queue) == k:
    6.              # deque operations are faster than \[\]
    7.              # list(deque) is same as queue\[:\]
    8.              ans.append(list(queue))
    9.              return
    10.          if start > n or n+1 - start + len(queue) < k: return
    11.  
    12.          for i in xrange(start, n+1):
    13.              queue.append(i)
    14.              dfs(i+1, n, k, queue)
    15.              queue.pop()
    16.      dfs(1, n, k, deque())
    17.      return ans
2.  [combination-sum](https://leetcode.com/problems/combination-sum): 给定不重复的数组candidates和target数字, 找出所有不重复的组合和为target, 同一个数字可重复使用
    
    *   在原有框架基础上增加和判断, 
    *   排序以及for循环内的break为了剪枝, 提高运行速度
    
    1.  def combinationSum(self, candidates, target):
    2.      ans = \[\]
    3.   candidates.sort()
    4.  
    5.      def dfs(queue, acc\_sum, target, start):
    6.   if acc\_sum == target:
    7.              ans.append(list(queue))
    8.              return
    9.  
    10.          for i in xrange(start, len(candidates)):
    11.              if acc\_sum + candidates\[i\] <= target:
    12.                  queue.append(candidates\[i\])
    13.                  dfs(queue, acc\_sum + candidates\[i\], target, i)  # number can be used multiple times
    14.                  queue.pop()
    15.              else:
    16.   break
    17.  
    18.      dfs(deque(), 0, target, 0)
    19.      return ans
3.  [combination-sum-ii](https://leetcode.com/problems/combination-sum-ii): 给定不重复的数组candidates和target数字, 找出所有不重复的组合和为target, 同一个数字只能使用一次
    *   上例line #13将i改成i+1即可
4.  [combination-sum-iii](https://leetcode.com/problems/combination-sum-iii): 从\[1,9\]的数组中找出k个数, 使其和为n
    *   combination以及combination-sum的结合, 判断条件为sum = target 以及 len(queue) == k
5.  [combination-sum-iv](https://leetcode.com/problems/combination-sum-iv): 给定不重复正整数数组以及target数, 找出所有可能组合, 同一数字可重复使用.
    *   解法跟上面一样, 如果将正整数限制去掉, 允许负数, 则每个数组只能使用一次, 否则可能有无限种情况.



----

- Date: 2018-12-26
- Tags: #Interview/Programing 



