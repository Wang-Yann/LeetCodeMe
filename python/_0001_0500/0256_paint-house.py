#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 14:08:07
# @Last Modified : 2020-07-22 14:08:07
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。 
# 
#  当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的矩阵来表示的。 
# 
#  例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。请你计算出粉刷
# 完所有房子最少的花费成本。 
# 
#  注意： 
# 
#  所有花费均为正整数。 
# 
#  示例： 
# 
#  输入: [[17,2,17],[16,16,5],[14,3,19]]
# 输出: 10
# 解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
#      最少花费: 2 + 5 + 3 = 10。
#  
#  Related Topics 动态规划 
#  👍 54 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """AC"""
        c1_c2 = c1_c3 = c2_c1 = c2_c3 = c3_c1 = c3_c2 = 0
        for d1, d2, d3 in costs:
            (c1_c2, c1_c3, c2_c1, c2_c3, c3_c1, c3_c2) = (min(c2_c1, c3_c1) + d2,
                                                          min(c2_c1, c3_c1) + d3,
                                                          min(c1_c2, c3_c2) + d1,
                                                          min(c1_c2, c3_c2) + d3,
                                                          min(c1_c3, c2_c3) + d1,
                                                          min(c1_c3, c2_c3) + d2)
        # print(c1_c2, c1_c3, c2_c1, c2_c3, c3_c1, c3_c2)
        return min(c1_c2, c1_c3, c2_c1, c2_c3, c3_c1, c3_c2)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(costs=[[17, 2, 17], [16, 16, 5], [14, 3, 19]]), 10],
    [dict(costs=[[3, 5, 3], [6, 17, 6], [7, 13, 18], [9, 10, 18]]), 26],
])
def test_solutions(kw, expected):
    assert Solution().minCost(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
