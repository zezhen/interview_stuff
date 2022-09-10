# 双向DP - cherry pickup
----

1.  比如[cherry-pickup](https://leetcode.com/problems/cherry-pickup/description/), grid的每个cell表示这块区域的cherry量, 从(0,0)出发摘取cherry, 向下或向右到(n-1, n-1), 再向上向左返回(0,0), 求最大可摘取的cherry数量.
    1.  ![[Archive/面试资料/Programming/_resources/双向DP_-_cherry_pickup.resources/unknown_filename.png]]
2.  这题太hard, 所有想到的都是brute force, [fun4LeetCode](https://leetcode.com/problems/cherry-pickup/discuss/109903/Step-by-step-guidance-of-the-O(N3)-time-and-O(N2)-space-solution) 有非常详细的解答, 或许还有其他思路
    1.  Constraint: once a cherry is picked up, the original cell (value 1) becomes an empty cell (value 0)
    2.  思路1: 因为这个constraint, 需要修改grid才可以, 因此我们需要维护一个状态信息, 状态空间又是非常大, 依然是指数复杂度.
    3.  问题的重点在于两个路径是否重复, 如果没有, 那就无所谓了, 如何避免重复呢?
    4.  首先, 将构建为T(i,j), 表示(0,0) -> (i,j) -> (0,0)的cherry量, 问题答案即为T(n-1, n-1), 对于T(i,j)有如下四种可能性:
        1.  Case 1: (0, 0) ==> (i-1, j) ==> (i, j) ==> (i-1, j) ==> (0, 0)
        2.  Case 2: (0, 0) ==> (i, j-1) ==> (i, j) ==> (i, j-1) ==> (0, 0)
        3.  Case 3: (0, 0) ==> (i-1, j) ==> (i, j) ==> (i, j-1) ==> (0, 0)
        4.  Case 4: (0, 0) ==> (i, j-1) ==> (i, j) ==> (i-1, j) ==> (0, 0)
    5.  Case 1即为T(i-1,j) + grid\[i\]\[j\], case 2 即为 T(i, j-1) + grid\[i\]\[j\], 如何表示case 3,4呢?
    6.  我们将问题拓展一下将T(i, j)改写成T(i,j,p,q), 即表示(0, 0) ==> (i, j); (p, q) ==> (0, 0), 如上四个case就变成了
        1.  Case 1: (0, 0) ==> (i-1, j) ==> (i, j); (p, q) ==> (p-1, q) ==> (0, 0)
        2.  Case 2: (0, 0) ==> (i-1, j) ==> (i, j); (p, q) ==> (p, q-1) ==> (0, 0)
        3.  Case 3: (0, 0) ==> (i, j-1) ==> (i, j); (p, q) ==> (p-1, q) ==> (0, 0)
        4.  Case 4: (0, 0) ==> (i, j-1) ==> (i, j); (p, q) ==> (p, q-1) ==> (0, 0)
    7.  Case 1即为T(i-1, j, p-1, q) + grid\[i\]\[j\] + grid\[p\]\[q\] ,
    8.  综合4种case, T(i, j, p, q) = grid\[i\]\[j\] + grid\[p\]\[q\] + max{T(i-1, j, p-1, q), T(i-1, j, p, q-1), T(i, j-1, p-1, q), T(i, j-1, p, q-1)}
    9.  如何避免grid\[i\]\[j\]\]出现在其他子结构中呢? 对于第一步, 比如(0, 0) ==> (i-1, j) ==> (i, j), 肯定没问题, 因为向下或向右, 所以leg 1的取值范围在\[(0,0), (i,j)\], 对于第二步(p, q) ==> (p-1, q) ==> (0, 0), 因为向左或向上, 其取值范围在\[(0,0), (p, q)\], 所以只要保证 (i,j)不在\[(0,0), (p, q)\]范围, 对于(p,q)亦然, 所以我们得到如下规则.
        1.  i < p && j > q
        2.  i == p && j == q
        3.  i > p && j < q
    10.  因为i, j, p, q满足一定的反相关性, 可以选择某种公式, 使得i与j自动能够自动调整, 而无需每次都检查, 也降低了维度 (现在是4维)
    11.  作者选择了n = i + j = p + q (很牛逼!!), 如此T(i, j, p, q) \= T(i, n-i, p, n-p) \=> T(n, i, p)
    12.  新的推导公式即为T(n, i, p) = grid\[i\]\[n-i\] + grid\[p\]\[n-p\] + max{T(n-1, i-1, p-1), T(n-1, i-1, p), T(n-1, i, p-1), T(n-1, i, p)}.
    13.  如此即可得三维矩阵可求解, 因为T(n, \*)只与T(n-1,\*)相关, 所以空间可以降为O(n^2), 时间为O(n^3)
3.  Java
    1.  public int cherryPickup(int\[\]\[\] grid) {
    2.   int N = grid.length, M = (N << 1) - 1;
    3.   int\[\]\[\] dp = new int\[N\]\[N\];
    4.   dp\[0\]\[0\] = grid\[0\]\[0\];
    
    6.   for (int n = 1; n < M; n++) {
    7.   for (int i = N - 1; i >= 0; i--) {
    8.   for (int p = N - 1; p >= 0; p--) {
    9.   int j = n - i, q = n - p;
    
    11.   if (j < 0 || j >= N || q < 0 || q >= N || grid\[i\]\[j\] < 0 || grid\[p\]\[q\] < 0) {
    12.   dp\[i\]\[p\] = \-1;
    13.   continue;
    14.   }
    
    16.   if (i > 0) dp\[i\]\[p\] = Math.max(dp\[i\]\[p\], dp\[i - 1\]\[p\]);
    17.   if (p > 0) dp\[i\]\[p\] = Math.max(dp\[i\]\[p\], dp\[i\]\[p - 1\]);
    18.   if (i > 0 && p > 0) dp\[i\]\[p\] = Math.max(dp\[i\]\[p\], dp\[i - 1\]\[p - 1\]);
    
    20.   if (dp\[i\]\[p\] >= 0) dp\[i\]\[p\] += grid\[i\]\[j\] + (i != p ? grid\[p\]\[q\] : 0)
    21.   }
    22.   }
    23.   }
    
    25.   return Math.max(dp\[N - 1\]\[N - 1\], 0);
    26.  }



----

- Date: 2019-02-18
- Tags: #Interview/Programing 



