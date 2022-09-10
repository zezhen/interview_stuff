# Binary Search Problem
----

The key point for any ==binary search== is to figure out the "Search Space". For me, I think there are two kind of "Search Space" -- index and range(the range from the smallest number to the biggest number). Most usually, when the array is sorted in one direction, we can use index as "search space", when the array is unsorted and we are going to find a specific number, we can use "range".
Let me give you two examples of these two "search space"

1.  index
    1.  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ ( the array is sorted)
2.  range
    1.  https://leetcode.com/problems/find-the-duplicate-number/ (Unsorted Array)
    2.  https://leetcode.com/problems/koko-eating-bananas/description/ (Hidden array, don’t look at the index BS only)






*   [smallest-rectangle-enclosing-black-pixels](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels): 在0/1二维数组中, 找出包含所有1的最小矩阵面积, 所有1都连续, 给定起始点为(x, y)=1
    1.  从(x,y)出发, dfs并记录最小最大边界即可
    2.  从(x, y)往左/上看是0001111, 往右/下看是1111000, 所以是可以二分查找每一行的left/right, 每一列的up/down
*   [largest-plus-sign](https://leetcode.com/problems/largest-plus-sign/description/): 在0/1二维数组中, 找到由1组成的最大十字长度
    1.  按row/col构造区域, 比如第i行没有1, 则row\[i\] = \[-1, N\], 如果matrix\[i\]\[3\]=1, row\[i\]=\[-1,3,N\], exclusive
    2.  然后逐行检查, 看区域大小是否满足大于当前最大size, 然后依次检查每列, 检查当前行在列中的区域位置
    3.  def orderOfLargestPlusSign(self, N, mines):
    4.      rows, cols = \[\[-1, N\] for \_ in xrange(N)\], \[\[-1, N\] for \_ in xrange(N)\] # initial region
    5.      for r, c in mines:
    6.          rows\[r\].append(c); cols\[c\].append(r) # add region splitter
    7.      for i in xrange(N):
    8.          rows\[i\].sort(); cols\[i\].sort()
    9.  
    10.      mxp = 0
    11.      for r in xrange(N):
    12.          for i in xrange(len(rows\[r\])-1):
    13.              left\_b, right\_b = rows\[r\]\[i\], rows\[r\]\[i+1\]            # region left/right boundary
    14.              for c in xrange(left\_b+mxp+1, right\_b-mxp): # right\_b - left\_b > mxp
    15.                  idx = bisect.bisect\_right(cols\[c\], r)-1
    16.                  up\_b = cols\[c\]\[idx\]
    17.                  down\_b = cols\[c\]\[idx+1\]
    18.                  mxp = max(mxp, min(c-left\_b, right\_b-c, r-up\_b, down\_b-r))
    19.      return mxp
*   [kth-smallest-element-in-a-sorted-matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/): 找到数组中第k小的数? [details refer to leetcode discussion](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code)
    1.  用heap, 保留数字所在位置(v, i, j), 从最小的数字开始寻找下一个
    2.  binary search base on range, low = matrix\[0\]\[0\], high = max\[n-1\]\[m-1\]
*   升序数组中绝对值最小
    *   三种情况: 1) 都是正数, 返回第一个数, 2) 都是负数,最后一个数 3) 有正有负, 二分查找0插入的位置
*   [find-k-closest-elements](https://leetcode.com/problems/find-k-closest-elements/description/): 给定升序数组array, 以及target数x和k值, 找出数组中里x最近的k个数
    1.  public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
    2.      int lo = 0, hi = arr.size() - k;
    3.      while (lo < hi) {
    4.          int mid = (lo + hi) / 2;
    5.          if (x - arr.get(mid) > arr.get(mid+k) - x)
    6.              lo = mid + 1;
    7.          else
    8.              hi = mid;
    9.      }
    10.      return arr.subList(lo, lo + k);
    11.  }
*   [find-k-th-smallest-pair-distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance)
    *   https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/109082/Approach-the-problem-using-the-%22trial-and-error%22-algorithm



----

- Date: 2019-01-02
- Tags: #Interview/Programing 



