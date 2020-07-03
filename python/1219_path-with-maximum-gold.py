#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄
# 金数量；如果该单元格是空的，那么就是 0。 
# 
#  为了使收益最大化，矿工需要按以下规则来开采黄金： 
# 
#  
#  每当矿工进入一个单元，就会收集该单元格中的所有黄金。 
#  矿工每次可以从当前位置向上下左右四个方向走。 
#  每个单元格只能被开采（进入）一次。 
#  不得开采（进入）黄金数目为 0 的单元格。 
#  矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
# 输出：24
# 解释：
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# 一种收集最多黄金的路线是：9 -> 8 -> 7。
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# 输出：28
# 解释：
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# 一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length, grid[i].length <= 15 
#  0 <= grid[i][j] <= 100 
#  最多 25 个单元格中有黄金。 
#  
#  Related Topics 回溯算法

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if not (0 <= r <= m - 1 and 0 <= c <= n - 1 and grid[r][c] != 0):
                return 0
            origin = grid[r][c]
            grid[r][c] = 0
            maxGold = 0
            for nr, nc in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                maxGold = max(maxGold, dfs(nr, nc))
            grid[r][c] = origin
            return maxGold + origin

        return max(dfs(r, c) for c in range(n) for r in range(m))


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    ), 24),
    pytest.param(dict(grid=[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]), 28),
])
def test_solutions(kwargs, expected):
    assert Solution().getMaximumGold(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
