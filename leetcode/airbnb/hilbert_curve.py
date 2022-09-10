# -*- coding: utf-8 -*-
'''
hilbert curve: refer to https://www.youtube.com/watch?v=3s7h2MHQtxc&t=288s

每次给你一个(x,   y,  iter)，问你在 iter 这张图中在(x, y)坐标的点是第几个？

'''

def hc_seq(x, y, order):
    if order == 0: return 1

    half_len = 1 << (order - 1)
    quarter_number = half_len * half_len

    if x >= half_len and y >= half_len:
        # quadrant 3, no rotation
        return 2 * quarter_number + hc_seq(x - half_len, y - half_len, order - 1)
    elif x < half_len and y >= half_len:
        # quadrant 2, no rotation
        return quarter_number + hc_seq(x, y - half_len, order - 1)
    elif x < half_len and y < half_len:
        # quadrant 1, clock-wise rotate 90 degree
        return hc_seq(y, x, order - 1)
    else:
        # quadrant 4, reverse clock-wise rotate 90 degree 
        return 3 * quarter_number + hc_seq(half_len-y-1, 2* half_len-x-1, order-1)

