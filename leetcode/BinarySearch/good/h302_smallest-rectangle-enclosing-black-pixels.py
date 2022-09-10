'''
https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/

An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example:

Input:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2

Output: 6
'''

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """

'''
expand from (x, y) and record the max/min position into (top, left, right, bottom), the area is (botton - top) * (right - left)

my solution:

1. maintain two structs: queue and visited
2. queue keep the board area (i, j), visited can be a map to keep the visited pisitions

optimal solution:

To find the left, array [0,left-1] are all 0, [left, y] is 1, so we can binary search to find left, set 
In the 2D array, we need to scan column m = (0+y)//2 to know whether there any pixel contains 1
if yes, go left, no then right.

same to top, right and bottom


# public class Solution {
#     public int minArea(char[][] image, int x, int y) {
#         int m = image.length, n = image[0].length;
#         int left = searchColumns(image, 0, y, 0, m, true);
#         int right = searchColumns(image, y + 1, n, 0, m, false);
#         int top = searchRows(image, 0, x, left, right, true);
#         int bottom = searchRows(image, x + 1, m, left, right, false);
#         return (right - left) * (bottom - top);
#     }
#     private int searchColumns(char[][] image, int i, int j, int top, int bottom, boolean whiteToBlack) {
#         while (i != j) {
#             int k = top, mid = (i + j) / 2;
#             while (k < bottom && image[k][mid] == '0') ++k;
#             if (k < bottom == whiteToBlack) // k < bottom means the column mid has black pixel
#                 j = mid; //search the boundary in the smaller half
#             else
#                 i = mid + 1; //search the boundary in the greater half
#         }
#         return i;
#     }
#     private int searchRows(char[][] image, int i, int j, int left, int right, boolean whiteToBlack) {
#         while (i != j) {
#             int k = left, mid = (i + j) / 2;
#             while (k < right && image[mid][k] == '0') ++k;
#             if (k < right == whiteToBlack) // k < right means the row mid has black pixel
#                 j = mid;
#             else
#                 i = mid + 1;
#         }
#         return i;
#     }
# }

'''