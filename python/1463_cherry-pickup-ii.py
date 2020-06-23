#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 rows x cols 的矩阵 grid 来表示一块樱桃地。 grid 中每个格子的数字表示你能获得的樱桃数目。 
# 
#  你有两个机器人帮你收集樱桃，机器人 1 从左上角格子 (0,0) 出发，机器人 2 从右上角格子 (0, cols-1) 出发。 
# 
#  请你按照如下规则，返回两个机器人能收集的最多樱桃数目： 
# 
#  
#  从格子 (i,j) 出发，机器人可以移动到格子 (i+1, j-1)，(i+1, j) 或者 (i+1, j+1) 。 
#  当一个机器人经过某个格子时，它会把该格子内所有的樱桃都摘走，然后这个位置会变成空格子，即没有樱桃的格子。 
#  当两个机器人同时到达同一个格子时，它们中只有一个可以摘到樱桃。 
#  两个机器人在任意时刻都不能移动到 grid 外面。 
#  两个机器人最后都要到达 grid 最底下一行。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# 输出：24
# 解释：机器人 1 和机器人 2 的路径在上图中分别用绿色和蓝色表示。
# 机器人 1 摘的樱桃数目为 (3 + 2 + 5 + 2) = 12 。
# 机器人 2 摘的樱桃数目为 (1 + 5 + 5 + 1) = 12 。
# 樱桃总数为： 12 + 12 = 24 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1
# ,0,2,3,0,0,6]]
# 输出：28
# 解释：机器人 1 和机器人 2 的路径在上图中分别用绿色和蓝色表示。
# 机器人 1 摘的樱桃数目为 (1 + 9 + 5 + 2) = 17 。
# 机器人 2 摘的樱桃数目为 (1 + 3 + 4 + 3) = 11 。
# 樱桃总数为： 17 + 11 = 28 。
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
# 输出：22
#  
# 
#  示例 4： 
# 
#  输入：grid = [[1,1],[1,1]]
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == grid.length 
#  cols == grid[i].length 
#  2 <= rows, cols <= 70 
#  0 <= grid[i][j] <= 100 
#  
#  Related Topics 动态规划

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        dfs(x1,y1,y2)表示机器人1在(x1,y1),机器人2在(x1,y2)时能摘到最多的樱桃数
        """
        m, n = len(grid), len(grid[0])

        @functools.lru_cache(None)
        def dfs(x1, y1, y2):
            if x1 == m:
                return 0
            res = grid[x1][y1]
            ans = 0
            if y1 != y2:
                res += grid[x1][y2]
            for ny1 in (y1 - 1, y1, y1 + 1):
                for ny2 in (y2 - 1, y2, y2 + 1):
                    if 0 <= ny1 <= n - 1 and 0 <= ny2 <= n - 1:
                        ans = max(ans, dfs(x1 + 1, ny1, ny2))
            return res + ans

        return dfs(0, 0, n - 1)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]), 24],
    [dict(grid=[[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                [1, 0, 2, 3, 0, 0, 6]]), 28],
    [dict(grid=[[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]), 22],
    [dict(grid=[[1, 1], [1, 1]]), 4],
])
def test_solutions(kw, expected):
    assert Solution().cherryPickup(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
