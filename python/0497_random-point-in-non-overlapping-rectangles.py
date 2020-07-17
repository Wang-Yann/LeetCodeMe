#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-01 22:24:30
# @Last Modified : 2020-05-01 22:24:30
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个非重叠轴对齐矩形的列表 rects，写一个函数 pick 随机均匀地选取矩形覆盖的空间中的整数点。
#
#  提示：
#
#
#  整数点是具有整数坐标的点。
#  矩形周边上的点包含在矩形覆盖的空间中。
#  第 i 个矩形 rects [i] = [x1，y1，x2，y2]，其中 [x1，y1] 是左下角的整数坐标，[x2，y2] 是右上角的整数坐标。
#  每个矩形的长度和宽度不超过 2000。
#  1 <= rects.length <= 100
#  pick 以整数坐标数组 [p_x, p_y] 的形式返回一个点。
#  pick 最多被调用10000次。
#
#
#
#
#  示例 1：
#
#
# 输入:
# ["Solution","pick","pick","pick"]
# [[[[1,1,5,5]]],[],[],[]]
# 输出:
# [null,[4,1],[4,1],[3,3]]
#
#
#  示例 2：
#
#
# 输入:
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# 输出:
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
#
#
#
#  输入语法的说明：
#
#  输入是两个列表：调用的子例程及其参数。Solution 的构造函数有一个参数，即矩形数组 rects。pick 没有参数。参数总是用列表包装的，即使没有也
# 是如此。
#
#
#  Related Topics 二分查找 Random
#  👍 20 👎 0

"""
import bisect
from random import randint

from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        """第 i 个矩形 rects [i] = [x1，y1，x2，y2]，其中 [x1，y1] 是左下角的整数坐标，[x2，y2] 是右上角的整数坐标"""
        self.__rects = rects
        self.__prefix_sum = list(map(lambda x:(x[2] - x[0] + 1) * (x[3] - x[1] + 1), rects))
        # 按序累加每个矩形的面积（即权重)
        for i in range(1, len(self.__prefix_sum)):
            self.__prefix_sum[i] += self.__prefix_sum[i - 1]

    def pick(self) -> List[int]:
        target = randint(0, self.__prefix_sum[-1] - 1)
        left = bisect.bisect_right(self.__prefix_sum, target)
        rect = self.__rects[left]
        width, height = rect[2] - rect[0] + 1, rect[3] - rect[1] + 1
        base = self.__prefix_sum[left] - width * height
        return [rect[0] + (target - base) % width, rect[1] + (target - base) // width]


if __name__ == '__main__':
    obj = Solution([[-2, -2, -1, -1], [1, 0, 3, 0]])
    # ops_list = ["Solution","pick","pick","pick"]
    # args_list =[[[[1,1,5,5]]],[],[],[]]
    ops_list = ["Solution", "pick", "pick", "pick", "pick", "pick"]
    args_list = [[[[-2, -2, -1, -1], [1, 0, 3, 0]]], [], [], [], [], []]

    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))
