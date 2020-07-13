#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 18:33:11
# @Last Modified : 2020-07-13 18:33:11
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一只蚂蚁坐在由白色和黑色方格构成的无限网格上。开始时，网格全白，蚂蚁面向右侧。每行走一步，蚂蚁执行以下操作。 
# 
#  (1) 如果在白色方格上，则翻转方格的颜色，向右(顺时针)转 90 度，并向前移动一个单位。 
# (2) 如果在黑色方格上，则翻转方格的颜色，向左(逆时针方向)转 90 度，并向前移动一个单位。 
# 
#  编写程序来模拟蚂蚁执行的前 K 个动作，并返回最终的网格。 
# 
#  网格由数组表示，每个元素是一个字符串，代表网格中的一行，黑色方格由 'X' 表示，白色方格由 '_' 表示，蚂蚁所在的位置由 'L', 'U', 'R',
#  'D' 表示，分别表示蚂蚁 左、上、右、下 的朝向。只需要返回能够包含蚂蚁走过的所有方格的最小矩形。 
# 
#  示例 1: 
# 
#  输入: 0
# 输出: ["R"]
#  
# 
#  示例 2: 
# 
#  输入: 2
# 输出:
# [
#  "_X",
#  "LX"
# ]
#  
# 
#  示例 3: 
# 
#  输入: 5
# 输出:
# [
#  "_U",
#  "X_",
#  "XX"
# ]
#  
# 
#  说明： 
# 
#  
#  K <= 100000 
#  
#  Related Topics 数组 
#  👍 8 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def printKMoves(self, K: int) -> List[str]:
        R, T, L, D = 0, 0, 0, 0

        def move_ant(ant):
            nonlocal R, T, L, D
            y, x = ant[0]
            if ant[1] == 0:
                ant[0] = (y, x + 1)
            if ant[1] == 1:
                ant[0] = (y + 1, x)
            if ant[1] == 2:
                ant[0] = (y, x - 1)
            if ant[1] == 3:
                ant[0] = (y - 1, x)
            y, x = ant[0]
            R, T, L, D = max(R, x), min(T, y), min(L, x), max(D, y)

        ant = [(0, 0), 0]  # 0-R 1-D 2-L 3-U
        grids = collections.defaultdict(lambda: '_')
        for _ in range(K):
            if grids[ant[0]] == 'X':  # black
                ant[1] = (ant[1] + 3) % 4
                grids[ant[0]] = '_'
            else:  # white
                ant[1] = (ant[1] + 1) % 4
                grids[ant[0]] = 'X'
            move_ant(ant)

        grids[ant[0]] = ['R', 'D', 'L', 'U'][ant[1]]
        return [''.join([grids[(y, x)] for x in range(L, R + 1)]) for y in range(T, D + 1)]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (0, ["R"]),
    (2, ["_X", "LX"]),
    (5, ["_U", "X_", "XX"]),
])
def test_solutions(args, expected):
    assert Solution().printKMoves(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
