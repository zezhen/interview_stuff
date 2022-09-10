# Array Problem
----



1.  子数组问题
    1.  连续子数组
        1.  [contiguous-array](https://leetcode.com/problems/contiguous-array): 0/1数组, 求最长0/1相同的连续子数组
        2.  [continuous-subarray-sum](https://leetcode.com/problems/continuous-subarray-sum/description/): 非负数组, 是否存在连续数组和为K.
        3.  [subarray-sum-equals-k](https://leetcode.com/problems/subarray-sum-equals-k): 连续子数组和为K, 多少种可能性.
        4.  [maximum-size-subarray-sum-equals-k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k): 最长的连续子数组和为K.
        5.  [binary-subarrays-with-sum](https://leetcode.com/problems/binary-subarrays-with-sum/description/)
            1.  以上5个方法解法类似, 从index=0开始accumulate, 然后记录acc值到hashmap中
            2.  当访问index=i时, 检查hashmap, 如果存在j, 则\[j, i\]为满足条件的连续子数组.
        6.  [subarray-sums-divisible-by-k](https://leetcode.com/problems/subarray-sums-divisible-by-k/): 与上几题基本相同, 唯一区别是acc % K记录到hashmap中
        7.  [subarray-product-less-than-k](https://leetcode.com/problems/subarray-product-less-than-k): 给定正数数组, 求乘积小于K的连续子数组个数.
            1.  左右指针l -> r, 个数 = r - l
        8.  [maximum-length-of-repeated-subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/): 两个数组最长的公共子数组. 类似最长公共子串DP问题
        9.  [minimum-size-subarray-sum/](https://leetcode.com/problems/minimum-size-subarray-sum/): 找最短subarray, 其sum>target, 左右两个pointer, 一增一减
        10.  [maximum-subarray](https://leetcode.com/problems/maximum-subarray): DP思想, 依次扫描, \_sum + a\[i\] > 0则继续, 记录\_max = max(\_max, \_sum), <=0, 则reset. [Kadane Algorithm](http://theoryofprogramming.com/2016/10/21/dynamic-programming-kadanes-algorithm/)
        11.  [number-of-subarrays-with-bounded-maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum): 求连续子数组的最大值在\[L, R\]区间内的个数
            1.  public int numSubarrayBoundedMax(int\[\] A, int L, int R) {
            2.      int j=0,count=0,res=0;    # j is the start pointer of subarray,
            
            4.      for(int i=0;i<A.length;i++){
            5.          if(A\[i\]>=L && A\[i\]<=R){
            6.              res+=i-j+1;      # there are i-j+1 subarray ending at i
            7.              count=i-j+1;    # record for next check
            8.          }
            9.          else if(A\[i\]<L){     # A\[i\] < L relay on the previous L<=A\[k\]<=R, subarray \[k,i\] is not in consideration.
            10.              res+=count;
            11.          }
            12.          else{                   # for the number > R is a barrier, move j and reset count
            13.              j=i+1;
            14.              count=0;
            15.          }
            16.      }
            17.      return res;
            18.  }
        12.  [count-of-range-sum](https://leetcode.com/problems/count-of-range-sum/description/): 给定整数数组, 求满足和在\[lower, upper\]范围内的连续子数组个数.
            1.  def countRangeSum(self, nums, lower, upper):
            2.      if not nums or lower > upper: return 0
            3.  
            4.      # for nums\[i\], suppose exists index j that make lower <= S(i, j) <= upper
            5.      # then we can get lower <= S(0, j) - S(0, i-1) <= upper, we can pre-compute S(0, k)
            6.      # S(0, j) - upper <= S(0, i-1) <= S(0, j) - lower,
            7.      # so we need to maintain an ordered struct and binary search for the range
            
            9.      acc = {-1:0}
            10.      for i in xrange(len(nums)):
            11.          acc\[i\] = acc\[i-1\] + nums\[i\]
            12.  
            13.      queue = \[0\] # left boundary
            14.      ans = 0
            15.      for i in xrange(len(nums)):
            16.          l = bisect.bisect\_left(queue, acc\[i\] - upper)
            17.          # print acc\[i\] - upper, queue, l
            18.          if l < len(queue):
            19.              r = bisect.bisect(queue, acc\[i\] - lower)
            20.              ans += (r - l)
            21.          bisect.insort(queue, acc\[i\])    # O(n), need to switch to SortedList
            22.  
            23.      return ans
    2.  (非连续)子序列
        1.  [distinct-subsequences](https://leetcode.com/problems/distinct-subsequences/description/): 给定字符串S和T, 求T在S中出现的次数, 如S = "babgbag", T = “bag”, output=5
            1.  DP问题, dp\[i\]\[j\] means the subsequence number of (S\[i:\], T\[j:\]), where S\[i\] = T\[j\]
        2.  [distinct-subsequences-ii](https://leetcode.com/problems/distinct-subsequences-ii): 给定字符串S, 求S中所有unique subsequence个数.
            1.  endswith\[i\] to count how many sub sequence that ends with ith character.
            2.  endswith\[i\] = sum(endswith) + 1
2.  数组 partition问题
    1.  [partition-labels](https://leetcode.com/problems/partition-labels): 给定字符串S, 将其分组成多个partition, 使得每个字符只存在于一个partition中.
        *   hashmap记录字符最左最右位置, 从index=0开始, 计算当前所能覆盖范围, i <= cover即可得到一个partition
        *   类似jump-game问题
    2.  [max-chunks-to-make-sorted](https://leetcode.com/problems/max-chunks-to-make-sorted): 将数组\[1...n\]分成多个chunk, chunk内排序就可以得到全局有序.
        *   max(chunk\[i\]) < min(chunk\[j\]), 两个指针s表示当前位置, 与当前数字nums\[s\]以及end(当前cover最远位置)比较
    3.  [max-chunks-to-make-sorted-ii](https://leetcode.com/problems/max-chunks-to-make-sorted-ii): 在上例的基础上, 不限制数组元素范围, 可重复
        *   用min\_right记录右侧最大数字
        *   从index=0开始, 如果cur\_max < min\_right\[i\]即可为一个chunk
    4.  [partition-array-into-disjoint-intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals): 将数组一分为二, 左边元素都小于右边.
        1.  建立两个数组: 左最大, 右最小, 然后找到第一个left\_max\[i\] <= right\_min\[i\]
    5.  [partition-equal-subset-sum](https://leetcode.com/problems/partition-equal-subset-sum/description/): 给定非空正数数组, 将其分成等和的子数组
        1.  首先检查数组长度和sum(nums) % 2 == 0?, 然后找到k个数使其和为target=sum / 2
        2.  两种方法: 方法1比较耗时, 方法2比较耗空间
            1.  order the array and solve it 0/1 knapsack way, use memo to maintain duplicated sub-space.
            2.  dp\[i\]\[j\] means whether the specific target j can be gotten from the first i numbers
                1.  dp\[0\]\[0\] = true,
                2.  dp\[i\]\[j\] = dp\[i-1\]\[j\] || (dp\[i-1\]\[j - nums\[j\]\] if j > nums\[j\] else False)
    6.  [partition-to-k-equal-sum-subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/): 将数组分成k个等和的子数组
        1.  public boolean canPartitionKSubsets(int\[\] nums, int k) {
        2.      int sum = 0;
        3.      for(int num:nums)sum += num;
        4.      if(k <= 0 || sum%k != 0)return false;
        5.      int\[\] visited = new int\[nums.length\];
        6.      return canPartition(nums, visited, 0, k, 0, 0, sum/k);
        7.  }
        8.  public boolean canPartition(int\[\] nums, int\[\] visited, int start\_index, int k, int cur\_sum, int cur\_num, int target){
        9.      if(k==1)return true;
        10.      if(cur\_sum == target && cur\_num>0) return canPartition(nums, visited, 0, k-1, 0, 0, target);
        11.      for(int i = start\_index; i<nums.length; i++){
        12.          if(visited\[i\] == 0){
        13.              visited\[i\] = 1;
        14.              if(canPartition(nums, visited, i+1, k, cur\_sum + nums\[i\], cur\_num++, target)) return true;
        15.              visited\[i\] = 0;
        16.          }
        17.      }
        18.      return false;
        19.  }
        20.  def canPartitionKSubsets(self, nums, k):  # assign number to buckets, refer to here
        21.      if sum(nums) % k != 0: return False
        22.  
        23.      buckets = \[0\]\*k
        24.      target = sum(nums) / k
        25.      nums.sort(reverse=True) # starting with bigger ones makes it faster
        26.      l = len(nums)
        
        28.      def walk(i):
        29.          if i == l:
        30.              return len(set(buckets)) == 1
        31.          for j in xrange(k):
        32.              buckets\[j\] += nums\[i\]
        33.              if buckets\[j\] <= target and walk(i+1):
        34.                  return True
        35.              buckets\[j\] -= nums\[i\]
        36.              if buckets\[j\] == 0: # we always start from first bucket, so no need to try following empty buckets
        37.                  break
        38.          return False        
        
        40.      return walk(0)
    7.  ==partition into equal sum subsets==
3.  查找问题
    1.  2D二维数组查找: 每行从左到右，每列从上到下递增的二维数组中，判断某个数是否存在
        *   从右上角的数开始, if 等于Target, 结束, 小于Target, 跳过这一行, 如果大于Target, 跳过这一列, 重复执行 (每次跳过一行或一列)
        *   [search-a-2d-matrix](https://leetcode.com/problems/search-a-2d-matrix/description/), [search-a-2d-matrix-ii](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)
        *   [kth-smallest-element-in-a-sorted-matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/): 找到数组中第k小的数? [details refer to leetcode discussion](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code)
            1.  用heap, 保留数字所在位置(v, i, j), 从最小的数字开始寻找下一个
            2.  binary search base on range, low = matrix\[0\]\[0\], high = max\[n-1\]\[m-1\]
    2.  旋转数组: 把递增数组开头的几个数字移动到数组的末尾，成为数组的旋转，找到数组中最小的数字
        *   [find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array): 无重复数字
            1.  int findMin(vector<int> &num) {
            2.      int start=0,end=num.size()-1;
            3.      while (start<end) {
            4.          if (num\[start\]<num\[end\]) return num\[start\];
            5.  
            6.          int mid = (start+end)/2;
            7.          if (num\[mid\]>=num\[start\]) {
            8.              start = mid+1;
            9.          } else {
            10.              end = mid;
            11.          }
            12.      }
            13.      return num\[start\];
            14.  }
        *   [find-minimum-in-rotated-sorted-array-ii](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii): 在上例基础上, 可重复数字, 当mid = nums\[0\]如何处理?
            1.  int findMin(vector<int> &num) {
            2.      int lo = 0;
            3.      int hi = num.size() - 1;
            4.      int mid = 0;
            5.      while(lo < hi) {
            6.          mid = lo + (hi - lo) / 2;
            
            8.          if (num\[mid\] > num\[hi\]) {
            9.              lo = mid + 1;
            10.          }
            11.          else if (num\[mid\] < num\[hi\]) {
            12.              hi = mid;
            13.          }
            14.          else { // when num\[mid\] and num\[hi\] are same, 
            15.              hi--;  //  we couldn't sure the position of minimum in mid's left or right, so just let upper bound reduce one
            16.          } 
            17.      }
            18.      return num\[lo\];
            19.  }
        *   [search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array)
            1.  interesting的方案是利用findMin找到最小的位置, 然后利用带位移的普通二分查找找到target
            2.  there four scenarios: minimum, mid and target in different positions, -inf or inf is used for certain comparison result.
                1.  int search(vector<int>& nums, int target) {
                2.      int lo = 0, hi = nums.size();
                3.      while (lo < hi) {
                4.          int mid = (lo + hi) / 2;
                5.          double num = (nums\[mid\] < nums\[0\]) == (target < nums\[0\])
                6.                     ? nums\[mid\]
                7.                     : target < nums\[0\] ? -INFINITY : INFINITY;
                
                9.          if (num < target)
                10.              lo = mid + 1;
                11.          else if (num > target)
                12.              hi = mid;
                13.          else
                14.              return mid;
                15.      }
                16.      return -1;
                17.  }
        *   [search-in-rotated-sorted-array-ii](https://leetcode.com/problems/search-in-rotated-sorted-array-ii)
            
            *   在上例的基础上增加重复数字, 类似find-minimum-in-rotated-sorted-array-ii中, 对于重复情况, 需要调整指针. refer to [discuss](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28218)
            
            1.  bool search(vector<int>& nums, int target) {
            2.      int left = 0, right =  nums.size()-1, mid;
            
            4.      while(left<=right)
            5.      {
            6.          mid = (left + right) >> 1;
            7.          if(nums\[mid\] == target) return true;
            8.  
            9.   // the only difference from the first one, trickly case, just updat left and right
            10.   if( (nums\[left\] == nums\[mid\]) && (nums\[right\] == nums\[mid\]) ) {++left; --right;}
            11.  
            12.          else if(nums\[left\] <= nums\[mid\])
            13.          {
            14.              if( (nums\[left\]<=target) && (nums\[mid\] > target) ) right = mid-1;
            15.              else left = mid + 1;
            16.          }
            17.          else
            18.          {
            19.              if((nums\[mid\] < target) &&  (nums\[right\] >= target) ) left = mid+1;
            20.              else right = mid-1;
            21.          }
            22.      }
            23.      return false;
            24.  }
    3.  数组的中位数
        1.  两个有序数组的中位数 [median-of-two-sorted-arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/): 
            
            *   refer to [discuss](https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481)
            *   
            *   we need find a split i for A and j for B that
            *   1\. i + j (left part) == m - i + n - j (or m - i + n - j + 1)  (right part)
            *       => assume n >= m, search i in \[0,m\], j = (m+n+1) / 2 - i
            *       => if m >= n, switch A and B, to make sure j >= 0
            *   2\. B\[j-1\] <= A\[i\] and A\[i-1\] <= B\[j\] (left part <= right part)
            *   
            *   so the problem is to find the right i, meets above two conditions.
            *   
            *   boundary scenarios:
            *   i == 0: the max of left is B\[j-1\]
            *   j == 0: the max of left is A\[i-1\]
            *   i == m: the min of right is B\[j\]
            *   j == n: the min of right is A\[i\]
            *   
            *   if m+n is odd: return max of left
            *   else return average of max of left + min of right
            *   
            
            1.  def findMedianSortedArrays(self, nums1, nums2):
            2.      m, n = len(A), len(B)
            3.      if m > n:
            4.          A, B, m, n = B, A, n, m
            5.      if n == 0:
            6.          raise ValueError
            7.  
            8.      imin, imax, half\_len = 0, m, (m + n + 1) / 2
            9.      while imin <= imax:
            10.          i = (imin + imax) / 2
            11.          j = half\_len - i
            12.          if i < m and B\[j-1\] > A\[i\]:
            13.              # i is too small, must increase it
            14.              imin = i + 1
            15.          elif i > 0 and A\[i-1\] > B\[j\]:
            16.              # i is too big, must decrease it
            17.              imax = i - 1
            18.          else:
            19.              # i is perfect
            20.  
            21.              if i == 0: max\_of\_left = B\[j-1\]
            22.              elif j == 0: max\_of\_left = A\[i-1\]
            23.              else: max\_of\_left = max(A\[i-1\], B\[j-1\])
            24.  
            25.              if (m + n) % 2 == 1:
            26.                  return max\_of\_left
            27.  
            28.              if i == m: min\_of\_right = B\[j\]
            29.              elif j == n: min\_of\_right = A\[i\]
            30.              else: min\_of\_right = min(A\[i\], B\[j\])
            31.  
            32.              return (max\_of\_left + min\_of\_right) / 2.0
        2.  一次性无序 [kth-largest-element-in-an-array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)
            1.  最小堆, O(nlogk)
            2.  快排, 然后找中间数 T: O(n\*logn)
            3.  分治类快排: 随机找一个点作为支点, 将集合划分两块, 比较左右两侧集合长度, 决定下一次分治; 最好T:O(n), 最差T:O(n^2), 期望T: O(n)
            4.  线性查找: <算法导论>p112
        3.  支持动态增加
            1.  维持一个最大堆或最小堆
            2.  红黑树: Java TreeSet/TreeMap, Python SortedList/SortedSet/SortedDict
    4.  索引数值数组: A zero-indexed array A of length N contains all integers from 0 to N-1
        1.  [find-all-duplicates-in-an-array](https://leetcode.com/problems/find-all-duplicates-in-an-array)
        2.  [find-all-numbers-disappeared-in-an-array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array)
        3.  [set-mismatch](https://leetcode.com/problems/set-mismatch)
            *   在\[1-n\]中找出重复的/缺失的数
        4.  [find-the-duplicate-number](https://leetcode.com/problems/find-the-duplicate-number): 不得修改array以查找duplicated number, 从别处copy的解法, 采用链表找环的方式, 挺有新意.
        5.  [first-missing-positive](https://leetcode.com/problems/first-missing-positive/description/): Given an unsorted integer array, find the smallest missing positive integer. O(n) time, O(1) space
            1.  扫描插入法, 丢弃大于长度的n的整数, 将整数i插入到位置i上, 最后线性扫描一遍
            2.  follow up: 如果是有序数组则按二分查找, 比较A\[i\]和i的大小以决定往左or右
    5.  众数
        1.  大于一半, 用堆结构抵消法, 加入元素与堆顶相同则加入, 否则消除堆顶
        2.  随机个数, 用hashmap
    6.  "一步千里": 有这样一个数组A，大小为n，相邻元素差的绝对值都是1。如：A={4,5,6,5,6,7,8,9,10,9}。现在，给定A和目标整数y，请找到y在A中的位置。除了依次遍历，还有更好的方法么？
        *   设数组A长度为n, x = A\[0\], d=y-x (假设y>x), 则y只可能出现在\[d, n\]的位置上, 如果d>n, 则结束, 小于d的位置都只可能小于y
        *   所以检测A\[d\], 如果A\[d\]=y, 结束, A\[d\] < y, 则以d为新的数组起点, 重复第一步
4.  [[BitManipulation 计数问题.md|BitManipulation 计数问题]]
5.  加减运算问题
    1.  求数组中两数/三数/k数和为目标值
        1.  2Sum: 排序+左右扫描 O(N logN)
        2.  3Sum
            *   a + b + c = target: 排序+固定a左右扫描 O(N^2)
            *   a + b + c = 0: 习惯采用上面方法, 假设a<b<c, 则a必为负数或0, 参考[3Sum](https://leetcode.com/problems/3sum/description/)最优解, 它首先锁定b和c的范围, 在进行搜索.
            *   [3Sum Closest](https://leetcode.com/problems/3sum-closest): a + b + c closest to target: 类似上例方法
            *   [3Sum Smaller](https://leetcode.com/problems/3sum-smaller): a + b + c < target.
            *   [3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity)==:== 有重复数字的数组, 求三数和为K有多少种.
                *   先统计数字出现次数, 然后类似普通3Sum, 同时计算次数
        3.  [4Sum](https://leetcode.com/problems/4sum/description/)
            *   a + b + c + d = target: 排序+依次固定a, b, 然后左右扫描c,d, 和最优解的差别主要在于以前判断, 比如排序后前四数和>target或后四数和<target, 以及固定a的提前判断等
            *   [4Sum II](https://leetcode.com/problems/4sum-ii) 4个数组中各选一数, 和为0
                1.  def fourSumCount(self, A, B, C, D):
                2.      AB = collections.Counter(a+b for a in A for b in B)
                3.      return sum(AB\[-c-d\] for c in C for d in D)
        4.  k数: back tracking + memorization
6.  数组合并/交换问题
    
    1.  [maximum-swap](https://leetcode.com/problems/maximum-swap/description/): 给定非负整数, 交换一堆数字构成最大值
        *   find the first digit that has a larger number at right
    2.  [Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle): 两数组田忌赛马问题, A over B
        *   最优解比较A和B的剩余最大, 如果A胜出则成对, 反之则用A剩余最小匹配.
    3.  [create-maximum-number](https://leetcode.com/problems/create-maximum-number/description/): given two arrays A and B with digits 0-9, create the maximum number of length k <= m + n from the two arrays. The relative order of the digits from the same array must be preserved.
        1.  基本事项是从A和B中分别取出top i和k-i个数, 然后merge, 尝试多次, 有很多细节.
        2.  def maxNumber(self, nums1, nums2, k):
        3.      def merge(arr1, arr2):
        4.          ans = \[\]
        5.          i = j = 0
        6.          while i < len(arr1) and j < len(arr2):
    
    1.              if arr1\[i\] > arr2\[j\] or arr1\[i\] == arr2\[j\] and arr1\[i:\] > arr2\[j:\]: # choose the bigger one
    2.                  ans.append(arr1\[i\])
    3.                  i += 1
    4.              else:
    5.                  ans.append(arr2\[j\])
    6.                  j += 1
    7.          if i < len(arr1): ans.extend(arr1\[i:\])
    8.          if j < len(arr2): ans.extend(arr2\[j:\])
    9.          return ans
    10.  
    11.      def largest(array, k):
    12.          if len(array) <= k: return array
    13.          if k == 0: return \[\]
    14.          ans, stack = \[\], \[array\[0\]\]
    15.          for i in xrange(1, len(array)):
    16.              while stack and array\[i\] > stack\[-1\] and len(array) - i + len(stack) > k:  # continue pop if k size is guaranteed
    17.                  stack.pop()
    18.              stack.append(array\[i\])
    19.          return stack\[:k\]
    20.  
    21.   candidate1 = largest(nums1, k) # pre-build top K candidates, otherwise need to scan whole array every time
    22.   candidate2 = largest(nums2, k)
    23.      ans = \[\]
    24.      for i in xrange(min(k, len(nums1))+1):
    25.          j = k - i
    26.          if j > len(nums2): continue
    27.  
    28.          arr1 = largest(candidate1, i)
    29.          arr2 = largest(candidate2, j)
    30.          ans = max(ans, merge(arr1, arr2))
    31.  
    32.      return ans
    
7.  容器/面积问题
    *   [container-with-most-water](https://leetcode.com/problems/container-with-most-water): 非负数组 a1,a2,…,an, ak表示在位置k上的柱子, 求问二维平面上构成最大container的两个柱子i,j面积
        1.  def maxArea(self, height):
        2.      i, j = 0, len(height)-1
        3.      maxA = 0
        4.      while i < j:
        5.          maxA = max(maxA, (j-i)\*min(height\[i\], height\[j\]))
        6.          if height\[i\] <= height\[j\]:
        7.              i += 1
        8.          else:
        9.              j -= 1
        10.      return maxA
    *   [trapping-rain-water](https://leetcode.com/problems/trapping-rain-water/description/): Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
        
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
    *   [trapping-rain-water-ii](https://leetcode.com/problems/trapping-rain-water-ii)
        1.  应用同样思路, #1中的左右两指针变成了外围一圈, 指针所有移动变成移动到周围邻居, 因此需要一个priority queue来维护lower, 总是取最小的格子, 然后更新起周边. 这个[视频](https://www.youtube.com/watch?v=cJayBq38VYw%0A)非常好的展示整个过程
    *   [maximum-subarray](https://leetcode.com/problems/maximum-subarray): 最大连续子数组和
        1.  [Kadane Algorithm](http://theoryofprogramming.com/2016/10/21/dynamic-programming-kadanes-algorithm/) DP: sum\[i\] = max(nums\[i\], nums\[i\] + sum\[i-1\]), 
        2.  def kadane\_max\_subarray(nums):
        3.      globalMax = curMax = nums\[0\]
        4.      for i in xrange(1, len(nums)):
        5.          curMax = max(nums\[i\], nums\[i\] + curMax)
        6.          globalMax = max(globalMax, curMax)
        7.      return globalMax
    *   maximum sum rectangular submatrix in matrix: 二维矩阵最大子数组(rectangle)和
        1.  def maxSumRect(matrix): # O(n\* m^2), if m > n, transpose the matrix
        2.      n, m = len(matrix), len(matrix\[0\])
        3.      maxSum = float('-inf’)
        4.      for l in xrange(m):
        5.          acc = \[0\] \* n
        6.          for r in xrange(l, m):
        7.              for i in xrange(n): acc\[i\] += matrix\[i\]\[r\]
        8.              curMax = kadane\_max\_subarray(acc)
        9.              maxSum = max(maxSum, curMax)
        10.      return maxSum
    *   [max-sum-of-rectangle-no-larger-than-k](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k): 如上增加最大K的限制
        1.  from sortedcontainers import SortedList
        2.  def max\_subarray\_less\_than\_k(nums, k):  # replace function kadane\_max\_subarray in above problems
        3.      maxSum, acc = float(‘-inf’), 0
        4.      sl = SortedList(\[0\])
        5.      for n in nums:
        6.          acc += n
        7.          i = sl.bisect\_left(acc - k)
        8.          if i < len(sl):
        9.              maxSum = max(maxSum, acc - sl\[i\])
        10.          sl.add(acc)
        11.      return maxSum
    *   [largest-rectangle-in-histogram](https://leetcode.com/problems/largest-rectangle-in-histogram): 数组表示histogram高度, 求组成的最大rectangle面积
        1.  There are two solutions:
        2.  对于histogram i, 如果存在boundary l, r, 中间所有的h\[k\] >= h\[i\], area = h\[i\] \* (r - l + 1)
        3.  最naive的方法是从i往两边扫O(n^2); maintain 两个数组 leftFirstLess和rightFirstLess, 保留左/右第一个小于h\[i\]的index, O(n)
        4.  def largestRectangleArea(self, heights):
        5.      n = len(heights)
        6.      leftFirstLess, rightFirstLess = \[0\] \* n, \[0\] \* n
        7.      leftFirstLess\[0\], rightFirstLess\[-1\] = -1, n     # set boundary
        8.  
        9.      for i in xrange(1, n): 
        10.          p = i - 1
        11.          while p >= 0 and heights\[p\] >= heights\[i\]:
        12.              p = leftFirstLess\[p\]      # jump to first index q that less that p, for all heights between (q,p\] is greater than i
        13.          leftFirstLess\[i\] = p
        14.  
        15.      for i in range(n-1)\[::-1\]:
        16.          p = i + 1
        17.          while p < n and heights\[p\] >= heights\[i\]:
        18.              p = rightFirstLess\[p\]
        19.          rightFirstLess\[i\] = p
        20.  
        21.      ans = 0
        22.      for i in xrange(n):
        23.          ans = max(ans, heights\[i\] \* (rightFirstLess\[i\] - leftFirstLess\[i\] - 1))
        24.      return ans
        25.  
        26.  def largestRectangleArea2(self, heights):
        27.      n, ans, stack = len(heights), 0, \[\]
        28.      i = 0
        29.      while i <= n:
        30.          h = heights\[i\] if i < n else 0
        31.          if not stack or h >= heights\[stack\[-1\]\]:
        32.              stack.append(i) # keep height\[i\] is increasing
        33.              i += 1
        34.          else:
        35.   # calculate the area for height\[j\], index r is the exclusive right boundary
        36.   # if stack is empty, that means all heights\[k\] > heights\[j\], thus pop out, width = i
        37.   # otherwise index stack\[-1\] is the left boundary as heights\[stack\[-1\]\] <= heights\[j\]
        38.   # height \* width is the area.
        39.   # if heights\[stack\[-1\]\] == heights\[j\], as i keep as current, next round will check stack\[-1\]
        40.              j = stack.pop()
        41.              width = i if not stack else (i - 1 - stack\[-1\])
        42.              ans = max(ans, heights\[j\] \* width)
        43.      return ans
    *   [maximal-rectangle](https://leetcode.com/problems/maximal-rectangle): 二维0/1数组中, 求1组成的最大rectangle面积
        1.  based on the solution from largestRectangleArea2 above but do more enhancement, more concise code
        2.  def maximalRectangle(self, matrix):
        3.      if not matrix or not matrix\[0\]:
        4.          return 0
        5.      n = len(matrix\[0\])
        6.      height = \[0\] \* (n + 1)
        7.      ans = 0
        8.      for row in matrix:
        9.          for i in xrange(n):
        10.              height\[i\] = height\[i\] + 1 if row\[i\] == '1' else 0 # height\[i\] will be k if there is continuous k size ‘1'
        11.   stack = \[-1\]    # so that stack won't be empty anymore, and height\[-1\] is always 0
        12.          for i in xrange(n + 1):
        13.   while height\[i\] < height\[stack\[-1\]\]:  # continue pop and calculate area
        14.   h = height\[stack.pop()\]
        15.   w = i - 1 - stack\[-1\]
        16.                  ans = max(ans, h \* w)
        17.              stack.append(i)
        18.      return ans
    *   [minimum-area-rectangle](https://leetcode.com/problems/minimum-area-rectangle): 给定二维平面上的点, 求点构成的最小rectangle的面积
        1.  def minAreaRect(self, points):
        2.      xgroup = collections.defaultdict(list)
        3.      for x,y in points:
        4.          xgroup\[x\].append(y)
        
        6.      ans, ycache = float('inf'), {}
        7.      for x in sorted(xgroup.keys()):
        8.          vals = xgroup\[x\]
        9.          for i in xrange(len(vals)):
        10.              for j in xrange(i+1, len(vals)):
        11.   if (vals\[i\], vals\[j\]) in ycache:    # caching for later check
        12.   ans = min(ans, abs(vals\[i\] - vals\[j\]) \* (x - ycache\[(vals\[i\], vals\[j\])\]))
        13.                  ycache\[(vals\[i\], vals\[j\])\] = x
        14.                  ycache\[(vals\[j\], vals\[i\])\] = x
        15.      return ans if ans < float('inf') else 0
    *   [perfect-rectangle](https://leetcode.com/problems/perfect-rectangle/description/): 给n个矩形, 问这些矩形是否构成完整的矩形, 而且没有重叠
        1.  我的解法需要记录最左右上下边角, 1) 比较面积, 2) 检查边角是否都存在, 3) 面积在x和y轴需要均匀分布. [here](https://leetcode.com/submissions/detail/202402251/)
        2.  如下解法: 1) 比较面积, 2) 比较边角, 精髓部分在于 corners ^= c(), perfect rectangle除了四个边角外, 其余所有点均是偶数次.
        3.  def isRectangleCover\_fastest(self, rectangles):
        4.      area,corners = 0,set()
        5.      a,c = lambda: (X-x)\*(Y-y),lambda: {(x,y),(x,Y),(X,y),(X,Y)}
        6.      for x,y,X,Y in rectangles:
        7.          area += a()
        8.   corners ^= c()    # all points except the corners in perfect rectangle occur even times.
        9.      x,y,X,Y = (f(z) for f,z in zip((min,min,max,max),zip(\*rectangles)))
        10.      return area==a() and corners==c()
    *   [the-skyline-problem](https://leetcode.com/problems/the-skyline-problem): 给定很多building (left, right, height), 有些有重叠, 从侧面看找出corner points, 相同高度给出最左边的点.
        1.  def **getSkyline**(self, buildings):
        2.      # credit to https://briangordon.github.io/2014/08/the-skyline-problem.html
        3.      # the basic idea is to record the building left/right corners, then scan from left most to right
        4.      # if enter a building, and its height higher than cur\_height, it become the new hight, otherwise omitted
        5.      # if leave a building, cur\_height ended, the next max height become new cur\_height, thus we need sorted list to record the heights
        6.      points = \[\]
        7.      for b in buildings:
        8.   **points.append((b\[0\], - b\[2\]))   # start**
        9.   **points.append((b\[1\], b\[2\]))     # end**
        10.      points.sort()
        11.  
        12.      ans = \[\]
        13.      pq = **SortedList**() # pq = \[\]
        
        15.      pq.add(0) # pq.append(0)
        16.      prev\_height = 0
        17.      for p in points:
        18.          if p\[1\] < 0:
        19.              pq.add(- p\[1\]) # pq.append(- p\[1\])
        20.          else:
        21.              pq.remove(p\[1\])
        
        23.          cur\_height = pq\[-1\] # cur\_height = max(pq)
        24.          if cur\_height != prev\_height:
        25.              ans.append(\[p\[0\], cur\_height\])
        26.              prev\_height = cur\_height
        27.      return ans
    *   [rectangle-area-ii](https://leetcode.com/problems/rectangle-area-ii): 二维平面上给定n个矩阵, 矩阵间可能有重叠, 求这些矩阵所覆盖的面积.
        1.  def **rectangleArea**(self, rectangles):
        2.      # credit to https://leetcode.com/problems/rectangle-area-ii/discuss/139835
        3.      # It's quite complicated to caculate the overlap, need to handle many scenarios
        4.      # It's similar as the skyline problem, which is to record the left/right boundary using 1/-1
        5.      # we can solve this problem using similar way.
        6.  
        7.      # first record the corners with 1/-1 for each rectangle
        8.      # we start from left most rectangle at lx, there might be one or more rectangles start from lx
        9.      # we have (lx, ly, 1), (lx, ry, -1), so we know the y length is ry - rx, keep a count,
        10.      # positive means we enter a rectangle area, zero means out of rectangle, we need to process y increasingly
        11.      # keep the total sum of y as preY
        12.  
        13.      # then move lx to right until meet the second x (preX = lx): x = lx' if overlap or x = rx if no overlap
        14.      # no matter which one, we already have area = (x - preX) \* preY
        15.      # then x become preX for next calculation, re-calculate preY.
        16.  
        17.      mod = 10\*\*9 + 7
        18.      points = \[\]
        19.      for lx,ly,rx,ry in rectangles:
        20.          points.append((lx, ly, 1))
        21.          points.append((lx, ry, -1))
        22.          points.append((rx, ly, -1))
        23.          points.append((rx, ry, 1))
        24.      points.sort(key=lambda (x,y,v): (x, -y))
        25.  
        26.      sd = SortedDict()  # sd = {}    # to keep the sorted y for x
        27.  
        28.      def calY():
        29.          ans, prev, count = 0, None, 0
        30.          for k, v in sd.iteritems():    # for k, v in sorted(sd.iteritems()):
        31.              if prev != None and count > 0:
        32.                  ans += k - prev
        33.              count += v  # after several iteration, some v become 0, we can either remove it or just ignore it
        34.              prev = k
        35.          return ans
        36.  
        37.      preX = preY = None
        38.      ans = 0
        39.      for i, (x, y, v) in enumerate(points):
        40.          sd\[y\] = sd.get(y, 0) + v
        41.          if i == len(points) - 1 or points\[i+1\]\[0\] > x:
        42.              if preX != None:
        43.                  ans += (x - preX) \* preY % mod
        44.              preX = x
        45.              preY = calY()
        46.      return ans % mod
8.  其他:
    1.  [random-point-in-non-overlapping-rectangles](https://leetcode.com/problems/random-point-in-non-overlapping-rectangles):
        1.  randomly pick a rectangle: calculate total area ’sum’, use random.randint(0, sum) to locate the rectangle.
        2.  randomly pick a point inside: left + randint(right-left+1), bot + randint(top - bot + 1)
    2.  把数组排列成最小的数
        1.  特定的大小方式, 不是数值上的对比, 而是排列后大小的对比, 记比较a和b, 改成比较ab和ba的大小
    3.  对数组的两个子有序段进行合并: 
        1.  寻找捣乱分子: 数组a中找出所有(a\[i\], a\[j\])对, a\[i\] > a\[j\] and i < j
            1.  采用size k的window进行合并排序, 逆序的对都满足条件, k从1->n/2
        2.  合并排序
    4.  计算两个有/无序整型数组的交集
        1.  有序: 先确定范围段, 二分查找两个数组中的起止位置, 然后依次比较
        2.  无序: Hash/分桶, 然后桶内比较
    5.  完美洗牌: 有个长度为2n的数组{a0,a1,a2,…,an-1,b0,b1,b2,…,bn-1}，希望排序后{a0,b0,a1,b1,....,an-1,bn-1}，请考虑有无时间复杂度o(n)，空间复杂度0(1)的解法
        1.  ai的最终位置在2i, bi的最终位置在2i+1, a1开始挪, 一次放置到目标位置, 被踢出来的元素挪到它的最终位置, 直到最后.







----

- Date: 2018-10-02
- Tags: #note #Interview/Programing 



