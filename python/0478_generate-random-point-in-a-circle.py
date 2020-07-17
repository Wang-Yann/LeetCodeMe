#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 15:43:38
# @Last Modified : 2020-05-05 15:43:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定圆的半径和圆心的 x、y 坐标，写一个在圆中产生均匀随机点的函数 randPoint 。
#
#  说明:
#
#
#  输入值和输出值都将是浮点数。
#  圆的半径和圆心的 x、y 坐标将作为参数传递给类的构造函数。
#  圆周上的点也认为是在圆中。
#  randPoint 返回一个包含随机点的x坐标和y坐标的大小为2的数组。
#
#
#  示例 1：
#
#
# 输入:
# ["Solution","randPoint","randPoint","randPoint"]
# [[1,0,0],[],[],[]]
# 输出: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
#
#
#  示例 2：
#
#
# 输入:
# ["Solution","randPoint","randPoint","randPoint"]
# [[10,5,-7.5],[],[],[]]
# 输出: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
#
#  输入语法说明：
#
#  输入是两个列表：调用成员函数名和调用的参数。Solution 的构造函数有三个参数，圆的半径、圆心的 x 坐标、圆心的 y 坐标。randPoint 没有
# 参数。输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。
#  Related Topics 数学 Random Rejection Sampling
#  👍 31 👎 0

"""

import math
import random
from typing import List


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.__radius = radius
        self.__x = x_center
        self.__y = y_center

    def randPoint(self) -> List[float]:
        r = self.__radius * math.sqrt(random.uniform(0, 1))
        theta = (2 * math.pi) * random.uniform(0, 1)
        return [self.__x + r * math.cos(theta), self.__y + r * math.sin(theta)]


if __name__ == '__main__':
    obj = Solution(1, 0, 0)
    ops_list = ["Solution", "randPoint", "randPoint", "randPoint"]
    args_list = [[1, 0, 0], [], [], []]

    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))
