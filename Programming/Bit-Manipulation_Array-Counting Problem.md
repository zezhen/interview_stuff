# Bit-Manipulation/Array-Counting Problem
----



1.  计数问题
    1.  可以采用求和的方法解决 (暂时不考虑溢出情况) 
        1.  一个一次+多个2次: 2 \* sum(set(nums)) - sum(nums)
        2.  一次一次+多个3次: (3 \* sum(set(nums)) - sum(nums)) / 2
        3.  ... 
    2.  统计一个数字在排序数组中出现的次数
        *   变形二分查找, 找到左右位置
    3.  重复数组中只出现一次的数/多次的数
        1.  一个一次+多个偶数次: 异或所有数, x=a^b^b=a, 异或结果x便是要找的数
        2.  两个一次+多个偶数次: 异或所有数, x=a^b, 找到x中最后一位0, 假设第i位, ai ^ bi = 0, 即两者要么1要么0, 可以区分
        3.  三个一次+多个偶数次: 转换成问题#2, x=a^b^c, 找到x中最后一位1, 假设第j位, 该位置所有其他元素都是成对出现, 比如ai=bi != ci, 由此可以区分出c, 然后在区分a和b
        4.  其他情况: bitmap or hashmap
    4.  奇数次
    5.  众数问题
        1.  [Majority Element](https://leetcode.com/problems/majority-element): 一个数超过n/2
        2.  [Majority Element II](https://leetcode.com/problems/majority-element-ii): 超过n/3的数




\# **Bit-Manipulation**
****
[Detailed explanation and generalization of the bitwise operation method for single numbers](https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers): "Given an array of integers, every element appears k (k > 1) times except for one, which appears p times (p >= 1, p % k != 0). Find that single one."
\=> Very good explanation, start from 1-bit example, then extend to 32-bits problem (not fully understand yet.)

code example:
x1 = x2 = … = xm = 0    # m  = math.ceiling(log k)
for (int i : nums) {
 xm ^= (xm-1 & ... & x1 & i);
 xm-1 ^= (xm-2 & ... & x1 & i);
 .....
 x1 ^= i;

 mask = ~(y1 & y2 & ... & ym) where yj = xj if kj = 1, and yj = ~xj if kj = 0 (j = 1 to m).

 xm &= mask;
 ......
 x1 &= mask;
}


1.  [single-number](https://leetcode.com/problems/single-number): 一个一次+多个偶数次
    *   异或所有数, x=a^b^b=a, 异或结果x便是要找的数
    *   int x1 = 0;
    *   for (int i : nums) {
    *       x1 ^= i;
    *   }
    *   return x1;
2.  [single-number-ii](https://leetcode.com/problems/single-number-ii): 一个一次+多个三次
    1.  int x1 = 0, x2 = 0, mask = 0;
    2.  for (int i : nums) {
    3.      x2 ^= x1 & i;
    4.      x1 ^= i;
    5.      mask = ~(x1 & x2);
    6.      x2 &= mask;
    7.      x1 &= mask;
    8.  }
    9.  return x1;  // Since p = 1, in binary form p = '01', then p1 = 1, so we should return x1.
    10.              // If p = 2, in binary form p = '10', then p2 = 1, and we should return x2.
    11.              // Or alternatively we can simply return (x1 | x2).
3.  [single-number-iii](https://leetcode.com/problems/single-number-iii): 两个1次+多个2次 (与上两题不同, 单独解决)
    
    *   用xor扫两次:
    
    1.  xor所有数, 得到x = a^b, 因为a!=b, x非0, 有些位bit=1, 说明a与b在这些位上不同
    2.  将所有数按照这些位分位两组, 选取最后一位即可 x &= -x
    3.  重新扫描, 根据 num\[i\] & x 是否为1分组xor
    
    2.  int diff = accumulate(nums.begin(), nums.end(), 0, bit\_xor<int>());
    3.  diff &= -diff;
    4.  
    5.  vector<int> rets = {0, 0};
    6.  for (int num : nums) {
    7.      if ((num & diff) == 0) {
    8.          rets\[0\] ^= num;
    9.      } else {
    10.          rets\[1\] ^= num;
    11.      }
    12.  }
    13.  return rets;
4.  [maximum-xor-of-two-numbers-in-an-array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array): 给定32位数数组, 找出两数异或的最大值. O(n)时间要求.
    1.  def findMaximumXOR(self, nums):
    2.      ans = mask = 0
    3.      for i in xrange(31, -1, -1): # start from significant bits
    4.          mask |= (1 << i)
    5.          andSet = set()
    6.          for num in nums:
    7.              andSet.add(mask & num) # bit i only has two possibilities, 0 or 1.
    8.          tmp = ans | (1 << i)
    9.          for prefix in andSet:
    10.              if (tmp ^ prefix) in andSet:    # tmp ^ prefix in andSet means there are two numbers has 0 or 1 in bit i
    11.                  ans = tmp
    12.                  break
    13.      return ans
5.  

**

**

----

- Date: 2018-12-28
- Tags: #Interview/Programing 



