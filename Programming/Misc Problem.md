# Misc Problem
----

[https://en.wikipedia.org/wiki/Master\_theorem\_(analysis\_of\_algorithms](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))


*   Reservoir Sampling
    1.  [linked-list-random-node](https://leetcode.com/problems/linked-list-random-node): given a large linkedlist, how to getRandom() with same probability for all nodes.
        
        *   \# there are multiple solution for get one random number
        *   \# 1. copy linked list numbers to a array, random select from array
        *   \# 2. because linked list size is large, so scan list and get size n, random select number from \[1,n\], scan link again.
        *   \# 3. reservior sampling. very good explanation in below link, good to sampling k numbers, this is k = 1 problem. refer to [Brief-explanation-for-Reservoir-Sampling](https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling)
        
        1.  def \_\_init\_\_(self, head):
        2.      self.head = head
        
        4.  def getRandom(self):
        5.      node = self.head
        6.      ans = node.val
        7.      i = 1
        8.      while node.next:
        9.          node = node.next
        10.          if random.randint(i+1) == i:
        11.              ans = node.val
        12.          i += 1
        13.      return ans
*   Trapping Rain Water
    1.  [trapping-rain-water](https://leetcode.com/problems/trapping-rain-water/description/)
        
        *   我自己的思路是计算left\_max和right\_max, 然后每一格的积水量即为 max(0, height\[i\] - min(left\_max\[i\], right\_max\[i\]))
        *   这个思路在1D数组上运行还可以, 但扩展都2D就很麻烦; 
        *   更好的思路是维护一个level值表示当前可达到最低水位, 然后左右两指针进行比较, lower的一个即可保证 level - lower的水量, 更新lower所在指针
        
        1.  def trap(self, height):
        2.      if not height or len(height) == 0:
        3.          return 0
        4.      l = level = water = 0
        5.      r = len(height) - 1
        6.      lower = None
        
        8.      while l < r:
        9.          if height\[l\] < height\[r\]:
        10.              lower = height\[l\];
        11.              l += 1
        12.          else:
        13.              lower = height\[r\];
        14.              r -= 1
        15.          if lower > level:
        16.              level = lower
        17.          water += level - lower
        18.      return water
    2.  [trapping-rain-water-ii](https://leetcode.com/problems/trapping-rain-water-ii)
        1.  应用同样思路, #1中的左右两指针变成了外围一圈, 指针所有移动变成移动到周围邻居, 因此需要一个priority queue来维护lower, 总是取最小的格子, 然后更新起周边.
        2.  https://www.youtube.com/watch?v=cJayBq38VYw 非常好的展示整个过程
*   Overlap Check
    *   interval: A.left < B.right & A.right > B.left
    *   Rectangle: RectA.Left < RectB.Right && RectA.Right > RectB.Left && RectA.Top > RectB.Bottom && RectA.Bottom < RectB.Top
*   GCD: Greatest Common Divisor
    1.  def gcd(self, n, m):
    2.      while m != 0:
    3.          n, m = m, n % m
    4.      return n



Bloom Filter

随机生成和为S的N个正整数——投影法https://blog.csdn.net/MoreWindows/article/details/8439393

面试笔记整理 

1.  https://hit-alibaba.github.io/interview/
2.  http://www.fangheart.top/categories/%E7%AE%97%E6%B3%95/
3.  https://zhengjianglong.gitbooks.io/note-of-interview/content/
4.  https://wizardforcel.gitbooks.io/the-art-of-programming-by-july/content/index.html
5.  https://www.cnblogs.com/edisonchou/tag/%E5%89%91%E6%8C%87Offer/
6.  https://blog.csdn.net/derrantcm/article/details/46887821
7.  https://www.zhihu.com/question/19927564
8.  https://www.bookstack.cn/read/Way-to-Algorithm/docs-GraphTheory-Connectivity-Gabow.md


https://www.zhihu.com/question/24964987


有趣的问题


1.  稳定婚姻问题和Gale-Shapley算法
    *   参考http://www.matrix67.com/blog/archives/2976
2.  寻找第k个丑数. 丑数n的因子只有2,3,5.
    1.  def nthUglyNumber(self, n):
    2.      if n == 1:
    3.          return 1
    4.      primes = \[2, 3, 5\]
    5.      index = \[0 for i in range(len(primes))\]
    6.      uglyNums = \[1\]
    
    8.      while len(uglyNums) < n:
    9.          next = min(map(lambda (index,prime): uglyNums\[index\] \* prime, zip(index, primes)))
    10.          uglyNums.append(next)
    
    12.          for i,prime in enumerate(primes):
    13.              while uglyNums\[index\[i\]\] \* prime <= next:
    14.                  index\[i\] += 1
    
    16.      return uglyNums\[-1\]
3.  完美平方数[perfect-squares](https://leetcode.com/problems/perfect-squares/description/): Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
    
    1.  refer to [here](http://www.cnblogs.com/grandyang/p/4800552.html%0A)
    
    1.  def numSquares(self, n):  # Lagrange's four-square theorem
    2.      while n % 4 == 0:
    3.          n /= 4
    4.      if n % 8 == 7:
    5.          return 4
    6.      a = 0
    7.      while a \* a < n:
    8.          b = int(math.sqrt(n - a \* a))
    9.          if a\*a + b\*b == n:
    10.              return 2 if a\*b > 0 else 1
    11.          a += 1
    
    13.      return 3
    14.  
    15.  def numSquares\_dp(self, n):
    16.      dp = \[sys.maxint\] \* (n+1)
    17.      dp\[0\] = 0
    18.      for i in xrange(0,n+1):
    19.          j = 1
    20.          while i + j\*j <= n:
    21.              dp\[i+j\*j\] = min(dp\[i+j\*j\], dp\[i\] + 1)
    22.              j += 1
    
    1.      return dp\[n\]
4.  [洗牌程序 ShuffleArray](https://coolshell.cn/articles/8593.html)
    1.  Fisher\_Yates算法
        1.  void ShuffleArray\_Fisher\_Yates(char\* arr, int len)
        2.  {
        3.   int i = len, j;
        4.   char temp;
        5.   if ( i == 0 ) return;
        6.   while ( --i ) {
        7.   j = rand() % (i+1);
        8.   temp = arr\[i\];
        9.   arr\[i\] = arr\[j\];
        10.   arr\[j\] = temp;
        11.   }
        12.  }
    2.  手动洗牌算法
        1.  void ShuffleArray\_Manual(char\* arr, int len)
        2.  {
        3.   int mid = len / 2;
        
        5.   for (int n=0; n<5; n++){
        
        7.   //两手洗牌
        8.   for (int i=1; i<mid; i+=2){
        9.   char tmp = arr\[i\];
        10.   arr\[i\] = arr\[mid+i\];
        11.   arr\[mid+i\] = tmp;
        12.   }
        
        14.   //随机切牌
        15.   char \*buf = (char\*)malloc(sizeof(char)\*len);
        
        17.   for(int j=0; j<5; j++) {
        18.   int start= rand() % (len-1) + 1;
        19.   int numCards= rand()% (len/2) + 1;
        
        21.   if (start + numCards > len ){
        22.   numCards = len - start;
        23.   }
        
        25.   memset(buf, 0, len);
        26.   strncpy(buf, arr, start);
        27.   strncpy(arr, arr+start, numCards);
        28.   strncpy(arr+numCards, buf, start);
        29.   }
        30.   free(buf);
        
        32.   }
        33.  }
    3.  测试算法
        1.  统计每个元素在不同位置出现的次数/概率, 比如54张牌, 出现的概率约为1/54, 误差应该在5%以内
        2.  统计每一种排列出现的概率(需要更多样本), 出现概率相当, 误差应该在5%内
5.  N个球放入M个盒子
    1.  球同,   盒同,   无空箱 ( N > M )
        *   先往M个盒中, 各放一个球避免空盒, 则问题变成N-M个球, M盒, 可空箱情况(#2)
    2.  球同,   盒同,   可空箱
        *   问题变成了M个非负整数的和为N的组合数?
        *   ==穷举法? 杨辉三角?==
    3.  球同,   盒不同, 无空箱
        *   插拔法: N个球, N-1个空位, 去M-1个棍子放入空位组成M个区域, 可能性为C(N-1,M-1)
    4.  球同,   盒不同, 可空箱
        *   #3的变形, 先在空箱中各放一个球避免空箱, 然后再分配N个球, 可能性为C(N+M-1, M-1)
    5.  球不同, 盒相同, 无空箱
        1.  S(N,M) = S(N-1, M-1) + M \* S(N-1, M) + 0 \* S(N, M-1)
            1.  S(N-1, M-1)为N-1个球放入M-1个盒子无空箱的可能性, 变成N,M情况只需要添加一个盒子和1个球即可
                *   相当于从N个球中选择N-1个球, 放入M-1个盒子, 剩余的一个球放入剩余的一个盒子中.
                *   因为盒相同, 而S(N-1, M-1)中包含了任意个球在单独盒子的可能性, 所以无需乘以N-1
            2.  S(N-1, M)为N-1个球放入M个盒子无空箱的可能性, 在增加一个球有M种选择
            3.  S(N, M-1)为N个球放入M-1个盒子情况, 因为无空箱的规定, 所以该情况不存在
    6.  球不同, 盒相同, 可空箱
        *   #5的变形, 把N个求装到k个箱子中, 无空箱的情况, k从1到M
        *   S(N, 1) + S(N, 2) + S(N,3) + … + S(N, M)
    7.  球不同, 盒不同, 无空箱
        *   #5的基础上变成盒不同, 球的组合S(N,M) \* 盒的排列 M!
    8.  球不同, 盒不同, 可空箱
        *   每个球都有M种选择, 可能性为N^M
6.  
    1.  
    2.  


参考他人总结
https://mnmunknown.gitbooks.io/algorithm-notes/content/
https://wizardforcel.gitbooks.io/the-art-of-programming-by-july/content/01.01.html


----

- Date: 2018-10-03
- Tags: #note #Interview/Programing 



