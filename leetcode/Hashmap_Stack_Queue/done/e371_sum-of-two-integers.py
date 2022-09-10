'''
https://leetcode.com/problems/sum-of-two-integers
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.


Example 1:


Input: a = 1, b = 2
Output: 3



Example 2:


Input: a = -2, b = 3
Output: 1


'''


# class Solution {
# public:
#     int getSum(int a, int b) {
#         return add(a, b);
#     }
    
#     int add(int a, int b) {
#         int sum = a;
#         int carry = b;
#         while(carry) {
#             int tmps = sum;
#             sum = tmps ^ carry;
#             carry = (tmps & carry) << 1;
#         }
    
#         return sum;
#     }
#     int subtract(int a, int b) {
#         int subtrahend = add(~b, 1);
#         int sub = add(a, subtrahend);
#         return sub;
#     }
# };