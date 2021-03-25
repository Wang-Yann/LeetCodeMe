#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你还记得那条风靡全球的贪吃蛇吗？ 
# 
#  我们在一个 n*n 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（(0, 0) 和 (0, 1)）开始移动。我们用
#  0 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（(n-1, n-2) 和 (n-1, n-1)）。 
# 
#  每次移动，蛇可以这样走： 
# 
#  
#  如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。 
#  如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。 
#  如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（(r, c)、(r, c+1)）移动到 （(r, c)、(r+1, c)）。
#  
#  
#  如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（(r, c)、(r+1, c)）移动到（(r, c)、(r, c+1)）。 
# 
#  
#  
# 
#  返回蛇抵达目的地所需的最少移动次数。 
# 
#  如果无法到达目的地，请返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[0,0,0,0,0,1],
#                [1,1,0,0,1,0],
#               [0,0,0,0,1,1],
#               [0,0,1,0,1,0],
#               [0,1,1,0,0,0],
#               [0,1,1,0,0,0]]
# 输出：11
# 解释：
# 一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。
#  
# 
#  示例 2： 
# 
#  输入：grid = [[0,0,1,1,1,1],
#               [0,0,0,0,1,1],
#               [1,1,0,0,0,1],
#               [1,1,1,0,0,1],
#               [1,1,1,0,0,1],
#               [1,1,1,0,0,0]]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 100 
#  0 <= grid[i][j] <= 1 
#  蛇保证从空单元格开始出发。 
#  
#  Related Topics 广度优先搜索

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        """
        GOOD
        https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/discuss/392940/Standard-Python-BFS-solution
        """
        N = len(grid)
        start = (0, 0, 0, 1)
        end = (N - 1, N - 2, N - 1, N - 1)
        curr_level = {start}
        moves = 0
        visited = set()
        while curr_level:
            next_level = set()
            for pos in curr_level:
                visited.add(pos)
                r1, c1, r2, c2 = pos
                # 水平，垂直，顺时针，逆时针
                if c1 + 1 < N and grid[r1][c1 + 1] == 0 and c2 + 1 < N and grid[r2][c2 + 1] == 0:
                    if (r1, c1 + 1, r2, c2 + 1) not in visited:
                        next_level.add((r1, c1 + 1, r2, c2 + 1))
                if r1 + 1 < N and grid[r1 + 1][c1] == 0 and r2 + 1 < N and grid[r2 + 1][c2] == 0:
                    if (r1 + 1, c1, r2 + 1, c1) not in visited:
                        next_level.add((r1 + 1, c1, r2 + 1, c2))
                if r1 == r2 and c2 == c1 + 1 and r1 + 1 < N and grid[r1 + 1][c1] + grid[r1 + 1][c1 + 1] == 0:
                    if (r1, c1, r1 + 1, c1) not in visited:
                        next_level.add((r1, c1, r1 + 1, c1))
                if c1 == c2 and r2 == r1 + 1 and c1 + 1 < N and grid[r1][c1 + 1] + grid[r1 + 1][c1 + 1] == 0:
                    if (r1, c1, r1, c1 + 1) not in visited:
                        next_level.add((r1, c1, r1, c1 + 1))
            if end in next_level:
                return moves + 1
            curr_level = next_level
            moves += 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(
        grid=[[0, 0, 0, 0, 0, 1],
              [1, 1, 0, 0, 1, 0],
              [0, 0, 0, 0, 1, 1],
              [0, 0, 1, 0, 1, 0],
              [0, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 0, 0]]
    ), 11],
    [dict(
        grid=[[0, 0, 1, 1, 1, 1],
              [0, 0, 0, 0, 1, 1],
              [1, 1, 0, 0, 0, 1],
              [1, 1, 1, 0, 0, 1],
              [1, 1, 1, 0, 0, 1],
              [1, 1, 1, 0, 0, 0]]
    ), 9],
])
def test_solutions(kw, expected):
    assert Solution().minimumMoves(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
