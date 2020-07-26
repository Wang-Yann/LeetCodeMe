#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-26 21:58:43
# @Last Modified : 2020-07-26 21:58:43
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 给定一个非空01二维数组表示的网格，一个岛屿由四连通（上、下、左、右四个方向）的 1 组成，你可以认为网格的四周被海水包围。 
# 
#  请你计算这个网格中共有多少个形状不同的岛屿。如果两个岛屿的形状相同，或者通过旋转（顺时针旋转 90°，180°，270°）、翻转（左右翻转、上下翻转）后形
# 状相同，那么就认为这两个岛屿是相同的。 
# 
#  
# 
#  样例 1: 
# 
#  11000
# 10000
# 00001
# 00011
#  
# 
#  给定上图，返回结果 1。 
#  
# 注意 ： 
# 
#  11
# 1
#  
# 
#  和 
# 
#   1
# 11 
# 
#  是相同的岛屿。因为我们通过 180° 旋转第一个岛屿，两个岛屿的形状相同。 
# 
#  
# 
#  样例 2: 
# 
#  11100
# 10001
# 01001
# 01110 
# 
#  给定上图，返回结果 2。 
#  
# 下面是两个不同的岛屿： 
# 
#  111
# 1 
# 
#  和 
# 
#  1
# 1
#  
# 
#  
# 
#  注意 ： 
# 
#  111
# 1 
# 
#  和 
# 
#  1
# 111
#  
# 
#  相同的岛屿。因为我们通过上下翻转第一个岛屿，两个岛屿的形状相同。 
# 
#  
# 
#  注释 : 二维数组每维的大小都不会超过50。 
#  Related Topics 深度优先搜索 哈希表 
#  👍 19 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        """
        TODO
        """
        seen = set()
        R, C = len(grid), len(grid[0])

        def explore(r, c):
            if 0 <= r < R and 0 <= c < C and grid[r][c] and (r, c) not in seen:
                seen.add((r, c))
                shape.add(complex(r, c))
                explore(r + 1, c)
                explore(r - 1, c)
                explore(r, c + 1)
                explore(r, c - 1)

        def canonical(shape):
            """
            HARD
            模拟岛屿的旋转和翻转有很多种方法，在 Python 代码中，我们把坐标看成复数，每次将坐标乘以单位虚数 1j 就是一次旋转操作。对于翻转操作，将坐标的实部和虚部交换即可

            """

            def translate(shape):
                w = complex(min(z.real for z in shape),
                            min(z.imag for z in shape))
                return sorted(str(z - w) for z in shape)

            ans = []
            for k in range(4):
                ans = max(ans, translate([z * (1j) ** k for z in shape]))
                ans = max(ans, translate([complex(z.imag, z.real) * (1j) ** k for z in shape]))
            return tuple(ans)

        shapes = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                shape = set()
                explore(r, c)
                # print(shape)
                if shape:
                    shapes.add(canonical(shape))
        # print(shapes)
        return len(shapes)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([
         [1, 1, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 1, 1]
     ]
    , 1),
    pytest.param([
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],

    ], 2),
])
def test_solutions(args, expected):
    assert Solution().numDistinctIslands2(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
