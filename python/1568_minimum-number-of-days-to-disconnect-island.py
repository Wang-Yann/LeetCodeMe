#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 03:02:33
# @Last Modified : 2021-02-22 03:02:33
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个由若干 0 和 1 组成的二维网格 grid ，其中 0 表示水，而 1 表示陆地。岛屿由水平方向或竖直方向上相邻的 1 （陆地）连接形成。 
# 
#  如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。 
# 
#  一天内，可以将任何单个陆地单元（1）更改为水单元（0）。 
# 
#  返回使陆地分离的最少天数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：2
# 解释：至少需要 2 天才能得到分离的陆地。
# 将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。
#  
# 
#  示例 2： 
# 
#  输入：grid = [[1,1]]
# 输出：2
# 解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。
#  
# 
#  示例 3： 
# 
#  输入：grid = [[1,0,1,0]]
# 输出：0
#  
# 
#  示例 4： 
# 
#  输入：grid = [[1,1,0,1,1],
#              [1,1,1,1,1],
#              [1,1,0,1,1],
#              [1,1,0,1,1]]
# 输出：1
#  
# 
#  示例 5： 
# 
#  输入：grid = [[1,1,0,1,1],
#              [1,1,1,1,1],
#              [1,1,0,1,1],
#              [1,1,1,1,1]]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length, grid[i].length <= 30 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 贪心算法 
#  👍 22 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        """脑筋急转弯啊
        求解无向图的割点可以用 Tarjan 算法，但由于其明显超出了面试难度，在笔试中也几乎不可能出现
        """

        def dfs(x: int, y: int):
            grid[x][y] = 2
            for tx, ty in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
                if 0 <= tx < R and 0 <= ty < C and grid[tx][ty] == 1:
                    dfs(tx, ty)

        def count():
            cnt = 0
            for i in range(R):
                for j in range(C):
                    if grid[i][j] == 1:
                        cnt += 1
                        dfs(i, j)
            # 还原
            for i in range(R):
                for j in range(C):
                    if grid[i][j] == 2:
                        grid[i][j] = 1
            return cnt

        R, C = len(grid), len(grid[0])

        # 岛屿数量不为 1，陆地已经分离
        if count() != 1:
            return 0

        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    grid[i][j] = 0
                    if count() != 1:
                        # 更改一个陆地单元为水单元后陆地分离
                        return 1
                    grid[i][j] = 1

        return 2


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(grid=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]), 2],
    [dict(grid=[[1, 1]]), 2],
    [dict(grid=[[1, 0, 1, 0]]), 0],
    [dict(grid=[[1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 0, 1, 1]]), 1],
    [dict(grid=[[1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1]]), 2],
])
def test_solutions(kw, expected):
    assert Solution().minDays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
