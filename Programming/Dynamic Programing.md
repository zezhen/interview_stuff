# Dynamic Programing
----

1.  ====重叠子空间==== Optimal substructure + Overlapping subproblems
    
    1.  这是最重要的部分, 也是DP的关键所在!
    2.  如果一下子找不到? 尝试先用naive的方法解决, 比如递归/备忘录/暴力搜索, 然后在构造重叠子空间问题.
        1.  Your first solution must also meet these restrictions:
    
    1.  The recursive calls must be self-contained. That means no global variables.
    2.  You cannot do tail recursion. Your solution must compute the results to each subproblem and then combine them afterwards.
    3.  Do not pass in unnecessary variables. Eg. If you can count the depth of your recursion as you return, don’t pass a count variable into your recursive function.
    
2.  ==状态转移==
    1.  当问题存在多种状态时, 需要先构建状态间的转移序列, 再对问题求解.
    2.  比如[best-time-to-buy-and-sell-stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75927)系列, 以及[minimum-swaps-to-make-sequences-increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119835/Java-O(n)-DP-Solution), [student-attendance-record-ii](https://leetcode.com/problems/student-attendance-record-ii)
3.  常用模式
    1.  下图列了三种常用DP模式, 针对不同的问题
        1.  两个同构对象相对独立, 比如两字符串, 从左上角dp\[0\]\[0\]开始, 不断拓展到dp\[n-1\]\[m-1\]
            1.  e.g. edit distance, longest common distance, etc
        2.  两个异构对象, 比如city和week, 不同对象的值有不用的结果, 如何找到一个'线路'使得结果最大, 通常有明确的起点.
            1.  [maximum-vacation-days](https://leetcode.com/problems/maximum-vacation-days), [freedom-trail](https://leetcode.com/problems/freedom-trail/description/), [dungeon-game](https://leetcode.com/problems/dungeon-game/description/), [minimum-window-subsequence](https://leetcode.com/problems/minimum-window-subsequence)
        3.  处理一个对象, 但不同位置先后顺序不同, 结果不同, 需要在其中选择最优的次序
            1.  [burst-balloons](https://leetcode.com/problems/burst-balloons/description/), [strange-printer](https://leetcode.com/problems/strange-printer), [remove-boxes](https://leetcode.com/problems/remove-boxes), [dungeon-game](https://leetcode.com/problems/dungeon-game/description/)
        4.  对于#1和#2, 更多不同的是方向, 应该如何选择?
            1.  对于#1, 反向操作通常是等价的, 但对于#2, j = n-1的状态必须是确定的, 由此才可以往前推.
            2.  在做[race-car](https://leetcode.com/problems/race-car)的时候, 我采用了#2的方式, 但是最后状态是不确定的, 除了位移, 还有速度, 所以必须引入更多的信息, 让问题变得异常复杂; 同时对于sub-problem的理解有误, 一直考虑着T(i.j)的问题, i是位移, j是速度, 而实际上T(i, j) = T(i-2^(j+2)+1), 1), 所以实际上只需要考虑位移即可.
    2.  ![[Archive/面试资料/Programming/_resources/Dynamic_Programing.resources/unknown_filename.1.png]]
4.  ==Self-Contained Subproblem==
    
    1.  The result of a subproblem doesn’t depends on external information, e.g. edit distance, T(i, j) means the distance of S\[:i\] and T\[:j\], it doesn’t depend on other characters in the rest part of S or T, thus T(i, j) is called self-contained subproblem.
    2.  However, the problems like ==[remove-boxes](https://leetcode.com/problems/remove-boxes),== let’s say T(i, j) is the points we remove the boxes \[i, j\] inclusive, if we find a k, that i <= k <= j, we remove box k, then the problem should be T(i,j)  = T(i, k-1) + T(k,k) + T(k+1, j), is that true? unfortunately, the points of T(i, k-1) depends on T(k+1, j), vice verse.
    3.  Another example is that for T(i, j), we want to remove box\[i\], but we find box\[m\] == box\[i\], so we’d better to keep it, remove \[i+1, m-1\] first, so the problem will be box\[i\], and box\[m, j\], the result of T(m, j) depends on how many box\[i\] before m, thus it’s not self-contained subproblem, we need additional information to make it to be. That’s can be T(i, j, k), k means how many boxes in same color with box\[i\].
    
    1.  Another problem is [burst-balloons](https://leetcode.com/problems/burst-balloons/description/), the external information is left and right boundary, the new definition of subproblem can be T(i, j, left, right) = max(left \* nums\[k\] \* right + T(i, k - 1, left, nums\[k\]) + T(k + 1, j, nums\[k\], right)) where i <= k <= j
5.  [[双向DP - cherry pickup|双向DP - cherry pickup]]
    1.  比如[cherry-pickup](https://leetcode.com/problems/cherry-pickup/description/), grid的每个cell表示这块区域的cherry量, 从(0,0)出发摘取cherry, 向下或向右到(n-1, n-1), 再向上向左返回(0,0), 求最大可摘取的cherry数量.
        1.  ![[Archive/面试资料/Programming/_resources/Dynamic_Programing.resources/unknown_filename.png]]


问题总结


1.  单字符串/数组问题
    *   [最长递增子序列](https://leetcode.com/problems/longest-increasing-subsequence/description/) LIS
        *   DP思想: L(j) = max {L(i), i<j && Ai<Aj  } + 1;  也就是说L(j)等于之前所有的L(i)中最大的的L(i)加一.这样的L(i)需要满足的条件就是Ai<Aj.这个推断还是比较容易理解的.就是选择j之前所有的满足小于当前数组的最大值.
            *   queue = \[nums\[0\]\]
            *   for i in range(1, len(nums)):
            *       j = bisect.bisect\_left(queue, nums\[i\])
            *       if j >= len(queue):
            *           queue.append(nums\[i\])
            *       else:
            *           queue\[j\] = nums\[i\]
        *   数组/递增, 这里有一种套路或者思想, 即maintain某一种数据结构, 当数组从n->n+1时, 可以通过该数据结构快速做出判断
            *   粗暴的方法, 当数组添加一个元素时, 只要依次往前扫描即可知以该元素结尾的LIS
            *   https://leetcode.com/problems/next-greater-element-i/description/
        *   这里的重点是maintain一个递增的数组, 该数据记录以该元素为结尾的一个LIS (往前找, 因为同时保留该数组中的其他元素)
            *   数组: 1, 3, 4, 2, 5 递增数组依次为
                *   1
                *   1,3
                *   1,3,4
                *   1,2,4   # 2替换3, 以2结尾的LIS的长度为2
                *   1,2,4,5 # 以5结尾的LIS长度为4, 但不代表1,2,4,是最长递增序列.
            *   每个元素被扫描一次, 查找递增数组复杂度为logN, 因此总复杂度为O(N\*logN)
    *   
2.  双字符串/数组问题
    1.  最大公共子串 (Longest Common Substring)
        1.  dp\[i\]\[j\] = 0                                          i=0 || j=0
        2.  dp\[i\]\[j\] = dp\[i-1\]\[j-1\]+1                        i>0,j>0, a\[i\] = b\[j\]
        3.  dp\[i\]\[j\] = 0                                          i>0,j>0, a\[i\] != b\[j\]
    2.  最长公共子序列 (Longest Common Subsequence)
        1.  dp\[i\]\[j\] = 0                                          i=0 || j=0
        2.  dp\[i\]\[j\] = dp\[i-1\]\[j-1\]+1                        i>0,j>0, a\[i\] = b\[j\]       
        3.  dp\[i\]\[j\] = max(dp\[i-1\]\[j\],dp\[i\]\[j-1\])        i>0,j>0, a\[i\] != b\[j\]
    3.  字符串编辑距离
        1.  [one-edit-distance](https://leetcode.com/problems/one-edit-distance): 给定两字符串s和t, 求是否只差1. 各一个pointer扫描字符串即可
        2.  [delete-operation-for-two-strings](https://leetcode.com/problems/delete-operation-for-two-strings/description/): DP, longest common subsequence
            1.  def logestCommonSubseq(self, word1, word2):
            2.      if not word1: return len(word2)
            3.      if not word2: return len(word1)
            
            5.      dp = \[\[0 for \_ in xrange(len(word1)+1)\] for \_ in xrange(len(word2)+1)\]
            6.      # set boundaries
            7.      # dp\[0\]\[j\], dp\[i\]\[0\] is 0
            8.      # for loop one by one
            9.      for i in xrange(1, len(word2)+1):
            10.          for j in xrange(1,len(word1)+1):
            11.              if word1\[j-1\] == word2\[i-1\]:
            12.                  dp\[i\]\[j\] = dp\[i-1\]\[j-1\] + 1
            13.              else:
            14.                  dp\[i\]\[j\] = max(dp\[i\]\[j-1\], dp\[i-1\]\[j\])
            15.      return len(word2) + len(word1) - 2 \* dp\[-1\]\[-1\]
        3.  [minimum-ascii-delete-sum-for-two-strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/): 在#2的基础上计算删除的字符ascii总和最小.
            1.  不同于#2, dp\[i\]\[j\]需要记录s1\[0:i\]和s2\[0:j\]的cost, 需要注意先设置边界
        4.  [edit-distance](https://leetcode.com/problems/edit-distance/description/): 经典DP, it’s wrong to calculate longest common substring and subtract it
            1.  def editDistance(self, word1, word2):
            2.      if not word1: return len(word2)
            3.      if not word2: return len(word1)
            4.  
            5.      dp = \[\[0 for \_ in xrange(len(word1)+1)\] for \_ in xrange(len(word2)+1)\]
            6.   # set boundaries
            7.      for j in xrange(len(word1)+1):
            8.          dp\[0\]\[j\] = j
            9.      for i in xrange(len(word2)+1):
            10.          dp\[i\]\[0\] = i
            11.      \# for loop one by one
            12.      for i in xrange(1, len(word2)+1):
            13.          for j in xrange(1, len(word1)+1):
            14.              if word1\[j-1\] == word2\[i-1\]:
            15.                  dp\[i\]\[j\] = dp\[i-1\]\[j-1\]
            16.              else:
            17.                  dp\[i\]\[j\] = min(dp\[i-1\]\[j-1\], dp\[i-1\]\[j\], dp\[i\]\[j-1\]) + 1
            18.      return dp\[-1\]\[-1\]
            19.  
        5.  [maximum-length-of-repeated-subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/): 给定两个字符串A和B, 求最长连续重复子串
            1.  DP, same as longest common subarray
3.  加和问题
    1.  0-1背包: 有N件物品和一个容量为V的背包。第i件物品的体积是w\[i\]，价值是v\[i\]。求解将哪些物品装入背包可使价值总和最大。

*   dp\[i\]\[j\] means the max value we get by packing first i goods with volume j bags (dp is a N \* V matrix)
*   dp\[i\]\[0\] = 0, dp\[0\]\[j\] = v\[0\] if j >= w\[0\] else 0
*   dp\[i\]\[j\] = max(dp\[i-1\]\[j\], dp\[i-1\]\[k-w\[i\]\] + v\[i\]), where k >= w\[i\], 

*   找零钱问题: 有数组penny，penny中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个整数target(小于等于1000)代表要找的钱数，求换钱有多少种方法。
    *   设dp\[i\]\[j\]为使用前i中货币凑成的j面值的种数，那么就会有两种情况：
    *   dp\[0\]\[\*\] = 0 means no coins
    *   dp\[i\]\[j\] = dp\[i-1\]\[j\] + dp\[i-1\]\[j - penny\[i\]\], where j >= penny\[i\]
*   [coin-change](https://leetcode.com/problems/coin-change/description/): 给定数量amount, 以及coins, e.g. \[2,3,5\], 找到coins和为amount的最少币数方案
    *   int coinChange(vector<int>& coins, int amount) {
    *       int Max = amount + 1;
    *       vector<int> dp(amount + 1, Max);
    *       dp\[0\] = 0;
    *       for (int i = 1; i <= amount; i++) {
    *           for (int j = 0; j < coins.size(); j++) {
    *               if (coins\[j\] <= i) {
    *                   dp\[i\] = min(dp\[i\], dp\[i - coins\[j\]\] + 1);
    *               }
    *           }
    *       }
    *       return dp\[amount\] > amount ? -1 : dp\[amount\];
    *   }

5.  状态转移问题
    1.  [minimum-swaps-to-make-sequences-increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/): Give two integer list A and B, we can swap A\[i\] and B\[i\] to make A and B are both strictly increasing. what’s the minimum swap?
        1.  def minSwap(self, A, B):
        2.      # refer to this [post](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119835/%0A)
        3.      # There are two types of states: swap and fix
        4.      # swapRecord means for the ith element in A and B, the minimum swaps if we swap A\[i\] and B\[i\]
        5.      # fixRecord means for the ith element in A and B, the minimum swaps if we DONOT swap A\[i\] and B\[i\]
        
        7.      swap, fix = 1, 0 # swap A\[0\] and B\[0\] or fix both
        8.      for i in xrange(1, len(A)):
        9.          if A\[i-1\] >= B\[i\] or B\[i-1\] >= B\[i\]:
        10.              # if we did swap in i-1 position, we need to swap again
        11.              swap += 1
        12.          elif A\[i-1\] >= A\[i\] or B\[i-1\] >= B\[i\]:
        13.              fix, swap = swap, fix + 1
        14.          else:
        15.              # either swap or fix is OK. Let's keep the minimum one
        16.              fix = min(fix, swap)
        17.              swap = fix + 1
        18.      return min(swap, fix)
6.  数学相关问题
    1.  Number Break
        1.  [counting-bits](https://leetcode.com/problems/counting-bits): 给定正整数n, 计算\[0,n\]所有数的二进制数的1的个数. O(n)时空.
        2.  [integer-break](https://leetcode.com/problems/integer-break): 给定整数n, 将n分解成至少两个正整数和, 求因子的最大乘积. 
        3.  [count-numbers-with-unique-digits](https://leetcode.com/problems/count-numbers-with-unique-digits/description/): 给定n, 计算区间\[0,10^n\]包含不重复数字的数字个数. (挺tricky的题目,需要找出数学规律)
    2.  数字partition问题 -> [[Array Problem|Array Problem]]
    3.  矩阵联乘问题: 给定n个矩阵{A1,A2,...,An}，矩阵A1的维数为p(i-1)×p(i), i = 1,2, ..., n，设p数组为\[30,35,15,5,10,20,25\]. 如何给矩阵连乘A1\*A2\*....\*An完全加上括号使用矩阵乘法中计算次数最少。
        1.  假定问题Ai\*Ai+1\*...Aj被完全加括号的最优方式是在Ak与Ak+1之间被分裂，设m\[i,j\]表示计算Ai...j所需的最小计算次数。m\[i,j\] = min{m\[i,k\]+m\[k+1,j\]+p(i-1)\*p(k)\*p(j) }
7.  系列问题
    1.  Best Time to Buy Stock
        1.  [best-time-to-buy-and-sell-stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock): 只能交易一次, 扫描维护当前最小价格和最大profit即可; 
        2.  [best-time-to-buy-and-sell-stock-ii](https://leetcode.com/articles/best-time-to-buy-and-sell-stock-ii): 无限次交易, 每次低买高卖即可
        3.  [best-time-to-buy-and-sell-stock-iii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/): 允许最多2次交易, 相当于两次问题1), dp\[i\]先记录\[0,i\]交易一次的最大profit, 再从right开始添加\[i+1:n-1\]交易一次的最大值, 最大和即为解
        4.  [best-time-to-buy-and-sell-stock-iv](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/): DP, t(i,j) is the max profit for up to i transactions by time j (0<=i<=K, 0<=j<=T).
        5.  [best-time-to-buy-and-sell-stock-with-transaction-fee](https://leetcode.com/articles/best-time-to-buy-and-sell-stock-with-transaction-fee): cash和hold两种状态, 状态间相互转移
        6.  [best-time-to-buy-and-sell-stock-with-cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/): sell, buy, prev\_sell, prev\_buy四种状态相互转移.
8.  游戏/概率问题:
    1.  [out-of-boundary-paths](https://leetcode.com/problems/out-of-boundary-paths/description/)
    2.  [knight-probability-in-chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/description/)
    3.  [soup-servings/](https://leetcode.com/problems/soup-servings/description/)
    4.  (以下均是计数或求概率问题, 递归配合memo, 比较方便易懂)
    5.  [out-of-boundary-paths](https://leetcode.com/problems/out-of-boundary-paths/description/)
    6.  [knight-probability-in-chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/description/)
    7.  [new-21-game](https://leetcode.com/problems/new-21-game/description/)
    8.  [knight-dialer](https://leetcode.com/problems/knight-dialer/description/)
    9.  [android-unlock-patterns](https://leetcode.com/problems/android-unlock-patterns/description/): 预编译可能的行动路线, 递归+memo执行
    10.  随机机器人: 有一条无限长的纸带,分割成一系列的格子,最开始所有格子初始是白色。现在在一个格子上放上一个萌萌的机器人(放上的这个格子也会被染红),机器人一旦走到某个格子上,就会把这个格子涂成红色。现在给出一个整数n,机器人现在会在纸带上走n步。每一步,机器人都会向左或者向右走一个格子,两种情况概率相等。机器人做出的所有随机选择都是独立的。现在需要计算出最后纸带上红色格子的期望值。
        1.  \# 1. dp\[i\]\[j\] means the expected times that the robot end at j after move i steps.
        2.  \# 2. dp\[0\]\[n\] = 1, dp\[i\]\[j\] = 0 if abs(n-j) > i, dp\[i\]\[j\] = 0.5^i if abs(n-j) = i
        3.  \# 3. dp\[i\]\[j\] = 0.5 \* dp\[i-1\]\[j-1\] + 0.5 \* dp\[i-1\]\[j+1\]
        4.  
        5.  n = 5
        6.  dp = \[\[0\] \* (2\*n+1) for \_ in xrange(n+1)\]
        7.  dp\[0\]\[n\] = 1
        8.  for i in xrange(1, n+1):
        9.      for j in xrange(2\*n+1):
        10.          left = 0.5 \* dp\[i-1\]\[j-1\] if j >= 1 else 0
        11.          right = 0.5 \* dp\[i-1\]\[j+1\] if j + 1 <= 2 \* n else 0
        12.          dp\[i\]\[j\] = dp\[i-1\]\[j\] + left + right
    11.  约瑟夫环问题: 假设下标从0开始，0，1，2 .. m-1共m个人，从1开始报数，报到k则此人从环出退出，问最后剩下的一个人的编号是多少？
        *   现在假设m=10, k=3, 初始序列为0 1 2 3 4 5 6 7 8 9
        *   第一个人出列后的序列为：0 1 3 4 5 6 7 8 9,  即: 3 4 5 6 7 8 9 0 1（\*）
        *   我们把该式转化为: 0 1 2 3 4 5 6 7 8 (\*\*)
        *   则你会发现: （(\*\*)+3) %10则转化为(\*)式了
        *   也就是说，我们求出9个人中第9次出环的编号，最后进行上面的转换就能得到10个人第10次出环的编号了
        *   设f(m,k,i)为m个人的环，报数为k，第i个人出环的编号，则f(10,3,10)是我们要的结果
        *   当i=1时，  f(m,k,i) = (m+k-1)%m
        *   当i!=1时，  f(m,k,i)= ( f(m-1,k,i-1)+k )%m
9.  2D数组pattern查找问题
    *   [largest-plus-sign](https://leetcode.com/problems/largest-plus-sign/description/): 1) DP记录四个方向, 检查每个’1'点, 去上下左右最小; 2) Binary Search
    *   [bomb-enemy](https://leetcode.com/problems/bomb-enemy/description/)
10.  Advanced Problems:
    1.  [[双向DP - cherry pickup|双向DP - cherry pickup]]
        1.  比如[cherry-pickup](https://leetcode.com/problems/cherry-pickup/description/), grid的每个cell表示这块区域的cherry量, 从(0,0)出发摘取cherry, 向下或向右到(n-1, n-1), 再向上向左返回(0,0), 求最大可摘取的cherry数量.
    2.  [find-the-shortest-superstring](https://leetcode.com/problems/find-the-shortest-superstring/description/): Given an array A of strings, find any smallest string that contains each string in A as a substring.
        1.  def shortestSuperstring(self, A):
        2.   # credit to https://leetcode.com/problems/find-the-shortest-superstring/discuss/195077
        3.   # construct a directed graph
        4.   #   node i => A\[i\]
        5.   #   weights are represented as an adjacency matrix:
        6.   #   shared\[i\]\[j\] => length saved by concatenating A\[i\] and A\[j\]
        7.   n = len(A)
        8.   shared = \[\[0\] \* n for \_ in range(n)\]
        9.   for i in range(n):
        10.   for j in range(n):
        11.   for k in range(min(len(A\[i\]), len(A\[j\])), -1, -1):
        12.   if A\[i\]\[-k:\] == A\[j\]\[:k\]:
        13.   shared\[i\]\[j\] = k
        14.   break
        15.  
        16.   # The problem becomes finding the shortest path that visits all nodes exactly once, which is a [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem).
        17.   # Brute force DFS would take O(n!) time.
        18.   # A DP solution costs O(n^2 2^n) time.
        19.   #
        20.   # Let's consider integer from 0 to 2^n - 1.
        21.   # Each i contains 0-n 1 bits. Hence each i selects a unique set of strings in A.
        22.   # Let's denote set(i) => {A\[j\] | j-th bit of i is 1}
        23.   # dp\[i\]\[k\] => shortest superstring of set(i) ending with A\[k\]
        24.   #
        25.   # e.g.
        26.   #   if i = 6 i.e. 110 in binary. dp\[6\]\[k\] considers superstring of A\[2\] and A\[1\].
        27.   #   dp\[6\]\[1\] => the shortest superstring of {A\[2\], A\[1\]} ending with A\[1\].
        28.   #   For this simple case dp\[6\]\[1\] = concatenate(A\[2\], A\[1\])
        29.   dp = \[\[''\] \* 12 for \_ in range(1 << 12)\]
        30.   for i in range(1 << n):
        31.   for k in range(n):
        32.   # skip if A\[k\] is not in set(i)
        33.   if not (i & (1 << k)):
        34.   continue
        35.   if i == 1 << k: # if set(i) == {A\[k\]}
        36.   dp\[i\]\[k\] = A\[k\]
        37.   continue
        38.   for j in range(n):
        39.   if j == k: continue
        40.   if i & (1 << j):
        41.   # the shortest superstring if we remove A\[k\] from the set(i)
        42.   s = dp\[i ^ (1 << k)\]\[j\]
        43.   s += A\[k\]\[shared\[j\]\[k\]:\]
        44.   if dp\[i\]\[k\] == '' or len(s) < len(dp\[i\]\[k\]):
        45.   dp\[i\]\[k\] = s
        46.  
        47.   min\_len = float('inf')
        48.   result = ''
        49.  
        50.   # find the shortest superstring of all candidates ending with different string
        51.   for i in range(n):
        52.   s = dp\[(1 << n) - 1\]\[i\]
        53.   if len(s) < min\_len:
        54.   min\_len, result = len(s), s
        55.   return result




----

- Date: 2018-10-03
- Tags: #Interview/Programing 



