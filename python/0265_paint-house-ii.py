#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 16:56:42
# @Last Modified : 2020-07-22 16:56:42
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假如有一排房子，共 n 个，每个房子可以被粉刷成 k 种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。 
# 
#  当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x k 的矩阵来表示的。 
# 
#  例如，costs[0][0] 表示第 0 号房子粉刷成 0 号颜色的成本花费；costs[1][2] 表示第 1 号房子粉刷成 2 号颜色的成本花费，以此
# 类推。请你计算出粉刷完所有房子最少的花费成本。 
# 
#  注意： 
# 
#  所有花费均为正整数。 
# 
#  示例： 
# 
#  输入: [[1,5,3],[2,9,4]]
# 输出: 5
# 解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5; 
#      或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5. 
#  
# 
#  进阶： 
# 您能否在 O(nk) 的时间复杂度下解决此问题？ 
#  Related Topics 动态规划 
#  👍 32 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        N = len(costs)
        k = len(costs[0])
        dp = [[0 for i in range(k)] for j in range(N)]
        dp[0] = costs[0]
        for i in range(1, N):
            for j in range(k):
                dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:]) + costs[i][j]
        return min(dp[N-1])


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(costs=[[1, 5, 3], [2, 9, 4]]), 5],
])
def test_solutions(kw, expected):
    assert Solution().minCostII(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
