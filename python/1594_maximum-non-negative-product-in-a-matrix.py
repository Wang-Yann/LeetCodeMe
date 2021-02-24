#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 08:24:19
# @Last Modified : 2021-02-24 08:24:19
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个大小为 rows x cols 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。 
# 
#  在从左上角 (0, 0) 开始到右下角 (rows - 1, cols - 1) 结束的所有路径中，找出具有 最大非负积 的路径。路径的积是沿路径访问的单
# 元格中所有整数的乘积。 
# 
#  返回 最大非负积 对 109 + 7 取余 的结果。如果最大积为负数，则返回 -1 。 
# 
#  注意，取余是在得到最大积之后执行的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[-1,-2,-3],
#              [-2,-3,-3],
#              [-3,-3,-2]]
# 输出：-1
# 解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,-2,1],
#              [1,-2,1],
#              [3,-4,1]]
# 输出：8
# 解释：最大非负积对应的路径已经用粗体标出 (1 * 1 * -2 * -4 * 1 = 8)
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1, 3],
#              [0,-4]]
# 输出：0
# 解释：最大非负积对应的路径已经用粗体标出 (1 * 0 * -4 = 0)
#  
# 
#  示例 4： 
# 
#  输入：grid = [[ 1, 4,4,0],
#              [-2, 0,0,1],
#              [ 1,-1,1,1]]
# 输出：2
# 解释：最大非负积对应的路径已经用粗体标出 (1 * -2 * 1 * -1 * 1 * 1 = 2)
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= rows, cols <= 15 
#  -4 <= grid[i][j] <= 4 
#  
#  Related Topics 贪心算法 动态规划 
#  👍 22 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        Max = [[0] * C for _ in range(R)]
        Min = [[0] * C for _ in range(R)]
        Max[0][0] = grid[0][0]
        Min[0][0] = grid[0][0]
        for j in range(1, C):
            Max[0][j] = Max[0][j - 1] * grid[0][j]
            Min[0][j] = Min[0][j - 1] * grid[0][j]

        for i in range(1, R):
            Max[i][0] = Max[i - 1][0] * grid[i][0]
            Min[i][0] = Min[i - 1][0] * grid[i][0]
        for i in range(1, R):
            for j in range(1, C):
                if grid[i][j] > 0:
                    Max[i][j] = max(Max[i - 1][j], Max[i][j - 1]) * grid[i][j]
                    Min[i][j] = min(Min[i - 1][j], Min[i][j - 1]) * grid[i][j]
                else:
                    Max[i][j] = min(Min[i - 1][j], Min[i][j - 1]) * grid[i][j]
                    Min[i][j] = max(Max[i - 1][j], Max[i][j - 1]) * grid[i][j]
        MOD=10**9+7
        return Max[-1][-1] % MOD if Max[-1][-1] >= 0 else -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(grid=[[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]), -1],
    [dict(grid=[[1, -2, 1],
                [1, -2, 1],
                [3, -4, 1]]), 8],
    [dict(grid=[[1, 3],
                [0, -4]]), 0],
    [dict(grid=[[1, 4, 4, 0],
                [-2, 0, 0, 1],
                [1, -1, 1, 1]]), 2],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maxProductPath(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
